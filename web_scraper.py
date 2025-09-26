import requests
from bs4 import BeautifulSoup


URL = "https://www.bbc.com/news"


response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

headlines = [h.get_text(strip=True) for h in soup.find_all("h3")]

with open("headlines.txt", "w", encoding="utf-8") as f:
    f.write("Top News Headlines\n")
    f.write("="*40 + "\n\n")
    for i, h in enumerate(headlines[:10], 1):  # Limit to top 10
        f.write(f"{i}. {h}\n")

print(" Headlines scraped and saved into 'headlines.txt'")
