import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create a list to store the draft data
draft_data = []

# Loop through each year from 1990 to 2022
for year in range(1990, 2023):
    url = f"https://www.pro-football-reference.com/years/{year}/draft.htm"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table containing the draft data
    table = soup.find("table", {"id": "drafts"})

    if table:
        # Find all rows in the table
        rows = table.find_all("tr")

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
                draft_data.append([round_num, pick_num, team, player, position])
    else:
        print(f"Warning: Unable to find table for year {year}")

# Create a pandas DataFrame from the draft data
df = pd.DataFrame(draft_data, columns=["Round", "Pick", "Team", "Player", "Position"])

# Save the DataFrame to a CSV file
df.to_csv("nfl_draft_data.csv", index=False)
