import requests

query = input("What you wanna know today champ?")
api = "****************************"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-04-20&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n-----------------------\n")

