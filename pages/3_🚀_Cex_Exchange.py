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
st.set_page_config(page_title='Cex Exchange - The Whales of Near',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🚀CEX Exchange')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Transfer_from_CEXWeekly':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/389c01aa-bdd4-4f1c-b623-4237cc5e731c/data/latest')
    elif query == 'Transfer_To_CEXWeekly':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/1cce9de6-602c-4fc3-aafb-1ad288d80af5/data/latest')
    elif query == 'Transfer_from_CEX_Daily':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/fc17e948-2ddf-4169-a6fe-07cffda76777/data/latest')
    elif query == 'NTransfer_To_CEX_Daily':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/edd737e4-1b0a-404e-842b-3a78d8a87ab6/data/latest')
    elif query == 'Transfer_from_CEX':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/0c772bd7-5e93-48da-adb8-a2a8e3188fad/data/latest')
    elif query == 'Transfer_To_CEX':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/a815a314-6f66-4377-9376-c121cdefc77b/data/latest')
    return None


Transfer_from_CEXWeekly = get_data('Transfer_from_CEXWeekly')
Transfer_To_CEXWeekly = get_data('Transfer_To_CEXWeekly')
Transfer_from_CEX_Daily = get_data('Transfer_from_CEX_Daily')
NTransfer_To_CEX_Daily = get_data('NTransfer_To_CEX_Daily')
Transfer_from_CEX = get_data('Transfer_from_CEX')
Transfer_To_CEX = get_data('Transfer_To_CEX')


df = Transfer_from_CEXWeekly
df2 = Transfer_To_CEXWeekly
df3 = Transfer_from_CEX_Daily
df4 = NTransfer_To_CEX_Daily
df5 = Transfer_from_CEX
df6 = Transfer_To_CEX


#########################################################################################

st.write(""" ### CEX Exchange Concept ##  """)

st.write("""
A centralized exchange (CEX) offers cryptocurrency exchange services to registered users. Its primary service typically matches buyers and sellers with an order book,through a centralized platform. To better understanding of Cex, on the other hand, DEX is a decentralized exchange (DEX) uses on-chain smart contracts to run its exchange services. In most cases, users swap tokens from liquidity pools, with liquidity provided by other users in exchange for swap fees. [[5]](https://academy.binance.com/en/articles/what-s-the-difference-between-a-cex-and-a-dex)   """)


st.info(""" ##### In This CEX Exchange Section you can find: ####

##### Transfer from CEX #####  
* Each Whale Number of Transactions and Volume From CEX 
* Weekly Transactions and Volume From CEX Prespective View (Last 12 Month)
* Daily Transactions and Volume From CEX zoom in (Last 3 Month)
##### Transfer To CEX #####    
* Each Whale Number of Transactions and Volume To CEX
* Weekly Transactions and Volume To CEX from Prespective View (Last 12 Month)
* Daily Transactions and Volume To Cex zoom in (Last 3 Month)


""")


#########################################################################################
st.text(" \n")
st.write(""" ## Transfer From Cex """)
st.write(""" Among the top 20 Whales list, "d73888a2619c7761735f23c798536145dfa87f9306b5f21275eb4b1a7ba971b9" had the most number of transactions from CEX exchanges to NEAR  with 61,910 Number of transaction with more than 83.5M NEAR total Volume. In the following, you can see these were only one way due to its transfer of only 6852 transactions (10M NEAR token) to CEX exchanges. This whlae ranked third in number of total transactions """)


# Transfer from cex Volume [Near]
fig = px.bar(df5, x="WHALE_WALLET", y="AMOUNT",
             color="WHALE_WALLET", title='Transfer from cex Volume [Near]')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Volume [Near]')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)

with c1:
    fig = px.pie(df5, values="number of transactions",
                 names="WHALE_WALLET", title='Share of each Whale From Cex Number of Transactions [Percentage]', hole=0.4)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with c2:
    fig = px.pie(df5, values="AMOUNT",
                 names="WHALE_WALLET", title='Share of each Whale From CEX Volume [Percentage]', hole=0.4)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#################################################################################
st.write(""" #### Weekly Transaction Prespective View """)

st.write(""" From a perspective view,  "Okex" had the most number and Volume of transactions in most of the 12-month period, while whales on Binance transferred 10M NEAR in only 6 transactions on may 16,2022 week. This substantial volume transactions repeated on November 2022 and January 2023 only on Binance.  

 """)

# Weekly Transfer from CEX
fig = px.bar(df.sort_values(["DATE", "number of transactions"], ascending=[
    True, False]), x="DATE", y="number of transactions", color="CEX_NAME", title='Weekly Transfer From CEX Number of Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Weekly Transfer from cex volume
fig = px.bar(df.sort_values(["DATE", "AMOUNT"], ascending=[
    True, False]), x="DATE", y="AMOUNT", color="CEX_NAME", title='Weekly Transfer From CEX Volume [Near]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(""" #### Daily Transaction Zoom in """)

st.write(""" Focused on the last three months, you can see the few "Binance" transactions with a significant volume on November 28, 2022, and December 14, 2022, and continued up until now, which on February 9, 2023, with only two transactions whales transfer 2M NEAR from "Binance" Exchange.  """)

# Daily Transfer from CEX
fig = px.bar(df3.sort_values(["DATE", "number of transactions"], ascending=[
    True, False]), x="DATE", y="number of transactions", color="CEX_NAME", title='Daily Transfer From CEX Number of Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily Transfer from cex volume
fig = px.bar(df3.sort_values(["DATE", "AMOUNT"], ascending=[
    True, False]), x="DATE", y="AMOUNT", color="CEX_NAME", title='Daily Transfer From CEX Volume [Near]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

################################################################################################################
st.text(" \n")
st.write(""" ## Transfer To Cex """)

st.write(""" As previously mentioned in transaction Section, "5c33c6218d47e00ef229f60da78d0897e1ee9665312550b8afd5f9c7bc6957d2" had the most number of transactions among whales now we could see most of these transactions were transferring to CEX exchanges from Near token with 27,036 Number of transaction with more than 94.6M NEAR total Volume. As you see above, these were mostly one-way due to its transfer of 2112 transactions (31M NEAR tokens) from CEX exchanges. """)


# Transfer To cex Volume [Near]
fig = px.bar(df6, x="WHALE_WALLET", y="AMOUNT",
             color="WHALE_WALLET", title='Transfer To CEX Volume [Near]')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)

with c1:
    fig = px.pie(df6, values="number of transactions",
                 names="WHALE_WALLET", title='Share of each Whale To Cex Number of Transactions [Percentage]', hole=0.4)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with c2:
    fig = px.pie(df6, values="AMOUNT",
                 names="WHALE_WALLET", title='Share of each Whale To CEX Volume [Percentage]', hole=0.4)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" #### Weekly Transaction Prespective View """)


# Weekly Transfer to CEX
fig = px.bar(df2.sort_values(["DATE", "number of transactions"], ascending=[
    True, False]), x="DATE", y="number of transactions", color="CEX_NAME", title='Weekly Transfer TO CEX Number of Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Weekly Transfer to cex volume
fig = px.bar(df2.sort_values(["DATE", "AMOUNT"], ascending=[
    True, False]), x="DATE", y="AMOUNT", color="CEX_NAME", title='Weekly Transfer To CEX Volume [Near]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" #### Daily Transaction Zoom in """)


# Daily Transfer to CEX
fig = px.bar(df4.sort_values(["DATE", "number of transactions"], ascending=[
    True, False]), x="DATE", y="number of transactions", color="CEX_NAME", title='Daily Transfer TO CEX Number of Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily Transfer to cex volume
fig = px.bar(df4.sort_values(["DATE", "AMOUNT"], ascending=[
    True, False]), x="DATE", y="AMOUNT", color="CEX_NAME", title='Daily Transfer To CEX Volume [Near]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

##########################################################################################################

st.text(" \n")

st.info(""" #### Coclusion: ####

 * One whale transfer 83.5M Near from CEX exchanges to NEAR in the last 12 Month which are mostly one way (10M NEAR to CEX exchange)
 * "Okex" had the most number of transactions in the most of the period, while "Binance" transactions are low in number and huge in volume  
 * 14M NEAR transferred from Binance on December 14, 2022, in only one day also, 2M NEAR transferred from Binance with only two transactions
 * whale with the most number of transactions transferred 94M NEAR to CEX exchanges and only transferred 31M back to it


""")
