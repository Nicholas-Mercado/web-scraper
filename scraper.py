import requests
from bs4 import BeautifulSoup


print(""" 
        --> Welcome to Citation Station <--
        
        Input a Wikipedia URL and you
        will get back a how many citations
        needed on that page and list of
        those citations 
      
""")
wiki_url = input("> ")
page = requests.get(wiki_url)
    
def get_citations_needed_count():
    count_of_cites=0

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(title = 'Wikipedia:Citation needed')
    
    for cites in results:
        count_of_cites += 1
        
    print(count_of_cites)
    return count_of_cites

get_citations_needed_count()

def get_citations_needed_report():
    pass
