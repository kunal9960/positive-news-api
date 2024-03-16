import requests

api_key = "1b029027b0404e2cb6c8e7cb30d8c932"
url = ("https://newsapi.org/v2/everything?q=tesla&from="
       "2024-02-16&sortBy=publishedAt&apiKey="
       "1b029027b0404e2cb6c8e7cb30d8c932")

# Make request
request = requests.get(url)

# Make dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
