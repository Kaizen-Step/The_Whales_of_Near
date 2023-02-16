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
st.set_page_config(page_title='Supply - Nera Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🐳Near Whales')


# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'NEAR_top20_whales':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/53e0d38b-0c1c-4022-8c86-bc158cbdee2d/data/latest')
    elif query == 'NEAR_top20_whales_EXcluded':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e352c3a7-bd07-45c0-8ef9-4aa30ffe51b3/data/latest')
    return None


NEAR_top20_whales = get_data('NEAR_top20_whales')
NEAR_top20_whales_EXcluded = get_data('NEAR_top20_whales_EXcluded')
NEAR_supply_richest = get_data('NEAR_supply_richest')
NEAR_Balance_Range = get_data('NEAR_Balance_Range')
TopPools_Volume = get_data('TopPools_Volume')
TopPools_Users = get_data('TopPools_Users')
TopPools_Transactions = get_data('TopPools_Transactions')
top10_Deligatorsvolume = get_data('top10_Deligatorsvolume')
top10_DeligatorsTX = get_data('top10_DeligatorsTX')


df = NEAR_top20_whales
df2 = NEAR_top20_whales_EXcluded

##################################################################################################################


st.write(""" ## Near Whales Extraction """)

st.write(""" to extract top 20 Near Whales we try to calculate the amount of Near deposit in each wallet and subtract the amount withdraw out to find wallets with the most Near token. To do this we use "near.core.fact_receipts" and "near.core.fact_transactions" and substract the amount in with amount out. In following list you can find the top 20 which include custodial and exchange wallets also.     """)

st.table(df)

st.write(""" ## Final List """)

st.write(""" We did our best to seprate the actual Whales from custodial and exchange wallets. Following is the list of wallets that we detect as exchange or custodial and Final list of top 20 Whale after excluding exchange and custodial wallets for rest of this dashboard we focused on this top 20 Whales activity and impact they made on the market.""")

c1, c2 = st.columns(2)

with c1:
    st.text(" \n")
    st.write("""
    **Wallets ommited from the Top 20 Whales list:**  
    * binancecold3.near    
    * f6bd6ba459446b7b6fca71707779de9473af56f8.lockup.near    
    * nfendowment03.near    
    * proximity-prime.near  
    * nfendowment01.near    
    * nfendowment05.near  
    * linear-protocol.near
    * v2-nearx.stader-labs.near  
    * e-near.near  
    * binance1.near  
    * d391f37d5a889a724170f44b2b1eff818c7e20bd.lockup.near  
    * marketplace.paras.near  
    * bitkubhwallet.near  
    * app.nearcrowd.near  
    * kucoinc.near  
    * token.sweat  
    * bitkubhwallet2.near  
    * multisender.app.near  
    * 0a2fb468f797b1049841328d4dadc868ca1dcab9.lockup.near  
    * nearcoldtree.near  
    * ec838c99348c4b5a8859a3ca9f44eb136bfa9a01.lockup.near  

            """)

with c2:
    st.table(df2)
