import re 
import pandas as pd
import csv
from bs4 import BeautifulSoup
import csv

with open('abc.html') as html_file:
    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_file, 'html.parser')
    
    td_title = soup.find_all('td', {'style': 'text-align: left; width: 200px'})
    headings = []
    for td_head in td_title[:10]:
        if td_head.find('strong'):
            td_head = td_head.text.strip()
            headings.append(td_head)
    print(headings)

    td_tags = soup.find_all('td', {'style': 'text-align: left'})
    rows = []
    for i, td_data in enumerate(td_tags):
        if i % 10 == 0:
            rows.append([])
        rows[-1].append(td_data.text.strip())
    print(rows)

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headings)
    writer.writerows(rows)
    
    # td_title = soup.find_all('td', {'style': 'text-align: left; width: 200px'})
    # td_tags = soup.find_all('td', {'style': 'text-align: left'})

    # # Open a CSV file for writing
    # with open('data.csv', 'w', newline='') as csv_file:
    #     writer = csv.writer(csv_file)

    #     # Write the headers
    #     writer.writerow(['Title', 'Tags'])

    #     # Write the data
    #     for td_title, td_tags in zip(td_title, td_tags):
    #         if td_title.find('strong'):
    #             title = td_title.text.strip()
    #             tags = td_tags.text.strip()
    #             writer.writerow([title, tags])
                
    
    # td_title = soup.find_all('td', {'style': 'text-align: left; width: 200px'})

    # for td in td_title[:10]:
    #     if td.find('strong'):
    #         print(td.text)
           
    # td_tags = soup.find_all('td', {'style': 'text-align: left'})

    # for td in td_tags:
    #     print(td.text.strip())
                

    # # Find the table in the HTML file
    # table = soup.find('table', attrs={'class':'main_table'})
    # # print(table)
    # active_td_element = None
    
    # # Find all the rows in the table
    # for row in table.find_all("tr"):
    #     # print(row)
    #     cells = row.find_all('tbody')   
    #     # print(cells)     
        
    #     for cell in cells:
    #         td_element = cell.find_all('td')  
    #         print("td.......",td_element)
    #         for columdata in td_element:
    #             # print(columdata.text)
            
            

# python3 just use th.text
# headers = [th.text.encode("utf-8") for th in table.select("tr th")]

# with open("out.csv", "w") as f:
#     wr = csv.writer(f)
#     wr.writerow(headers)
#     wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])