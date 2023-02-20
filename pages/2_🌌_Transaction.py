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
st.set_page_config(page_title='Transactions - The Whales of Near',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🌌Transactions')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'TransactionType_each_Wallet':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a89edfff-1085-4954-a859-6f2abd0b639f/data/latest')
    elif query == 'Daily_TX_Type':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/999b8676-c867-4638-8a0b-6833dbef705c/data/latest')
    elif query == 'Daily_TX_FEE_Type':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7232fce4-57e1-41e9-a356-2a3b857e4687/data/latest')
    elif query == 'Total_Transaction_Comparison':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fb5217ce-4ab7-44ce-83e5-8aa7b9a79e96/data/latest')
    elif query == 'Top10_Platforms':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/934aaafb-dde1-41b4-ad66-eb7a15f30e5c/data/latest')
    elif query == 'Top10_TransactionType':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e54eaa63-ab14-4313-af7a-fdff2d8abecc/data/latest')
    elif query == 'TX_SUCC_Fail':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/a21367b3-6df5-447c-996e-919d2f89b6e7/data/latest')
    elif query == 'D_TX_type':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/645f8b4c-f300-49a5-b37a-dc3a5ab7da59/data/latest')
    elif query == 'D_Fee_Type':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/4b0ac171-828a-4afa-ae66-0758801aa3d4/data/latest')
    return None


TransactionType_each_Wallet = get_data('TransactionType_each_Wallet')
Daily_TX_Type = get_data('Daily_TX_Type')
Daily_TX_FEE_Type = get_data('Daily_TX_FEE_Type')
Total_Transaction_Comparison = get_data('Total_Transaction_Comparison')
Top10_Platforms = get_data('Top10_Platforms')
Top10_TransactionType = get_data('Top10_TransactionType')
TX_SUCC_Fail = get_data('TX_SUCC_Fail')
D_TX_type = get_data('D_TX_type')
D_Fee_Type = get_data('D_Fee_Type')


df = TransactionType_each_Wallet
df2 = Daily_TX_Type
df3 = Daily_TX_FEE_Type
df4 = Total_Transaction_Comparison
df5 = Top10_Platforms
df6 = Top10_TransactionType
df6 = TX_SUCC_Fail
df7 = D_TX_type
df8 = D_Fee_Type
######################################################################################################################


st.write(""" ### Transaction Concept ##  """)

st.write("""
A Simply put, cryptocurrency transaction is a transfer of information made between blockchain addresses. These transfers have to be signed with a private key that corresponds to its address. Signed transactions are broadcast to the network of nodes, active computers that follow a specific set of rules to validate transactions and blocks. Valid transactions need to be confirmed by being included in blocks through the process of mining.[[4]](https://www.bitstamp.net/learn/crypto-101/how-do-cryptocurrency-transactions-work/)   """)


st.info(""" ##### In This Transaction Section you can find: ####

 * Whales Different Type of Transactions Activity 
 * Whales Transactions Compare to other Users  
 * Whales Weekly Transaction Prespective view (Last 12 Month)
 * Whales Daily Transaction Zoom in (Last 3 Month)



""")


#####################################################################################
st.text(" \n")
st.text(" \n")
st.write(""" ## Whales Transaction Activity """)

st.write(""" 95.1% percent of whale transactions were transferring, while Staking was ranked second-to-last before deleted accounts. What is really shocking here is that there was no NFT trading or mint transaction during the 12-month period (Checked with another query), and the number of swap transactions was relatively low. While four of the top twenty whales had no transaction during the last 12 months, "5c33c6218d47e00ef229f60da78d0897e1ee9665312550b8afd5f9c7bc6957d2" ranked first with 147,334 transactions which all of them is transferring. The user seems to be a bot due to its more than ten transactions per minute performance.  "d73888a2619c7761735f23c798536145dfa87f9306b5f21275eb4b1a7ba971b9" Ranked third with 20,284 number of transactions we discuss these two whales more in CEX exchange section. "token.sweat" stood first among platforms with a significant difference from others (with 20,834 whale usage in one year). """)

