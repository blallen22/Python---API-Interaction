# import the requisite packages
import bs4 as BeautifulSoup 
from bs4 import SoupStrainer
import re
import urllib.request 
import pandas as pd
import requests

# identify 50 NYSE ticker symbols that we're interested in
symbols = ['ADS','ADP','DM.V','SRVR','ATDS','TECD','TDS','BLOK','DTMXF','DAVA',
           'DAIO','DLTA','TDJ','GDAT','HDSLF','NTDTY','DTRK','DAL.MI','DTSS',
           'TDE','TDA','TDI','DATI','CDTAF','MJDS','DTST','DCM.TO','GNRD','DAAT',
           'D6H.DE','NB2.DE','BCY.SI','9613.T','3902.T','NB2.F','DCLT','600198.SS',
           'SWISF','DTL.AX','FN1000.FGI','0HCR.L','GATA','5403.TWO','TRAC','DGPIF',
           '20Y.BE','ARD.V','DGATE.IS','DAC.V','DTC.JO',
]

# specify the agent
headers = {'User-agent': 'Mozilla/5.0'}
mySymbols = {}

# loop through the ticker symbols
for s in symbols:
    vals = {}
    # get the profile from the website
    # the url for the stock appears on this page
    url = ("https://finance.yahoo.com/quote/{}/profile?p={}".format(s,s))
    webpage = requests.get(url, headers=headers)
    soup = BeautifulSoup.BeautifulSoup(webpage.content) 

    # the title has the company name but also has additional information in the format of 
    # (SSS) profile and .... 
    # where SSS is the symbol. We remove this extra title to get the company name
    title = soup.find("title")
    tmp = title.get_text()
    rxTitle = re.compile(r'\(.*$')
    coName = rxTitle.sub("", tmp)
    
    # loop through all the links
    # The company web site is the the one that doesn't have Yahoo in the reference,
    # and has a blank title
    for link in soup.find_all('a', href=True):
        try:
            if link['target'] and "" == link['title']:
                m = re.search('yahoo', link['href'], flags=re.IGNORECASE)
                if None == m:
                    
                    url = link['href']
                    webpage = requests.get(url, headers=headers)
                    soup = BeautifulSoup.BeautifulSoup(webpage.content) 
                    
                    vals = {"company":coName, "url":link['href']} 
                    print (s, vals)
                    mySymbols[s] = vals
        except:
            pass
        
        
        
# put the scraped data into a pandas dataframe
df = pd.DataFrame.from_dict(mySymbols, orient = 'index')
df
