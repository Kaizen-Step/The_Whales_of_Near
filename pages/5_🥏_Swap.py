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
                   page_icon=':bar_chart:📈', layout='wide')
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
st.write(""" ### Swap Concept ##  """)

st.write("""
Crypto swapping is the process of exchanging crypto assets for their equivalent value in another coin or token. You can directly exchange crypto assets for another without intermediates involved in the process. Crypto swapping allows you to instantly trade one cryptocurrency for another, with no crypto-to-fiat exchange required. Saving time and paying less in fees are obvious benefits, but it's far from the only reason users participate in. [[7]](https://bitpay.com/blog/what-is-a-crypto-swap/#:~:text=Crypto%20swapping%20allows%20you%20to,reason%20users%20participate%20in%20swapping.)   """)


st.info(""" ##### In This Swap Section you can find: ####

* One and Only Whale Swap List  
* Platforms Whale Used for Swapping 
* Top 20 Swaps from Near (Not Whale List)
* Top 20 Swaps to Near (Not Whale List)


""")


#################################################################################################

st.write(""" ## Whales Swap  """)


st.write(""" The only wallet with swap transactions is "bb273c1b4fe46a54743de83f92513d644e57423d2fee2ad4549cd4b40737f3d3" in the following; you can find all his swap transactions with details.""")


# list of one wallet swap activity

st.table(df)


# Platforms User Used
fig = px.bar(df2, x="Platforms", y="Number of Swap TX",
             color="Platforms", title='Top 10 Platforms Whale Used in Number of Transactions')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" #### Top 20 Swaps from Near  """)

st.write(""" top 20 Near swapers were below list but none of them were among top 20 whales list. we use this chart to make a comparison between these top 20 and only whale. """)


# Platforms User Used
fig = px.bar(df3, x="TRADER", y="volume of swaps",
             color="TRADER", title='Top 20 Swaps from Near Based on Near Amount')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" #### Top 20 Swaps To Near  """)

# Platforms User Used
fig = px.bar(df4, x="TRADER", y="volume of swaps",
             color="TRADER", title='Top 20 Swaps to Near Based on Near Amount')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#################################################################################################

st.text(" \n")

st.info(""" #### Coclusion: ####

 * there were no significant swap transaction among top 20 Whale list 

""")
