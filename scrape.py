import requests
from bs4 import BeautifulSoup
import csv

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = []
for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    quotes.append([text, author])

with open("quotes.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    writer.writerows(quotes)

print("Quotes scraped and saved to quotes.csv")
