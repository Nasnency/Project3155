# Core Directory

This directory contains the "core" features of the webpage. Most of the features here relate to the launching or management of the site's behind-the-scenes behaviors, most notably including user sessions.

## session.py

This file contains the python code used to manage user sessions. A user's session is what ties their username (and other data) to the actions they perform on the site. In theory, multiple sessions can be active at once; in practice, this has not yet been implemented, and for testing purposes only one session is active at a time.

## utils.py

This file contains a collection of miscellaneous utilities that are used by the website. Primarily, this is for database-to-webpage communication, but also includes a few other features used in miscellaneous places that weren't easily classified as belonging to any one other file. 