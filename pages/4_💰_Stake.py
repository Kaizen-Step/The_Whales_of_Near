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
st.set_page_config(page_title='Stake - The Whales of Near',
                   page_icon=':bar_chart:', layout='wide')
st.title('💰Stake')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'NEAR_Stake':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/7d23a8c4-64de-484c-9d8d-045d17c40657/data/latest')
    elif query == 'NEAR_Unstake':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/233d8efc-a071-46f7-bacc-42317a39c663/data/latest')
    return None


NEAR_Stake = get_data('NEAR_Stake')
NEAR_Unstake = get_data('NEAR_Unstake')


df = NEAR_Stake
df2 = NEAR_Unstake

####################################################################################################

st.write(""" ## Stake Near """)

# Number of Stake Transactions Whales have done in last 12 Month
fig = px.bar(df, x="TX_SIGNER", y="Number of Stake TX",
             color="TX_SIGNER", title='Number of Stake Transactions Whales have done in last 12 Month')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Number of Stake')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Number of Stake Transactions Whales have done in last 12 Month
fig = px.bar(df, x="TX_SIGNER", y="Stake Amount",
             color="TX_SIGNER", title=' Amount of Near Staked by Whales in last 12 Month [Near]')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title="Stake Amount")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Number of Stake Transactions Whales have done in last 12 Month
fig = px.bar(df, x="Pool Name", y="Stake Amount",
             color="Pool Name", title=' Top Staked Pools Based on Near Amount ')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title="Stake Amount")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Whales Compare to Other Users Percentage of Transactions
fig = px.pie(df, values="Stake Amount",
             names="Pool Name", title=' Top Staked Pools Based on Near Amount ', hole=0.5)
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


################################################################################################

st.write(""" ## Unstake Near """)


# Number of Stake Transactions Whales have done in last 12 Month
fig = px.bar(df2, x="TX_SIGNER", y="Number of Stake TX",
             color="TX_SIGNER", title='Number of Unstake Transactions Whales have done in last 12 Month')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Number of Stake')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Number of Stake Transactions Whales have done in last 12 Month
fig = px.bar(df2, x="TX_SIGNER", y="Stake Amount",
             color="TX_SIGNER", title=' Amount of Near Unstaked by Whales in last 12 Month [Near]')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title="Stake Amount")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Number of Stake Transactions Whales have done in last 12 Month
fig = px.bar(df2, x="Pool Name", y="Stake Amount",
             color="Pool Name", title=' Top Untaked Pools Based on Near Amount ')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title="Stake Amount")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Whales Compare to Other Users Percentage of Transactions
fig = px.pie(df2, values="Stake Amount",
             names="Pool Name", title=' Top Unstaked Pools Based on Near Amount Percentage ', hole=0.5)
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
