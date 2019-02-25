from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
i = 0
while i < 20:
    i += 1
    my_url = "https://www.olx.ba/pretraga?trazilica=+Samsung+s5&kategorija=31&stranica=" + str(i)
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    results = page_soup.findAll("div", {"class": "listitem artikal obicniArtikal imaHover-disabled"})

    result = results[0]
    with open("pik_samsung_s5.csv", "a",) as samsung_s5:
      headers = "Naziv, Opis, Cijena, Lokacija\n"
      samsung_s5.write(headers)
      for result in results:
          name_result = result.findAll("p", {"class": "na"})
          name = name_result[0].text.replace(",", "|")
          sub_name = result.findAll("div", {"class": "pna"})
          subname = sub_name[0].text.replace(",", "|")
          price_result = result.findAll("div", {"class": "cijena"})
          price = price_result[0].span.text.replace(",", "|")
          location_result = result.findAll("div", {"class": "lokacijadiv"})
          location = location_result[0].text.replace(",", "|")
          samsung_s5.write(("{} , {} , {}, {} \n".format(name.encode(), subname.encode(), price.encode(), location.encode())))

