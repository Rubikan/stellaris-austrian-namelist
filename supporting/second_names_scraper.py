import re
import requests
from bs4 import BeautifulSoup

def parse_second_names():
    print("Parsing second names")
    url_without_page = "https://namenskarten.lima-city.at/oesterreichs-haeufigste-nachnamen.php?p="
    namelist = ""
    for i in range(100):
        url = url_without_page + str(i)
        print("Opening URL: " + url)
        resp = requests.get(url)
        parsed_page = BeautifulSoup(resp.text, "html.parser")       
        for row in parsed_page.findAll("table")[0].findAll("tr"):
            tds = row.findAll("td")
            if not tds:
                continue
            name_in_column = BeautifulSoup(str(tds[1].contents[0]), "html.parser").findAll("a")[0].text           
            # Check for spaces to surround the name with quotation marks
            if re.search(r"\s", name_in_column):
                name_in_column = "\"" + name_in_column + "\""
            print(name_in_column)
            namelist = namelist +  name_in_column + " "
    return namelist

with open("second_names.txt", "w") as output:
    print(parse_second_names(), file=output)