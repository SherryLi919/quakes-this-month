# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

import json
from pathlib import Path

import matplotlib.pyplot as plt


def point_size(magnitude):
    """Turn earthquake magnitude into a visible point size."""
    if magnitude is None:
        return 0
    return max(2, magnitude**3)


def make_plot(data_file, output_file):
    with open(data_file, encoding="utf-8") as file:
        data = json.load(file)

    longitudes = []
    latitudes = []
    sizes = []

    skipped = 0

    for earthquake in data["features"]:
        magnitude = earthquake["properties"]["mag"]
        coordinates = earthquake["geometry"]["coordinates"]

        if magnitude is None or coordinates[0] is None or coordinates[1] is None:
            skipped += 1
            continue

        longitudes.append(coordinates[0])
        latitudes.append(coordinates[1])
        sizes.append(point_size(magnitude))

    Path(output_file).parent.mkdir(exist_ok=True)

    plt.figure(figsize=(14, 7))

    plt.scatter(
        longitudes,
        latitudes,
        s=sizes,
        alpha=0.45,
    )

    plt.xlabel("Longitude (degrees)")
    plt.ylabel("Latitude (degrees)")
    plt.title("Global Earthquakes — Last 30 Days")

    plt.xlim(-180, 180)
    plt.ylim(-90, 90)

    plt.grid(alpha=0.2)

    plt.tight_layout()
    plt.savefig(output_file, dpi=200)
    plt.close()

    print(f"Plotted {len(longitudes)} earthquakes.")
    print(f"Skipped {skipped} records without usable location or magnitude.")


make_plot(
    "data/earthquakes.geojson",
    "out/earthquakes.png",
)
