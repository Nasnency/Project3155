# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Alex Gonzalez](mailto:agonza79@uncc.edu)
* [Zileyah Onafowora](mailto:zonafowo@uncc.edu)
* [Udoeyop David](mailto:dudoeyop@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |
| 1.1 | 03/27/23 | Initial draft edit | [Alex Gonzalez](mailto:agonza79@uncc.edu) | [Alex Gonzalez](mailto:agonza79@uncc.edu) |
| 1.2 | 03/30/23 | Intial draft edit | [Zileyah Onafowora](mailto:zonafowo@uncc.edu) |[Zileyah Onafowora](mailto:zonafowo@uncc.edu)
| 1.3 | 03/30/23 | Draft Formatting | [Alex Gonzalez](mailto:agonza79@uncc.edu) | [Alex Gonzalez](mailto:agonza79@uncc.edu) |
| 1.4 | 03/30/23 | Added further requirements, user cases and stories | [Alex Gonzalez](mailto:agonza79@uncc.edu) | [Alex Gonzalez](mailto:agonza79@uncc.edu) |
| 1.5 | 04/4/23 | Draft Formatting | [Udoeyop David](mailto:dudoeyop@uncc.edu) | [Udoeyop David](mailto:dudoeyop@uncc.edu) |
| 1.6 | 04/5/23 | Organized requirements, user cases and stories | [Alex Gonzalez](mailto:agonza79@uncc.edu) | [Alex Gonzalez](mailto:agonza79@uncc.edu) |

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

The site we plan to make is a webcomic-viewing page. We plan to make an interactive design that allows users to not just passively read, but actively join in on the experience with comments and bookmarking features. This will allow the artist to share their work and get feedback on it, while allowing readers to form a community around the project. 

## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

* **REQ 1.1.1:**
  * **Description:** The artist should be able to log in to a private page that readers cannot access, from which they can control their webcomic.
  * **Type:** `Functional`
  * **Priority:** 1
  * **Rationale:** The artist being able to control their content, and the readers not being able to manipulate it maliciously, is the central focus of the site.
  * **Testing:** The artist should input their credentials at a login page and verify that it redirects them to the control page; readers should be blocked or redirected if they attempt to do so.
* **REQ 1.1.2:** 
  * **Description:** The artist should be able to submit a new comic page from the control page.
  * **Type:** `Functional`
  * **Priority:** 1
  * **Rationale:** The entire purpose of this site is for the artist to share their work.
  * **Testing:** The artist should log into the control page and submit an image file, which should appear visible upon refresh for all users.
* **REQ 1.1.3:** 
  * **Description:** The artist should be able to remove comments from the control page.
  * **Type:** `Functional`
  * **Priority:** 3
  * **Rationale:** Just as it is important for users to leave comments, it should be important for artists to curate them, to prevent content they disagree with from being visible and associated with their work.
  * **Testing:** The artist should log into the control page and remove a pre-existing comment, which should vanish upon refresh for all users.
* **REQ 1.1.4:**
  * **Description:** The artist should be able to delete a comic page from the control page.
  * **Type:** `Functional`
  * **Priority:** 3
  * **Rationale:** The artist should have the ability to curate their content and be able to take down comic pages in case of error.
  * **Testing:** The artist should log into the control page and delete a comic page, which should vanish upon refresh for all users.
* **REQ 1.1.5:** 
  * **Description:** The reader should be able to bookmark a comic page.
  * **Type:** `Functional`
  * **Priority:** 3
  * **Rationale:** Allowing a user to preserve a comic page for future reference and return to it later would enrich their enjoyment of the comic. 
  * **Testing:** The user should log into the website, navigate to a page they would like to bookmark, and then bookmark it. The page should then appear in their list of bookmarks for later review. 
* **REQ 1.1.6:** 
  * **Description:** A reader should be able to leave a comment under a comic page, which will then become visible to other users when they refresh the page.
  * **Type:** `Functional`
  * **Priority:** 3
  * **Rationale:** User engagement is a core part of the design and experience of the site, and allows the artist to receive feedback, as well.
  * **Testing:** A reader should write and submit a comment; a separate user, upon refreshing the page, should be able to view the comment. 
* **REQ 1.1.7:**
  * **Description:** A reader should be able to edit their own comments left under a comic page.
  * **Type:** `Functional`
  * **Priority:** 4
  * **Rationale:** Humans make mistakes, and it is important to cater for that when building this site.
  * **Testing:** User should be able to click edit button to edit an existing comment. New comment should be shown upon refresh for all users.
* **REQ 1.1.8:** 
  * **Description:** Users should be able to navigate forwards and backwards through different comic pages. 
  * **Type:** `Functional`
  * **Priority:** 1
  * **Rationale:** Being able to navigate to pages other than the most recent allows the users to enjoy previous pages and read the comic as a whole.
  * **Testing:** The user should access the webcomic site, and then click the feature that moves them to a new page, which should load the webpage for that comic page.
* **REQ 1.1.9:** 
  * **Description:** Users without an account should be able to register an account by providing a username, email address and password.
  * **Type:** `Functional`
  * **Priority:** 2
  * **Rationale:** Having an account allows the user to interact actively with the site through features such as bookmarking and commenting.
  * **Testing:** The user should input the required credentials at the account registration page and succesfully create an account. If an email address is already associated with an account, the site should prompt the user to log in instead.
* **REQ 1.2.0:** 
  * **Description:** Users with an existing account should be able to log in by providing a username and password.
  * **Type:** `Functional`
  * **Priority:** 2
  * **Rationale:** Logging in allows the user to access their personalized features.
  * **Testing:** The user should input the required credentials at the log in page and succesfully log into their account. If password or username is incorrect or not found, the site should warn the user.
* **REQ 1.2.1:** 
  * **Description:** Users should recieve a URL in their clipboard by pressing a share button.
  * **Type:** `Functional`
  * **Priority:** 5
  * **Rationale:** Allowing users to share the website and its content will facilitate the site's growth. 
  * **Testing:** The user should be able to click the share button and receive a formatted message containing the website's URL in their clipboard. The share button should display a message to notify the user of this action. 
* **REQ 1.2.2:** 
  * **Description:** The site should reflect the theme of the artist's comic.
  * **Type:** `Non-functional`
  * **Priority:** 5
  * **Rationale:** The site should be appealing to the audience and follow the comic's aesthetic theme.


## Constraints

The project should preload the comic and comments, instead of loading them after the fact, for speed.

The project should not take more than 5 seconds to load on a 20 Mbps internet connection.

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **UC 1.1.1:** As a reader, I want to leave a comment under a comic page.
  * **Description:** A reader creates a new comment under a comic page. 
  * **Actors:** Reader leaving the comment.
  * **Preconditions:** The page has been completely loaded, including the comic and the other comments. 
  * **Postconditions:** The comment has been left on the page, and is visible on other users' pages after they refresh the page. 
* **UC 1.1.2:** As an artist, I want to remove a comment from a comic page. 
  * **Description:** Artist selects a comment for removal, and removes it.
  * **Actors:** Artist removing the comment.
  * **Preconditions:** The artist is logged in to the control page. There is already a comment, which is to be removed.
  * **Postconditions:** The comment has been removed. 
* **UC 1.1.3:** As a reader, I want to bookmak a comic page.
  * **Description:** Reader clicks a bookmarking button and bookmarks a page.
  * **Actors:** Reader marking the page.
  * **Preconditions:** The reader is logged in and on the page they want to bookmark.
  * **Postconditions:** The page is bookmarked and added to that reader's bookmarks.
* **UC 1.1.4:** As a site user, I want to navigate through the comic pages with back and forward buttons.
  * **Description:** User selects a button and navigates through the comic pages.
  * **Actors:** User navigating the site.
  * **Preconditions:** The user is on the site.
  * **Postconditions:** The user has navigated to a different comic page. 
* **UC 1.1.5:** As an artist, I want to submit new comic pages to the site.
  * **Description:** Artist selects an image file to upload, and uploads it to the site.
  * **Actors:** Artist submitting a new comic page.
  * **Preconditions:** The artist is in the control page and has selected an image file to submit.
  * **Postconditions:** There is a new comic page available for all users to see. 
* **UC 1.1.6:** As a reader, I want to be able to edit an exsisting comment.
  * **Description:** Reader clicks the edit button and edits their comment.
  * **Actors:** Reader editing their comment.
  * **Preconditions:** The reader is logged to the site and on a comic page with a comment previously created by them. 
  * **Postconditions:** The comment has been edited. 

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

* **US 1.1.1:** 
  * **Type of User:** `Reader`
  * **Description:** As a reader, I want to enjoy reading a webcomic and connect with the community around it. I expect to load a page, read a comic, and then read the comments left underneath it. If I am so inclined, I also expect to leave a comment of my own; in occasional circumstances, I may even wish to refresh the page several times in a row, both for purposes of having "conversations" and to eagerly begin reading a new page the instant it is published.
* **US 1.1.2:** 
  * **Type of User:** `Artist`
  * **Description:** As an artist, I want to curate the community that I am fostering around my project. After having posted a new page, I would like to review the praise, critiques, and other such comments that will appear beneath it. I would also like to filter and remove the inevitable objectionable comments, so that my work can be enjoyed by others without intrusion.
* **US 1.1.3:** 
  * **Type of User:** `Reader`
  * **Description:** As a reader, I would like to bookmark a page so that I may return to it later. After navigating to a page that I would like to mark for later, I will click on a button, which will add the page to my bookmarks. I will then go to my bookmarks page, and review the bookmarks I have saved.
* **US 1.1.4:** 
  * **Type of User:** `User`
  * **Description:** As a user of the site, I want to click the buttons that will navigate me forward and backward through the comic, and then be navigated as expected through said comic to other pages.
* **US 1.1.5:** 
  * **Type of User:** `User`
  * **Description:** As a user of the site, I want to share this webpage with others and in other platforms in an easy and quick manner. 
* **US 1.1.6:** 
  * **Type of User:** `Artist`
  * **Description:** As an artist, I want my webpage to follow the theme of my artwork and be appealing to my audience. 

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Term:** Artist
  * **Definition:** The owner of the site, who creates the displayed art and curates the comments and community that revolve around it.
* **Term:** Reader
  * **Definition:** The users of the site who have an account, who enjoy the created webcomic and leave comments regarding it.
* **Term:** User
  * **Definition:** Anyone who is interacting with the site, Artist or Reader.
