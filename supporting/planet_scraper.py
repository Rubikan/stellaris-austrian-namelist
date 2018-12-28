import csv
import re
import requests

def should_print(row):
    if len(row) < 4:
        return False
    if not row[3]:
        return False
    if "Ortschaftsname" == row[3]:
        return False
    return True

def parse_planetnames():
    url = "https://www.statistik.at/verzeichnis/reglisten/ortsliste.csv"
    namelist = ""
    print("Pulling CSV from: " + url)
    resp = requests.get(url)
    csv_reader = csv.reader(resp.text.split("\n"), delimiter=";")
    for row in csv_reader:
        if not should_print(row):
            continue
        name_in_column = row[3]
        # Check for spaces to surround the name with quotation marks
        if re.search(r"\s", name_in_column):
            name_in_column = "\"" + name_in_column + "\""
        print(name_in_column)
        namelist = namelist +  name_in_column + " "
    return namelist

with open("planet_names.txt", "w") as output:
    print(parse_planetnames(), file=output)