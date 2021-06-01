import requests as scp
from bs4 import BeautifulSoup
i = 0
page = 1
print("Enter appID of the game you want to search mods for:")
appid = input()
if appid.isdigit():
    print("Next enter the the mod search term")
    searchterm = input()
    def scpfromsteam(p):
        url = 'https://steamcommunity.com/workshop/browse/?appid=' + appid + '&searchtext=' + searchterm + '&p=' + str(p)

        info = scp.get(url=url).text
        soup = BeautifulSoup(info, 'lxml')
        results = soup.find_all("div", class_="workshopItemTitle")
        return results
    results = scpfromsteam(page)
    while i<len(results):
        print(str(i) + "." + results[i].get_text())
        i = i+1
    input()
else:
    input("please try again with a valid digit")

