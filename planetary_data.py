import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

API_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+top+100+pl_name,pl_orbper,pl_rade+from+pscomppars+where+pl_orbsmax+%3C+1&format=json"

def fetch_exoplanet_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        
        # Save to CSV
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_filename = f"exoplanet_data_{timestamp}.csv"
        df.to_csv(csv_filename, index=False)
        
        # Generate Plotly scatter plot
        fig = px.scatter(df, x="pl_orbper", y="pl_rade", text="pl_name", 
                        title="Exoplanet Orbital Period vs. Radius",
                        labels={"pl_orbper": "Orbital Period (days)", "pl_rade": "Radius (Earth radii)"})
        fig.update_traces(textposition="top center")
        fig.write_html(f"exoplanet_chart_{timestamp}.html")
        
        print(f"Data fetched successfully! Saved {len(data)} records to {csv_filename}")
        print(f"Chart saved as exoplanet_chart_{timestamp}.html")
        print("\nSample data:")
        print(df.head())
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_exoplanet_data()