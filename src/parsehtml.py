from bs4 import BeautifulSoup

with open('../data/raw/kathimerini/polemos-stin-oukrania.txt') as file:
    soup = BeautifulSoup(file, "html.parser")
    sample = soup.find_all('article')
    print(len(sample))
