# ArcGIS to Cloud Data Pipeline README

This repository contains code and instructions for setting up an automated data pipeline from ArcGIS to cloud software.

## Overview:

The aim of this project was to establish a seamless data pipeline from ArcGIS to cloud services. We utilized ArcPy Geometry primitives to create polygons, converted them to Well Known Text (WKT) format, and imported them into a PostGIS database using psycopg2. Subsequently, we developed a Flask application to retrieve polygon data from the database and serve it as GeoJSON objects. Finally, we integrated the Flask application into ArcGIS Online for visualization.

## Contents:

Notebooks: Contains Jupyter notebooks detailing the step-by-step process of creating polygons, converting to WKT, and importing into PostGIS.

App: Includes the Flask application (app.py) for retrieving polygon data from PostGIS and serving as GeoJSON.

Documentation: Additional documentation and tutorials for setting up the data pipeline on Google Cloud Run and troubleshooting VM deployment issues.

## Instructions:

Refer to the notebooks for creating polygons using ArcPy Geometry primitives, converting to WKT, and importing into PostGIS using psycopg2.
Set up a Flask application using the provided app.py file to retrieve polygon data from PostGIS.
Follow the documentation to deploy the Flask application on Google Cloud Run for seamless integration with ArcGIS Online.

## Note:

Ensure to handle sensitive information such as passwords securely.

For issues with VM deployment, refer to the troubleshooting guide and consider migrating to Google Cloud Run.

For a detailed explanation of the data flow and setup process, refer to the provided video recording.