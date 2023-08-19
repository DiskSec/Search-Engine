import webbrowser

def search(query):
    search_url = f"https://search.brave.com/search?q={query}"
    webbrowser.open(search_url)

if __name__ == "__main__":
    search_query = input("Enter your search query: ")
    search(search_query)
