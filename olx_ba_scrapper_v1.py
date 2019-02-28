from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import datetime


inp_1 = input("Unesite prvi pojam pretrage: ")
inp_2 = input("Unesite drugi pojam pretrage: ")
FILE_NAME = "pik_{}_{}_{}.csv".format(inp_1, inp_2, str(datetime.now().strftime("%d-%m-%Y, %H-%M-%S")))

Paid = ("div", {"class": "listitem artikal obicniArtikal imaHover-disabled i"})
Regular = ("div", {"class": "listitem artikal obicniArtikal imaHover-disabled"})
Highlight = ("div", {"class": "listitem artikal obicniArtikal istaknin imaHover-disabled"})

def scrapper(source):
    i = 0
    while True:
        i += 1
        my_url = "https://www.olx.ba/pretraga?trazilica=+{}+{}&stranica={}".format(inp_1, inp_2, str(i))
        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        results = page_soup.findAll(source[0], source[1])
        print(results)
        try:
            result = results[0]
            for result in results:
                name_result = result.findAll("p", {"class": "na"})
                name = name_result[0].text.replace(",", "|")
                sub_name = result.findAll("div", {"class": "pna"})
                subname = sub_name[0].text.replace(",", "|")
                price_result = result.findAll("div", {"class": "cijena"})
                price = price_result[0].span.text.replace(",", "|")
                location_result = result.findAll("div", {"class": "lokacijadiv"})
                location = location_result[0].text.replace(",", "|")
                file.write("{} , {} , {}, {} \n".format(name, subname, price, location))
        except Exception as ex:
            break

with open("results/" + FILE_NAME, "a", encoding="utf-8") as file:
    file.write("Naziv, Opis, Cijena, Lokacija\n")
    scrapper(Paid)
    scrapper(Regular)
    scrapper(Highlight)
