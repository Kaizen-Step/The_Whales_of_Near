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
                   page_icon=':bar_chart:📈', layout='wide')
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
###########################################################################################################
st.write(""" ### Stake Concept ##  """)

st.write("""
Staking is when you lock crypto assets for a set period of time to help support the operation of a blockchain. In return for staking your crypto, you earn more cryptocurrency.
Many blockchains use a proof of stake consensus mechanism. Under this system, network participants who want to support the blockchain by validating new transactions and adding new blocks must “stake” set sums of cryptocurrency.
Staking helps ensure that only legitimate data and transactions are added to a blockchain. Participants trying to earn a chance to validate new transactions offer to lock up sums of cryptocurrency in staking as a form of insurance. [[6]](https://www.forbes.com/advisor/in/investing/cryptocurrency/what-is-staking-in-crypto/#:~:text=Staking%20is%20when%20you%20lock,proof%20of%20stake%20consensus%20mechanism.)   """)


st.info(""" ##### In This Stake Section you can find: ####

##### Stake Near #####  
* Each Whale Number and Amount of Stake  
* Top Staked Pool Based on Near Amount

##### Unstake Near #####    
* Each Whale Number and Amount of Unstake  
* Top Untaked Pool Based on Near Amount


""")
###########################################################################################################

st.write(""" ## Stake Near """)

st.write(""" Only 8 out of the top 20 whales did stake in the last 12 Months. Whale "c6d39aa078dbcba02800d1251194d33dbea2122d671435ac1c6ed5ffae383c03" staked 20.6M NEAR and ranked first, following which "6972348ec8e7c100a8f4f08171dde5e38ae0e329308e2fa60a986b6439ca3932" stood second with 8.1M NEAR staked. "figment.poolv1.near" was top-ranked pool based on number and volume with 30.9M NEAR which is 70% of total NEAR staked in the 12-month period.    """)

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


c1, c2 = st.columns(2)

with c1:
    # Number of Stake Transactions Whales have done in last 12 Month
    fig = px.bar(df, x="Pool Name", y="Stake Amount",
                 color="Pool Name", title=' Top Staked Pools Based on Near Amount ')
    fig.update_layout(showlegend=True, xaxis_title=None,
                      yaxis_title="Stake Amount")
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Whales Compare to Other Users Percentage of Transactions
    fig = px.pie(df, values="Stake Amount",
                 names="Pool Name", title=' Top Staked Pools Based on Near Amount ', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


################################################################################################

st.write(""" ## Unstake Near """)
st.write(""" Only 3 out of 20 Unstake NEAR during the last 12 months, "68f5bab7f593e6031632570e61e27165247ef7c971285a441820d52414641937" with almost 1M NEAR, stood first. 96% of these unstaked transactions were from "hashquark.poolv1.near" with 954k NEAR volume.     """)

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

c1, c2 = st.columns(2)

with c1:
    # Number of Stake Transactions Whales have done in last 12 Month
    fig = px.bar(df2, x="Pool Name", y="Stake Amount",
                 color="Pool Name", title=' Top Untaked Pools Based on Near Amount ')
    fig.update_layout(showlegend=True, xaxis_title=None,
                      yaxis_title="Stake Amount")
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Whales Compare to Other Users Percentage of Transactions
    fig = px.pie(df2, values="Stake Amount",
                 names="Pool Name", title=' Top Unstaked Pools Based on Near Amount Percentage ', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


####################################################################################

st.text(" \n")

st.info(""" #### Coclusion: ####

 * only 8 out of 20 Whales staked 
 * one whale staked 20M and ranked first with a 12M difference from the second rank
 * "figment.poolv1.near" is the top-ranked pool staked with 30.9M NEAR
 * Only 1M NEAR unstaked during the last 12 months; almost all of those were from "hashquark.poolv1.near"


""")
