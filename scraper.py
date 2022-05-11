import requests
from bs4 import BeautifulSoup

def get_citations_needed_count():
    count_of_cites=0
    
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(title = 'Wikipedia:Citation needed')
    
    for cites in results:
        count_of_cites += 1
        
    print(count_of_cites)
    return count_of_cites

get_citations_needed_count()

def get_citations_needed_report():
    pass
