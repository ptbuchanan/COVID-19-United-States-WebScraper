from bs4 import BeautifulSoup
import requests
import csv

# get request parsing the html from site into text
source = requests.get('https://www.worldometers.info/coronavirus/country/us/').text

# indenting the html tags
soup = BeautifulSoup(source,'lxml')

# extracting the table from the tags
table = soup.find('table', id = "usa_table_countries_yesterday")

# store the table header in its own variable
table_header = table.find('thead').find_all('th')

# creating a file called results.csv in write mode
with open('results.csv', 'w') as f:

    # writing to file f
    writer = csv.writer(f)
    # storing the headers
    header = []
    # putting all data into new file
    new_list = []

    # taking all raw data from the headers
    for th in table_header:
        header.append(th.text)

    # removing the new lines from each one
    for element in header:
        new_list.append(element.strip())

    # removing \xa0 from the word
    new_list[8] = new_list[8].replace(u'\xa0', ' ')

    # removing \n from the word
    new_list[11] = new_list[11].replace('\n', ' ')

    # inserting the data from array into the csv file
    writer.writerow(new_list)

    # putting data into each row through tr tag
    for row in table.find_all('tr'):
        csvRow = []
        for data in row.find_all('td'):
            csvRow.append(data.text)
        for i in range(len(csvRow)):
            csvRow[i] = csvRow[i].replace('\n', '')

        writer.writerow(csvRow)

f.close()
