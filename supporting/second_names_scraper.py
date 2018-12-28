import requests
from bs4 import BeautifulSoup

url_without_page = "https://namenskarten.lima-city.at/oesterreichs-haeufigste-nachnamen.php?p="
with open('second_names.txt', 'w') as output:
    for i in range(100):
        url = url_without_page + str(i)
        print("Opening URL: " + url)
        req = requests.get(url)
        parsed_page = BeautifulSoup(req.text, "html.parser")
        for row in parsed_page.findAll("table")[0].findAll("tr"):
            tds = row.findAll("td")
            if not tds:
                continue
            name_in_column = BeautifulSoup(str(tds[1].contents[0]), "html.parser").findAll("a")[0].text
            print(name_in_column)
            print(name_in_column, file=output, sep=" ", end=" ")