import requests
import pandas as pd


url = "https://api.spacexdata.com/v4/launches"

response = requests.get(url)
data = response.json()

launches_data = []
for launch in data:
    launch_data = {
        'Flight Number': launch['flight_number'],
        'Mission Name': launch['name'],
        'Launch Date': launch['date_utc'],
        'Rocket Name': launch['rocket'],
        'Launch Site': launch['launchpad'],
        'Launch Success': launch['success'],
    }
    launches_data.append(launch_data)

launches_df = pd.DataFrame(launches_data)


launches_df['Launch Date'] = pd.to_datetime(launches_df['Launch Date']).dt.strftime('%Y-%m-%d %H:%M:%S')

print(launches_df)
