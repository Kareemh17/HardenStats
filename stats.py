import requests
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt

PPG = []
names = []
FMG = []
PlusMinus = []
req = requests.get('https://www.foxsports.com/nba/stats?season=2018&category=SCORING&group=1&time=0')
soupt = soup(req.text, 'html.parser')
table = soupt.find('table', {'class': 'wisbb_standardTable'})
tbody = table.find('tbody')

for a in tbody.find_all('a', {'class': 'wisbb_fullPlayer'}):
    span = a.find_all('span')[0]
    names.append(span.text.strip())

print(names)
for tr in tbody.find_all('tr'):
    ppg = tr.find_all('td')[4].text.strip()
    PPG.append(float(ppg))

for tr in tbody.find_all('tr'):
    fmg = tr.find_all('td')[14].text.strip()
    FMG.append(float(fmg))

with plt.style.context('seaborn-bright'):
    plt.scatter(x=PPG[1:],y=FMG[1:],c='grey',label='The top 49 scorers in the NBA')
    plt.scatter(x=PPG[0],y=FMG[0],c='red',label='James Harden')
    for label, x, y in zip(names, PPG, FMG):
        plt.annotate(label, xy=(x, y),fontsize = 8)
    plt.xlabel('Points Per Game')
    plt.ylabel('Free Throws Per Game')
    plt.title('The top 49 NBA Players and James Harden')
    # plt.legend()
    plt.show()
