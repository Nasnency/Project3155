# Database Directory

This directory contains the database assets for the application. In addition to hosting the database itself, it also contains a setup script and a python file for database functions. 

## comicData.db

This file is the actual database used for the website. It contains information including user login data, comments, and file data for the comic pages. 

## db.py

This file manages the database connections for the website, and performs fetching, updating, and validation for everythign from user login to webpage loading. 

## resetDB.sh

This file is a debugging script used to return the database to its default state. It will wipe all data in the database: use with caution!

## schema.sql

This file contains the database schema, and is used to create the database in the first place. Descriptors of the tables can be found within it. 

## startingData.sql

This file is for debugging purposes, and contains some starting data that can be put into the database upon reset. 