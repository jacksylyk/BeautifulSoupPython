import requests
from bs4 import BeautifulSoup


class Scrapper:
    def init(self):
        pass

    def get(self, curr):
        page = requests.get(
            "https://google.com/search?q=site%3Acoingecko.com+" + curr + "&ie=utf-8&oe=utf-8")
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find_all("h3")
        return result


sc = Scrapper()
all = sc.get("ethereum")

for i in all:
    print(i.find("div").get_text())