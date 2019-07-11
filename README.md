# Pepper TV Dashboard™

A web page showing various [Pepper](https://www.pepper.com/) mobile apps-related data.

## Prerequisites

  - Python >= 3.5
  - A modern web browser
  - (Optional, but recommended) A [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)-capable web server

## Installation

  1. Clone this repo somewhere
  2. `pip install -r requirements.txt`

## Configuration

Copy the `config.example.py` file to `config.py` and fill in the configuration parameters.

Available configuration parameters are:

  - `SECRET_KEY` Set this to a complex random value

I'll let you search yourself about how to configure a web server along uWSGI.

## Usage

  - Standalone

Run the internal web server, which will be accessible at `http://localhost:8080`:

```
python local.py
```

Edit this file and change the interface/port as needed.

  - uWSGI

The uWSGI file you'll have to set in your uWSGI configuration is `uwsgi.py`. The callable is `app`.

  - Others

You'll probably have to hack with this application to make it work with one of the solutions described
[here](http://flask.pocoo.org/docs/0.12/deploying/).
