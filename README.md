![PuppyPlanner Logo](static/img/logos/pupplyplanner-100px.png)

# PuppyPlanner: The Reminders App

*PuppyPlanner* is a small demo web app for tracking reminders and managing your daily tasks.
It uses:

* [Python](https://www.python.org/) as the main programming language
* [FastAPI](https://fastapi.tiangolo.com/) for the backend
* [HTMX](https://htmx.org/) 1.8.6 for handling dynamic interactions (instead of raw JavaScript)
* [Jinja templates](https://jinja.palletsprojects.com/en/3.1.x/) with HTML and CSS for the frontend
* [TinyDB](https://tinydb.readthedocs.io/en/latest/index.html) for the database
* [Playwright](https://playwright.dev/python/) and [pytest](https://docs.pytest.org/) for testing


## Learning how it works

Development and testing are two sides of the same coin:

1. To learn how to *develop* full-stack Python apps, explore the FastAPI and HTMX integration patterns used in PuppyPlanner.
2. To learn how to *test* modern web apps, examine the comprehensive test suite including UI, API, and unit tests.

This project demonstrates modern full-stack Python development with dynamic frontend interactions.


## Installing dependencies

You will need a recent version of Python to run this app.
To install project dependencies:

```
pip3 install -r requirements.txt
```

It is recommended to install dependencies into a [virtual environment](https://docs.python.org/3/library/venv.html).


## Running the app

To run the app:

```
uvicorn app.main:app --reload
```

Then, open your browser to [`http://127.0.0.1:8000`](http://127.0.0.1:8000) to load the app.

## Logging into the app

The [`config.json`](config.json) file declares the users for the app.
You may use any configured user credentials, or change them to your liking.
The "default" username is `pupply` with the password `pupplyTest123`.


## Setting the database path

The app uses TinyDB, which stores the database as a JSON file.
The default database filepath is `reminder_db.json`.
You may change this path in [`config.json`](config.json).
If you change the filepath, the app will automatically create a new, empty database.

## Features

- **User Authentication**: Secure login system with configurable user credentials
- **Dynamic Lists**: Create, edit, and delete reminder lists
- **Task Management**: Add, edit, complete, and remove individual tasks
- **Real-time Updates**: HTMX-powered interactions without page refreshes
- **Responsive Design**: Clean, modern interface that works on all devices
- **RESTful API**: Well-documented API endpoints for all operations
