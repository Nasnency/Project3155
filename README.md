# Webcomic Display Site

## Description

This repository contains semi-functional code for an online site designed to host and share a webcomic. It was built as 6-week-long project for ITSC 3155. Significant features are not yet implemented. This site should not be seen as complete, as development will continue past the end of the semester. Functional features that are currently working include registration, login, logout, and leaving comments. Features that are not yet working include comic uploading and comment moderation.

## Documentation Note

The remainder of this README is mostly copied verbatim from the original README provided with the site template. Although the site's content and functions have undergone significant changes, the requirements to launch it, thankfully, have not. The README files contained in the directiories mentioned below, however, are completely new, and should be reviewed.

<br>

----

<br>

## How to Use

Go into the ComicCorner folder. To run this project, you simply need to have Python 3.10 installed on your machine. You can download Python 3.10 from the [official website](<https://www.python.org/downloads/release/python-3108>).

### Setup Script (Recommended)

A script titled `setup.sh` is included at the root of this repository, which will automatically install the required dependencies and set up the database. To run this script, execute the following command:

```bash
bash setup.sh
```

If you instead prefer to manually install the python module dependencies, run the following command:

```bash
pip install -r requirements.txt # or pip3 install -r requirements.txt if pip is not set to use Python 3
```

### Running the Server

Another script titled `run.sh` is also included at the root of this repository, which will automatically run the application. Execution of this script is recommended but not required. If you would like to manually run the server, run the following command:

```bash
./run.sh # or bash run.sh if permissions are not set
```

## Documentation Style

Across all files, classes and functions are documented using docstrings, which are formatted according to the [Google Python Style Guide](<https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>).

Additionally, `authentication`, `core`, `database`, `static` `templates`, and `tests` each contain their own `README.md` file, where the contents of each directory are described in more detail.

## Testing

The unit tests are kept across various files in the `testing` directory. From the root of the repository, you can run the `test.py` script to check all unit tests, which will generate a report in the `testing/reports` directory.
