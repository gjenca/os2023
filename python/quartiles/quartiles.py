import requests
from bs4 import BeautifulSoup as BS
import time
import difflib

def search_scimago(journal_name):

    query_name='+'.join(journal_name.strip().split())
    ret={}
    end_search=False
    for pagenum in range(1,6):
        params={'q':query_name,'page':pagenum}
        resp=requests.get('https://www.scimagojr.com/journalsearch.php',params)
        soup=BS(resp.text,'html.parser')
        for search_result in soup.find('div',class_='search_results').find_all('a'):
            path_to_journal=search_result['href']
            journal_url=f'https://www.scimago.com/{path_to_journal}'
            title=search_result.span.text.strip()
            if title in ret:
                end_search=True
                break
            ret[title]=journal_url
        if end_search:
            break
        time.sleep(0.1)
    return ret

def find_best(what,where):

    ret_best=None
    maximum=0
    for s in where:
        this_ratio=difflib.SequenceMatcher(None,what,s).ratio()
        if this_ratio>maximum:
            ret_best=s
            maximum=this_ratio
    return ret_best

def find_best2(what,where):

    return max(where,key = lambda s: difflib.SequenceMatcher(None,what,s).ratio())


results=search_scimago('order')
best=find_best2('order',results)
print(best,results[best])