# Transaction Type In Each Wallet
fig = px.bar(df.sort_values(["TRADER", "Number of Action Type"], ascending=[
    True, False]), x="TRADER", y="Number of Action Type", color="Action Type", title='Whales Type of Transactions [Log Scale]', log_y=True)
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Whales Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)

with c1:
    fig = px.pie(df6, values="Number of Action Type",
                 names="Action Type", title='Share of each Transaction Type Used by Whales [Percentage]', hole=0.4)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Top Transaction Type Used Whales [Log Value]
    fig = px.bar(df6, x="Action Type", y="Number of Action Type",
                 color="Action Type", title='Top Transaction Type Used by Whales [Log Scale]', log_y=True)
    fig.update_layout(showlegend=True, xaxis_title=None,
                      yaxis_title='Number of Transaction')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Top 10 Platforms Whales Used
fig = px.bar(df5, x="PLATFORM", y="Platforms usage",
             color="PLATFORM", title='Top 10 Platforms Whales Used in Number of Transactions')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Platform Usage')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
########################################################################################################################

st.text(" \n")
st.text(" \n")
st.write(""" ## Whale Compare to Other Users  """)

st.write(""" Although the share of the top 20 whales in the number of total transactions was less than 1 percent, the average transaction per user among whales was 473.125 during 12 months, which was more than 13 times as high as this average among other users. In contrast, the average transaction fees paid by whales were lower than by regular users (0.0603 and 0.06564 Near, respectively). """)


c1, c2, c3 = st.columns(3)
with c1:

    # Whales Compare to Other Users Total Transactions
    fig = px.bar(df4, x="STATUS", y="Number of Transactions",
                 color="STATUS", title='Whales Compare to Other Users Total Transactions [Log Scale]', log_y=True)
    fig.update_layout(showlegend=True, xaxis_title=None,
                      yaxis_title='Number of Transactions')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # Whales Compare to Other Users Percentage of Transactions
    fig = px.pie(df4, values="Number of Transactions",
                 names="STATUS", title='Whales Compare to Other Users Percentage of Transactions', hole=0.4)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c3:
    # Whales Compare to Other Users Average Transactions per User
    fig = px.bar(df4, x="STATUS", y="Average Transaction Per User",
                 color="STATUS", title='Whales Compare to Other Users Average Transactions per User [Log Scale]', log_y=True)
    fig.update_layout(showlegend=True, xaxis_title=None,
                      yaxis_title='Average Number of Transactions')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2, c3 = st.columns(3)
with c1:

    # Whales Compare to Other Users Total Transactions Fees
    fig = px.bar(df4, x="STATUS", y="TOTAL_TX_FEE",
                 color="STATUS", title='Whales Compare to Other Users Total Transactions Fees [Near-Log Scale]', log_y=True)
    fig.update_layout(showlegend=True, xaxis_title=None,
                      yaxis_title='Total Transaction Fees')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    # Whales Compare to Other Users Percentage of Transactions Fees
    fig = px.pie(df4, values="TOTAL_TX_FEE",
                 names="STATUS", title='Whales Compare to Other Users Percentage of Transactions Fees', hole=0.4)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c3:
    # Whales Compare to Other Users Average Transaction Fees paid per Users
    fig = px.bar(df4, x="STATUS", y="Average Transaction Fee Per Users",
                 color="STATUS", title='Whales Compare to Other Users Average Transaction Fees paid per Users [Near-Log Scale ]', log_y=True)
    fig.update_layout(showlegend=True, xaxis_title=None,
                      yaxis_title='Average Transaction Fees')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##################################################################################################################
st.text(" \n")
st.text(" \n")
st.write(""" ## Whale Weekly Transaction and Transaction Fees  """)


