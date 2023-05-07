# Templates directory

This fodler only contains the html files for the application. Flask assumes html files will be stored in a subdirectory titles `templates`, so any added pages should be placecd here. 

## 404.html

This file contains the html displayed when the user attempts to navigate to a page that does not exist. It was added to stop flask from throwing errors when a url was mistyped during testing, and includes a link to the home page. 

## 500.html

This file contains the html displayed when the server encounters an internal error. As this site is still under active development, the 500 page appears with unfortunate frequency, and was given a humorous style to lessen the frustration of encountering yet another python bug. It is a dead-end page with no links. 

## about.html

This file is currently a placeholder. It will eventually provide information about the webcomic, artist, and site. The placeholder art was drawn by Vanessa Hosek.

## archive.html

This file is currently a placehodler. It will eventually contain a gallery of compressed-and-shrunken thumbnail images, each acting as a link to the respective comic page they represent. The placeholder art was drawn by Alex Gonzalez.

## cast.html

This file is currently a placeholder. It will eventually list off the characters featured in the comic, alongside fictionaly biographies and concept art. The placeholder art was drawn by "Mads", who wished to remain anonymous.

## control.html

This file contains the html for the artist's control page. It is currently non-functional, but will eventually allow the artist to control their site and it scontant. From this page, the artist will be able to upload or remove comic pages, moderate comments, and make other changes, such as banning a user. 

## index.html

This file contains the html for the "home" page. It is also used to display any single comic page, as well as any comments associated with it. It also allows users to navigate through comic pages, and through the use of forms, lets users leave comments through the `post_comment()` method in the `app.py` file. Note that this page technically resides at the `/home` url. 

## layout.html

This file contains the html for the "header" of the site, and appears at the top of every page except the login, registration, and control pages. It performs a number of featrures, including redirects to the login/registration pages; once the user is logged in, these buttons merge into a new one that allows users to logout. 

## login.html

This file contains the html for the login page. It uses html forms to collect login information from the user, and then passes it to the `login()` method in the `app.py` file.

## register.html

This file contains the html for the registration page. It uses html forms to collect registration information from the user, and then passes it to the `register()` method in the `app.py` file. 

## signup-layout.html

This file contains a modified form of the header found in `layout.html`. It is identical, save for the absence of the "login" and "register" buttons. It is only displayed on the "login" and "register" pages. 