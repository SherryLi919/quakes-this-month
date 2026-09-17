# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///

import requests
from pathlib import Path


def download_data(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    Path("data").mkdir(exist_ok=True)

    with open(filename, "wb") as file:
        file.write(response.content)


url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"

download_data(
    url,
    "data/earthquakes.geojson"
)
