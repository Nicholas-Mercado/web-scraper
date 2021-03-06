import requests
from bs4 import BeautifulSoup


print(""" 
        --> Welcome to Citation Station <--
        
        Input a Wikipedia URL and you
        will get back how many citations
        that page is missing and list of
        those citations 
      
""")
wiki_url = input("> ")
# wiki_url = "https://en.wikipedia.org/wiki/History_of_Mexico"  <---test
page = requests.get(wiki_url)
    
def get_citations_needed_count():
    count_of_cites=0

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(title = 'Wikipedia:Citation needed')
    
    for cites in results:
        count_of_cites += 1
        
    print(f"The url you entered : {wiki_url}")
    print(f"Has {count_of_cites} citations needed! ")
    return



def get_citations_needed_report():
    
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(title = 'Wikipedia:Citation needed')
    for p in results:
        just_text = p.parent.parent.parent
        print(just_text.get_text())

get_citations_needed_count()
get_citations_needed_report()
