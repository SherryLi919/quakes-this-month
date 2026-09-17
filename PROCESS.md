# Process

## Tools

- Python for downloading and processing the earthquake data.
- `uv` for running the Python scripts and managing the script dependency on Matplotlib.
- Matplotlib for creating the earthquake visualization.
- Git and GitHub for version control and publishing the project.
- USGS GeoJSON feed for the earthquake data.

## Kept

I kept the downloaded earthquake GeoJSON file unchanged as
`data/earthquakes.geojson`. This keeps the raw data separate from the
plotting code and allows the plotting program to work without another
internet connection.

## Rejected

I rejected the original weather-data example from the template because
this project is about earthquakes. I replaced that example with a USGS
earthquake data workflow and a global earthquake plot.
