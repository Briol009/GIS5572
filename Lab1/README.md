# ArcGIS to Cloud Data Pipeline

This repository contains code and instructions for setting up an automated data pipeline from ArcGIS to cloud software.

## Overview:

The aim of this project was to create a data pipeline from ArcGIS to cloud services. ArcPy Geometry primitives were used to create polygons, converted to (WKT) format, imported into a PostGIS database, and then the Flask application was used to retrieve polygon data from the database as a GeoJSON object in ArcOnline.

## Contents:

Notebooks: Creates polygons, converts polygons to WKT, and imports into PostGIS (database).

App: Includes the Flask application (app.py) for retrieving polygon data from PostGIS and serving as GeoJSON.

Documentation: Additional documentation and tutorials for setting up the data pipeline on Google Cloud Run and troubleshooting VM deployment issues were documented in the lab instructions.

## Instructions:

Refer to the notebooks for creating polygons using ArcPy Geometry primitives, converting to WKT, and importing into PostGIS using psycopg2.

Set up a Flask application using the provided app.py file to retrieve polygon data from PostGIS.

Follow the documentation to deploy the Flask application on Google Cloud Run. We followed this tutorial: https://www.youtube.com/watch?v=0mfng-vih_I

Follow lab instructions for the remainder of the tutorials, files, and links. We followed this tutorial: https://github.com/runck014/cloud_run_demo

## Note:

Ensure to handle sensitive information such as passwords securely.

For issues with VM deployment, consider migrating to Google Cloud Run.

For a detailed explanation of the data flow, refer to the provided video recording in folder Lab 1.2.