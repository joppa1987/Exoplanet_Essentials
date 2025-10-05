NASA Exoplanet Data Fetcher
A Python script to fetch and save confirmed exoplanet data from NASA's Exoplanet Archive, designed for planetary science research and data analysis.
Overview
This project automates the retrieval of exoplanet data from the NASA Exoplanet Archive using its Table Access Protocol (TAP) API. It fetches key parameters (planet name, orbital period, and radius) for up to 100 exoplanets with orbits closer than 1 AU (Astronomical Unit). The data is saved as timestamped CSV and JSON files for further analysis, with optional visualization as an interactive HTML scatter plot.
Inspired by NASA's Kepler and TESS missions, this tool simplifies access to exoplanet data for researchers, students, and space enthusiasts.
Features

Retrieves exoplanet data: name (pl_name), orbital period (pl_orbper), and radius (pl_rade).
Filters for planets within 1 AU (inner solar system analogs).
Outputs data in CSV and JSON formats with timestamps.
Optional: Generates an interactive scatter plot using Plotly.
Robust error handling for API and network issues.

Requirements

Python 3.6+
Libraries: requests, pandas, (optional) plotly
Internet connection to access the NASA API

Installation

Clone or download this repository:git clone https://github.com/yourusername/nasa-exoplanet-fetcher.git
cd nasa-exoplanet-fetcher


Install dependencies:pip install requests pandas

For the optional chart feature:pip install plotly



Usage

Run the script:
python planetary_data.py


Output:

Console: Displays a success message, number of records fetched, and a preview of the first five rows.
Files: Generates exoplanet_data_YYYYMMDD_HHMMSS.csv and exoplanet_data_YYYYMMDD_HHMMSS.json in the project directory.
Optional: If using the Plotly version, an HTML file (exoplanet_chart_YYYYMMDD_HHMMSS.html) with a scatter plot.

Example Output:
Data fetched successfully! Saved 92 records to exoplanet_data_20251005_105300.csv and exoplanet_data_20251005_105300.json
Sample data:
      pl_name  pl_orbper  pl_rade
0  Kepler-452b  384.843    1.63
1  TRAPPIST-1d    4.049     0.78
...


Open the CSV in Excel or the HTML chart in a browser for analysis.


Data Source

API: NASA Exoplanet Archive TAP Service (link).
Table: pscomppars (Planetary Systems Composite Parameters).
Query: SELECT TOP 100 pl_name, pl_orbper, pl_rade FROM pscomppars WHERE pl_orbsmax < 1.

Future Enhancements

Add a Flask-based web dashboard to display data interactively.
Integrate machine learning to predict exoplanet habitability.
Expand to other NASA APIs (e.g., Mars rover images).
Support more parameters (e.g., star temperature, planet mass).

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-name).
Commit changes (git commit -m "Add feature").
Push to the branch (git push origin feature-name).
Open a Pull Request.

Please report issues or suggest features via the Issues tab.
License
This project is licensed under the MIT License. See the LICENSE file for details.
References

NASA Exoplanet Science Institute. (2025). Exoplanet Archive TAP Service. Retrieved from https://exoplanetarchive.ipac.caltech.edu/docs/TAP.html
NASA. (2025). Kepler and TESS Missions. Retrieved from https://www.nasa.gov/mission_pages/kepler/overview

Acknowledgments

Inspired by NASA's open data initiatives and exoplanet exploration efforts.
Built for educational and research purposes as part of a university project.
