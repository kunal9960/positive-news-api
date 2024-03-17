import requests
import os
from send_email import send_email

api = os.getenv("API")
url = ("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="
       f"{api}")

# Make request
request = requests.get(url)

# Make dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Daily News!\n\n"
for article in content["articles"][:10]:
    if article["title"] and article["description"] and article["url"] is not None:
        body += article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
