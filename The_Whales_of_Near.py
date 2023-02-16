# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='The Whales of Near',
                   page_icon=':bar_chart:', layout='wide')
st.title(' The Whales 🐋 of NEAR')


# Content
c1, c2 = st.columns(2)


with c1:
    st.text(" \n")
    st.text(" \n")
    st.video('https://www.youtube.com/watch?v=1cozsZP8yd4&t=30s')

with c2:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/Whale.jpg'))


st.write("""
### What Is NEAR Blockchain ? ###
NEAR Protocol is software that aims to incentivize a network of computers to operate a platform for developers to create and launch decentralized applications.
Central to NEAR Protocol’s design is the concept of sharding, a process that aims to split the network’s infrastructure into several segments in order for computers, also known as nodes, to only have to handle a fraction of the network’s transactions.  
By distributing segments of the blockchain, rather than the complete blockchain across network participants, sharding is expected to create a more efficient way to retrieve network data and scale the platform.  
NEAR operates in a similar manner to other centralized data storage systems like Amazon Web Services (AWS) that serve as the base layer on which applications are built. But rather than being run by a single entity, NEAR is operated and maintained by a distributed network of computers.  
Just as AWS allows developers to deploy code in the cloud without needing to create their own infrastructure, NEAR Protocol facilitates a similar architecture built around a network of computers and its native cryptocurrency, the NEAR token.[[1]](https://www.coindesk.com/learn/what-is-near-protocol-and-how-does-it-work)

### What Is a Crypto Whale?  ###
Crypto whales, much like their animal namesake, are the most prominent players in the crypto market as they hold the most extensive amounts of a specific cryptocurrency. Also, much like large animals, when a crypto whale sneezes, the whole blockchain can catch a cold. Their large wallets can single-handedly change the value of cryptocurrencies with their actions.  
 Cryptocurrency whales, or crypto whales, are individuals or entities that own large quantities of a specific cryptocurrency. Generally speaking, a crypto whale is an entity that holds enough digital currency to significantly influence market prices by trading significant amounts of coins and tokens. Although there isn't a straightforward or defined threshold, most Bitcoin whales own a minimum of 1,000 bitcoins (BTCs).
Because they own such large amounts of cryptocurrency, most crypto whales refrain from trading on traditional crypto markets, as their hefty transactions might overwhelm the liquidity of trading volumes. Instead, they engage in over-the-counter (OTC) crypto trading, where they buy and sell crypto to each other, many times off-chain.
Whales significantly impact blockchains that run on a proof-of-stake (PoS) protocol as larger quantities of staked funds lead to more voting power. For these networks, the existence of whales could be both a positive indicator of the blockchain's stability and growth. However, the bulk of money controlled by whales can negatively impact power and voting allocation.
### Whale Watching  ###
Whale watching refers to tracking a crypto whale’s activity on the market. Identifying a crypto whale enables average users to watch their movement on the market while trying to predict the whale's next action plan. This allows the user to make money while avoiding potential losses.
Crypto whales have influenced some of the largest cryptocurrencies in the world, including BTC. As a result, smaller investors need to keep tabs on the biggest crypto users and stay informed of any significant changes to their crypto wallets to adjust their investment strategy accordingly.[[2]](https://worldcoin.org/articles/what-is-a-crypto-whale)


## Methodology ##  
Where in the ocean of NEAR do the whales hang out? Examine the top 20 addresses by amount of NEAR held - excluding any custodial or exchange addresses that you can. Can you identify any “power players” or wallets of interest? What behaviors do these whales exhibit?  
to answer these questions first we calculate NEAR amount in and out in each wallet using "near.core.fact_receipts" and "near.core.fact_transactions" tabels then ommit the exchange and custodial wallets from this list, after that we monitor this Top 20 Whales activity on chain data to find any particular pattern. Activity on CEX particulary monitored using "near.core.dim_address_labels" and "near.core.fact_transfers", finally the Impact of Whales Activity on NEAR Price considered. In this dashboard all the results gathered from last 12 month activity of this list except Daily zoom in chart which focused on last 3 month.




""")

st.write("""   
#### Sources ####  """)
st.write("""    1.https://www.coindesk.com/learn/what-is-near-protocol-and-how-does-it-work/  
        2.https://worldcoin.org/articles/what-is-a-crypto-whale  
        3.https://www.youtube.com/watch?v=1cozsZP8yd4&t=30s
      
              """)
c1, c2 = st.columns(2)
with c2:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
    st.info(
        '**Project Github:  [The Whales of Near](https://github.com/Kaizen-Step/The_Whales_of_Near)**', icon="🐾")

with c1:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
    st.info(
        '**Twitter:  [Ludwig.1989](https://flipsidecrypto.xyz/)**', icon="🕊️")
