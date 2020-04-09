from bs4 import BeautifulSoup
import requests
import csv

my_csv = open("scraped_data.csv", "w")
my_csv_writer = csv.writer(my_csv)
web_page = requests.get("https://www.mohfw.gov.in/").text

soup_obj = BeautifulSoup(web_page, "lxml")
soup_obj = soup_obj.find("section", id="state-data")
table = soup_obj.table

headings = table.thead.find_all("strong")
heads = []
for i in headings:
    heads.append(i.text)

my_csv_writer.writerow(heads)

complete_row = []
for rows in table.tbody.find_all("tr"):
    for table_data in rows.find_all("td"):
        complete_row.append(table_data.text)
    my_csv_writer.writerow(complete_row)
    complete_row.clear()

my_csv.close()
print("Written to CSV.. Wow!")
