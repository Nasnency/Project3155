# Authentication Directory

This directory contains the functions and data related to user authentication. It is sparsely populated, as most of the features are contained in a single file. In its original form, the passwords were being stored in a .txt file; the updated version instead stores them in a database.

## authTools.py

This file contains the entirety of the authentication functions for the webpage. Everything from password validation to username uniqueness checking is present in this file. Many of these functions work closely with the database, using it to verify data and ensure that users are able to browse the site in a safe and secure manner.