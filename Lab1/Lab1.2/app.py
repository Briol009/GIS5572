from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

# Database configuration
#with open(r'./PASS/database.txt', 'r') as file:
#    database_key = file.read().strip()
database_key = 'loganandgreg'

DB_NAME = "gis5572"
DB_USER = "postgres"
DB_PASSWORD = database_key
DB_HOST = "35.232.21.197"
DB_PORT = "5432"

@app.route('/')
def hello_world():
    return "hello world!"

# Route to retrieve polygon as GeoJSON
# this connects to the database and runs SQL query that returns geojson object
@app.route('/geojson_polygon')
def get_polygon_geojson():
    # Connect to the database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    # Create a cursor
    # asks database for ArcGIS text for polygon
    # returns polygon as a geojson string of text
    cur = conn.cursor()

    query = """
        SELECT 
            json_build_object(
                'type', 'FeatureCollection',
                'features', json_agg(
                    json_build_object(
                        'type', 'Feature',
                        'geometry', ST_AsGeoJSON(ST_SetSRID(shape, 4326))::json,
                        'properties', json_build_object()
                    )
                ),
                'crs', 
                json_build_object(
                    'type', 'name',
                    'properties', 
                    json_build_object(
                        'name', 'epsg:4326'
                    )
                )
            ) AS geojson
        FROM lab1
    """

    # Execute SQL query to retrieve the polygon
    cur.execute(query)
    row = cur.fetchone()[0]

    # Close cursor and connection
    cur.close()
    conn.close()

    # Return the GeoJSON
    return row

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
