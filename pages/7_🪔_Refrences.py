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
st.set_page_config(page_title='Aknowledgement - Terra Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🪔 Refrences')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Aknowledgement
st.write(""" ##     Aknowledgement 
We are grateful to all who helped us develop this project specially ****Mr. Ali Taslimi**** (twitter: @AliTslm ) with comprehensive streamlit open source project(https://github.com/alitslm/cross_chain_monitoring) that provides streamlit functions and tools.
And also ****Flipside Crypto**** with massive database and last but not least ****MetricsDao**** that is the reason behind this project.
""")

# SQL Codes
st.write(""" ## SQL Codes ## """)

st.write("""
At the following links, you can find the SQL codes that are used in this dashboard: 

""")


st.write("""
1. [Daily Transaction Fee Based on Users](https://flipsidecrypto.xyz/edit/queries/efb927d0-41bd-4762-a2f2-b463b8cfb01e/visualizations/02c54c89-d55f-4611-8cc6-bcfe7e6d386a)
2. [Daily Transaction Success and Fails](https://flipsidecrypto.xyz/edit/queries/a21367b3-6df5-447c-996e-919d2f89b6e7/visualizations/d8836273-aed8-42db-9805-a9e0ec90f271)
3. [Top 10 Transaction Type](https://flipsidecrypto.xyz/edit/queries/e54eaa63-ab14-4313-af7a-fdff2d8abecc/visualizations/221f849d-3463-4e65-9431-1b2b86224322)
4. [Top 10 Platforms](https://flipsidecrypto.xyz/edit/queries/934aaafb-dde1-41b4-ad66-eb7a15f30e5c/visualizations/ade73bfa-1eee-4a64-8ae5-46c21de94da4)
5. [Total Transaction Comparison](https://flipsidecrypto.xyz/edit/queries/fb5217ce-4ab7-44ce-83e5-8aa7b9a79e96/visualizations/c0f44e09-b01b-4f3d-890e-76777479faa1)
6. [Daily Transaction Fee Based on Action Type](https://flipsidecrypto.xyz/edit/queries/7232fce4-57e1-41e9-a356-2a3b857e4687/visualizations/9d09c7b4-b6c8-445b-8ff7-668ccae7bc7a)
7. [Daily TX Type](https://flipsidecrypto.xyz/edit/queries/7232fce4-57e1-41e9-a356-2a3b857e4687/visualizations/9d09c7b4-b6c8-445b-8ff7-668ccae7bc7a)
8. [Transaction Type in each wallet](https://flipsidecrypto.xyz/edit/queries/a89edfff-1085-4954-a859-6f2abd0b639f/visualizations/79de6764-7c8f-4d00-86ed-d9fe4b159a8f)
9. [Daily TX_FEE Type_Platform](https://flipsidecrypto.xyz/edit/queries/8a5efd9a-2075-4d42-b4ae-01240827c9e1/visualizations/184637fc-6c70-44eb-bf24-bcbde37334c9)
10. https://app.flipsidecrypto.com/velocity/queries/9dbae3b1-ab95-47e9-89bc-d26c6a01d9f8
11. https://app.flipsidecrypto.com/velocity/queries/195bf8df-3418-4365-8302-d0c61deb1216
12. https://app.flipsidecrypto.com/velocity/queries/328f1bda-dbbe-49ae-85a2-053c01333c7f
13. https://app.flipsidecrypto.com/velocity/queries/5f75bdd1-5010-427d-94a9-caed33fb610c
14. https://app.flipsidecrypto.com/velocity/queries/09c7e9ab-7aaa-4f58-869d-d0d34a078218
15. https://app.flipsidecrypto.com/velocity/queries/72c12f5a-72b2-4039-adc0-b43f52a80494
16. https://app.flipsidecrypto.com/velocity/queries/69325192-0e7b-4547-ab47-781c9552db37
17. https://app.flipsidecrypto.com/velocity/queries/6f303a26-78fe-4db1-b2a1-8a8149081293


""")
