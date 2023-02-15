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
                   page_icon=':bar_chart:', layout='wide')
st.title('🚀Cex Exchange')

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


st.write(""" ## Transfer From Cex """)

# Transfer from cex Number of Transaction
fig = px.bar(df5, x="WHALE_WALLET", y="number of transactions",
             color="WHALE_WALLET", title='Transfer from cex Number of Transaction')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Transfer from cex Volume [Near]
fig = px.bar(df5, x="WHALE_WALLET", y="AMOUNT",
             color="WHALE_WALLET", title='Transfer from cex Volume [Near]')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ## Transfer To Cex """)


# Transfer to cex Number of Transaction
fig = px.bar(df6, x="WHALE_WALLET", y="number of transactions",
             color="WHALE_WALLET", title='Transfer To cex Number of Transaction')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Transfer To cex Volume [Near]
fig = px.bar(df6, x="WHALE_WALLET", y="AMOUNT",
             color="WHALE_WALLET", title='Transfer To cex Volume [Near]')
fig.update_layout(showlegend=True, xaxis_title=None,
                  yaxis_title='Volume')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ## Weekly Cex """)


st.write(""" ### Weekly From Cex """)


# Weekly Transfer from CEX
fig = px.bar(df.sort_values(["DATE", "number of transactions"], ascending=[
    True, False]), x="DATE", y="number of transactions", color="CEX_NAME", title='Weekly Transfer From CEX Number of Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Weekly Transfer from cex volume
fig = px.bar(df.sort_values(["DATE", "AMOUNT"], ascending=[
    True, False]), x="DATE", y="AMOUNT", color="CEX_NAME", title='Weekly Transfer From Cex Volume [Near]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ### Weekly to Cex """)

# Weekly Transfer to CEX
fig = px.bar(df2.sort_values(["DATE", "number of transactions"], ascending=[
    True, False]), x="DATE", y="number of transactions", color="CEX_NAME", title='Weekly Transfer TO CEX Number of Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Weekly Transfer to cex volume
fig = px.bar(df2.sort_values(["DATE", "AMOUNT"], ascending=[
    True, False]), x="DATE", y="AMOUNT", color="CEX_NAME", title='Weekly Transfer To Cex Volume [Near]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ## Daily Cex """)

st.write(""" ### Daily From Cex """)

# Daily Transfer from CEX
fig = px.bar(df3.sort_values(["DATE", "number of transactions"], ascending=[
    True, False]), x="DATE", y="number of transactions", color="CEX_NAME", title='Daily Transfer From CEX Number of Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily Transfer from cex volume
fig = px.bar(df3.sort_values(["DATE", "AMOUNT"], ascending=[
    True, False]), x="DATE", y="AMOUNT", color="CEX_NAME", title='Daily Transfer From Cex Volume [Near]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ### Daily to Cex """)

# Daily Transfer to CEX
fig = px.bar(df4.sort_values(["DATE", "number of transactions"], ascending=[
    True, False]), x="DATE", y="number of transactions", color="CEX_NAME", title='Daily Transfer TO CEX Number of Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily Transfer to cex volume
fig = px.bar(df4.sort_values(["DATE", "AMOUNT"], ascending=[
    True, False]), x="DATE", y="AMOUNT", color="CEX_NAME", title='Daily Transfer To Cex Volume [Near]')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
