import requests
from send_email import send_email

topic = "tesla"
api_key = "1b029027b0404e2cb6c8e7cb30d8c932"
url = ("https://newsapi.org/v2/top-headlines?"
       "country=us&category=business&apiKey=1b029027b0404e2cb6c8e7cb30d8c932&language=en")

# Make request
request = requests.get(url)

# Make dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] and article["description"] is not None:
        body = ("Subject: Today's news" + "\n"
                + (body + article["title"] + "\n"
                   + article["description"] + "\n"
                   + article["url"] + 2 * "\n"))

body = body.encode("utf-8")
send_email(message=body)
