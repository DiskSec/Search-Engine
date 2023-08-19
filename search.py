import requests
from bs4 import BeautifulSoup

def search(query):
    search_url = f"https://search.brave.com/search?q={query}"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        results = soup.find_all("h3", class_="result-title")
        
        for index, result in enumerate(results, start=1):
            title = result.get_text()
            print(f"{index}. {title}")
    else:
        print("Error fetching search results.")

if __name__ == "__main__":
    search_query = input("Enter your search query: ")
    search(search_query)
