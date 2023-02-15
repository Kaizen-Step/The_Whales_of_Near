# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Swaps - The Whales of Near',
                   page_icon=':bar_chart:', layout='wide')
st.title('🥏Swaps')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Swap_list':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/4d83f6d7-8e36-4a83-bcbe-1a6932d5aaff/data/latest')
    elif query == 'NEAR_supply_richest':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ac3115a1-889a-42c2-a24c-6bca000fac66/data/latest')
    elif query == 'Swaps_from_Near':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/2661ca2d-0ae9-4713-ae8c-97fa2329dd7f/data/latest')
    elif query == 'Swaps_to_Near':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/8f3d6f0f-fdb5-4304-8adb-3a35ea945cf5/data/latest')
    return None


Swap_list = get_data('Swap_list')
NEAR_supply_richest = get_data('NEAR_supply_richest')
Swaps_from_Near = get_data('Swaps_from_Near')
Swaps_to_Near = get_data('Swaps_to_Near')

df = Swap_list
df2 = NEAR_supply_richest
df3 = Swaps_from_Near
df4 = Swaps_to_Near

#################################################################################################

st.write(""" ## Whales Swap  """)


st.write(""" the only wallet with swaps is "bb273c1b4fe46a54743de83f92513d644e57423d2fee2ad4549cd4b40737f3d3" """)


# list of one wallet swap activity

st.table(df)


# Platforms User Used
fig = px.bar(df2, x="Platforms", y="Number of Swap TX",
             color="Platforms", title='Top 10 Platforms Whales Used in Number of Transactions')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ### Top 20 Swaps from Near  """)

# Platforms User Used
fig = px.bar(df3, x="TRADER", y="volume of swaps",
             color="TRADER", title='Top 20 Swaps from Near Based on Near Amount')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ### Top 20 Swaps To Near  """)

# Platforms User Used
fig = px.bar(df4, x="TRADER", y="volume of swaps",
             color="TRADER", title='Top 20 Swaps to Near Based on Near Amount')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
