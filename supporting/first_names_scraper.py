import csv
import os
import re
import requests
import xlrd

def should_print(row):
    if len(row) < 6:
        return False
    if not row[0]:
        return False
    if "Liste aller jemals vergebenen ersten Bubennamen 1984-2017" == row[0]:
        return False
    if "Liste aller jemals vergebenen ersten Mädchennamen 1984-2017" == row[0]:
        return False
    if "Vorname" == row[0]:
        return False
    if "Original-Schreibweise" == row[0]:
        return False
    if "Q: STATISTIK AUSTRIA" == row[0]:
        return False
    return True

def download_convert_xlsx():
    url = "https://www.statistik.at/wcm/idc/idcplg?IdcService=GET_NATIVE_FILE&RevisionSelectionMethod=LatestReleased&dDocName=115202"
    resp = requests.get(url, allow_redirects=True)
    with open("temp_first_names.xlsx", "wb") as output:
        output.write(resp.content)
        output.close()
        print("Finished downloading xlsx file from: " + url)
    workbook = xlrd.open_workbook("temp_first_names.xlsx", encoding_override="utf-8")
   
    with open("first_names_male.csv", "w", encoding="utf-8") as csv_male:
        sheet_male = workbook.sheet_by_name("Bubennamen_1984-2017")
        writer_male = csv.writer(csv_male)
        for rownum in range(sheet_male.nrows):
            writer_male.writerow(sheet_male.row_values(rownum))
        print("Finished generating .csv for male names")
    
    with open("first_names_female.csv", "w", encoding="utf-8") as csv_female:
        sheet_female = workbook.sheet_by_name("Mädchennamen_1984-2017")
        writer_female = csv.writer(csv_female)
        for rownum in range(sheet_female.nrows):
            writer_female.writerow(sheet_female.row_values(rownum))
        print("Finished generating .csv for female names")

def parse_names(filename, occurence_threshold=5):
    with open(filename, encoding="utf-8") as csv_file:
        namelist = ""
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:           
            if not should_print(row):
                continue
            if not row[2]:
                continue
            if occurence_threshold > int(float(row[2])):
                print("Skipping {0} because {1} is below the threshold {2}".format(row[0], row[2], occurence_threshold))
                continue
            name_in_column = row[0]
            # Check for spaces to surround the name with quotation marks
            if re.search(r"\s", name_in_column):
                name_in_column = "\"" + name_in_column + "\""
            print(name_in_column)
            namelist = namelist +  name_in_column + " "
        return namelist

def cleanup():
    os.remove("temp_first_names.xlsx")
    os.remove("first_names_male.csv")
    os.remove("first_names_female.csv")    

def parse_male_and_female_names():
    download_convert_xlsx()
    male_names = parse_names("first_names_male.csv")
    female_names = parse_names("first_names_female.csv")
    cleanup()
    return male_names, female_names

male_names, female_names = parse_male_and_female_names()
with open("first_names_male.txt", "w", encoding="utf-8") as output:
    print(male_names, file=output)
with open("first_names_female.txt", "w", encoding="utf-8") as output:
    print(female_names, file=output)