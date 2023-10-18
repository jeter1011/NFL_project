import requests
from bs4 import BeautifulSoup

# The URL of the page we want to scrape
url = "https://www.pro-football-reference.com/years/2022/draft.htm"

# Make a GET request to retrieve the page's content
response = requests.get(url)

# Parse the page's content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the draft data
table = soup.find("table", {"id": "drafts"})

# Find all rows in the table
rows = table.find_all("tr")

# Extract the column names from the second row
header_row = rows[1]
header_cols = header_row.find_all("th")
column_names = [col.get_text() for col in header_cols]

# Create a list to store the draft data
draft_data = []

# Loop through each row and extract the data
for row in rows[2:]:
    if "Rnd" in row.text:
        continue
    cells = row.find_all(["th", "td"])
    if cells:
        round_num = cells[0].get_text()
        pick_num = cells[1].get_text()
        team = cells[2].get_text()
        player = cells[3].get_text()
        position = cells[4].get_text()
        college = cells[5].get_text()
        draft_data.append([round_num, pick_num, team, player, position, college])


# Print the draft data
for data in draft_data:
    print(data)