st.write(""" While the first six months of 2022 experienced fluctuation of around 2k transactions per week, the second half showed a significant rise and stood at 8000 transactions in a week. The first week of November 2022 had the highest transaction, with more than 14K. As previously mentioned, most of these 
 transactions were transferring, but the share of function-call rose significantly in the second half of 2022.   """)

#  Weekly Transactions Classified By Users
fig = px.bar(df2.sort_values(["DATE", "Number of Action Type"], ascending=[
    True, False]), x="DATE", y="Number of Action Type", color="TRADER", title='Weekly Whales Transactions Classified By Users')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Weekly Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Weekly Transactions Classified By Transaction Type
fig = px.bar(df2.sort_values(["DATE", "Number of Action Type"], ascending=[
    True, False]), x="DATE", y="Number of Action Type", color="Action Type", title='Weekly Whales Transactions Classified By Transaction Type')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Weekly Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#  Weekly Transactions Success and Fails
fig = px.bar(df6.sort_values(["DATE", "Number of Action Type"], ascending=[
    True, False]), x="DATE", y="Number of Action Type", color="TX_STATUS", title='Weekly Whales Transactions Success and Fails')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Weekly Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#############################################################################################################


# Weekly Transaction Fee Classified by Transaction Type
fig = px.bar(df3.sort_values(["DATE", "Weekly Transaction Fee"], ascending=[
    True, False]), x="DATE", y="Weekly Transaction Fee", color="Action Type", title='Weekly Transaction Fee Classified by Transaction Type')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Weekly Transaction Fees')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Transaction Fee Classified by Users
fig = px.bar(df3.sort_values(["DATE", "Weekly Transaction Fee"], ascending=[
    True, False]), x="DATE", y="Weekly Transaction Fee", color="TRADER", title='Weekly Transaction Fee Classified by Users')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Weekly Transaction Fees')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##########################################################################################################
st.text(" \n")
st.text(" \n")
st.write(""" ## Whale Daily Transaction and Transaction Fees  """)

st.write(""" Whale's daily transactions remained relatively unchanged in the last three months until Feb 14, 2023, which became more than three times as high as its average. While most of these transactions were committed by one user(2800 out of a total of 3300), half of these transactions were transferring, and almost half of it was function-call. It is interesting to know what happened on that day ?!.  """)


#  Daily Transactions Classified By Users
fig = px.bar(df7.sort_values(["DATE", "Number of Action Type"], ascending=[
    True, False]), x="DATE", y="Number of Action Type", color="TRADER", title='Daily Whales Transactions Classified By Users')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily Transactions Classified By Transaction Type
fig = px.bar(df7.sort_values(["DATE", "Number of Action Type"], ascending=[
    True, False]), x="DATE", y="Number of Action Type", color="Action Type", title='Daily Whales Transactions Classified By Transaction Type')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily Transaction Fee Classified by Transaction Type
fig = px.bar(df8.sort_values(["DATE", "Daily Transaction Fee"], ascending=[
    True, False]), x="DATE", y="Daily Transaction Fee", color="Action Type", title='Daily Transaction Fee Classified by Transaction Type')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Transaction Fees')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Transaction Fee Classified by Users
fig = px.bar(df8.sort_values(["DATE", "Daily Transaction Fee"], ascending=[
    True, False]), x="DATE", y="Daily Transaction Fee", color="TRADER", title='Daily Transaction Fee Classified by Users')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Transaction Fees')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


############################################################################################
st.text(" \n")

st.info(""" #### Coclusion: ####

 * 95 percent of whale transactions were transferring- No NFT traded- relatively low stake and swaps
 * Although whales accounted for less than 1 percent of Total transactions, they had average transaction figures 12 times higher than regular users  
 * Number of Whales Transactions rose significantly in the second half of 2022
 * on 14 Feb 2022, the number of transactions rose more than three times its average



""")
