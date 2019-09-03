import pandas as pd
from selenium import webdriver

from bs4 import BeautifulSoup




filepath = 'D:/HK B/All_estate_info_update.csv'
outputpath='D:/HK B/All_estate_info_with_blockname.csv'
df = pd.read_csv(filepath)
df['BLOCKS_LIST']=None
df['NUM_ONLINE']=None
df['CHECK_NUM']=None
browser=webdriver.Chrome()
browser.minimize_window()
#for i in range(0,1):
for i in range(0,len(df),1):
    # collect necessary info
    BlocksList=[]
    estate = df.at[i, 'Estate_name']
    url=df.at[i,'URL_NEW']
    table_record_num=df.at[i,'No__of_Blocks']
    # grab block name
    try:
        browser.get(url)
        content=browser.page_source
        soup=BeautifulSoup(content,'html.parser')
        a_tags=soup.find_all('div',{"class":"estate_locator_detail_column_2 blocks_name"})
        tag=a_tags[0]
        items=tag.find_all('div',{"class":"item__text"})
        for item in items:
            item_s=str(item)
            first_split=item_s.split('>')
            second_split=first_split[1].split('<')
            blockname=second_split[0]
            BlocksList.append(blockname)
        #print(soup.prettify())
        df.at[i,'BLOCKS_LIST']=BlocksList
        online_num=len(BlocksList)
        df.at[i,'NUM_ONLINE']=online_num
        if table_record_num-online_num==0:
            df.at[i,'CHECK_NUM']='fine'
        else:
            df.at[i, 'CHECK_NUM'] = 'CAUTION!'
        # to make sure the progress work
        browser.implicitly_wait(5)
        print(estate ,' works')
    except:
        df.at[i, 'BLOCKS_LIST']=None
        print(estate, ' error' )

browser.quit()

df.to_csv(outputpath,index=None)