from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os

i = 0
#inp_1 = input("Unesite prvi pojam pretrage: ")
#inp_2 = input("Unesite drugi pojam pretrage: ")
inp_3 = input()
inp_4 = list(inp_3)
inp_5 = "".join(inp_4[:-1])
while i < 20:
    i += 1
    my_url = "https://www.{}{}".format(inp_5, i)
    print(my_url)
    #my_url = "https://www.olx.ba/pretraga?trazilica=+{}+{}&kategorija=31&stranica=".format(inp_1, inp_2) + str(i)
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    results = page_soup.findAll("div", {"class": "listitem artikal obicniArtikal imaHover-disabled"})

    result = results[0]
    with open("pik_samsung_s5.csv", "a", encoding="utf-8") as samsung_s5:

        headers = "Naziv, Opis, Cijena, Lokacija\n"
        if os.stat('pik_samsung_s5.csv').st_size == 0:
            samsung_s5.write(headers)
        else:
            for result in results:
                name_result = result.findAll("p", {"class": "na"})
                name = name_result[0].text.replace(",", "|")
                sub_name = result.findAll("div", {"class": "pna"})
                subname = sub_name[0].text.replace(",", "|")
                price_result = result.findAll("div", {"class": "cijena"})
                price = price_result[0].span.text.replace(",", "|")
                location_result = result.findAll("div", {"class": "lokacijadiv"})
                location = location_result[0].text.replace(",", "|")
                samsung_s5.write("{} , {} , {}, {} \n".format(name, subname, price, location))

