import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://overthecap.com/rookie-class-evaluation"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", {"class": "sortable snap-index"})
rows = table.find_all("tr")

header_row = rows[0]
header_cols = header_row.find_all("th")
column_names = [col.get_text() for col in header_cols[0:]]

print(column_names)
#
# print(header_row)
# print(header_cols)

draft_data = []
for row in rows[:]:
    cells = row.find_all("td")
    if cells:
        row_header = cells[0].get_text()
        row_data = [row_header] + [cell.get_text() for cell in cells[1:]]
        draft_data.append(row_data)

rookie_class_eval_df = pd.DataFrame(draft_data, columns=column_names)
rookie_class_eval_df.to_csv("rookie_eval.csv", index=False)

# # Get the header text from the first cell in each row
# row_headers = []
# for row in rows:

#     cells = row.find_all("th")
#     if cells:
#         row_header = cells[0].get_text()
#         row_headers.append(row_header)
#
# # Print the row headers
# print(row_headers)