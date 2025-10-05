from flask import Flask, render_template_string
import requests
import pandas as pd

app = Flask(__name__)

API_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+top+100+pl_name,pl_orbper,pl_rade+from+pscomppars+where+pl_orbsmax+%3C+1&format=json"

def fetch_exoplanet_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        return df.to_dict(orient='records'), f"Saved {len(data)} records"
    except requests.exceptions.RequestException as e:
        return [], f"Error fetching data: {e}"

@app.route('/')
def display_data():
    data, message = fetch_exoplanet_data()
    # Simple HTML template
    template = '''
    <!DOCTYPE html>
    <html>
    <head><title>Exoplanet Data</title></head>
    <body>
    <h1>NASA Exoplanet Data</h1>
    <p>{{ message }}</p>
    <table border="1">
    <tr><th>Planet Name</th><th>Orbital Period (days)</th><th>Radius (Earth radii)</th></tr>
    {% for row in data %}
    <tr><td>{{ row.pl_name }}</td><td>{{ row.pl_orbper }}</td><td>{{ row.pl_rade }}</td></tr>
    {% endfor %}
    </table>
    </body>
    </html>
    '''
    return render_template_string(template, data=data, message=message)

if __name__ == '__main__':
    app.run(debug=True)