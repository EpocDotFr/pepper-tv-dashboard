from flask import render_template, jsonify
from ptvd import app, cache
import services


@app.route('/')
def home():
    # print(services.fetch_app_info(services.Stores.ITUNES, id='914813032', country='fr'))

    return render_template('home.html')


@app.route('/apps-info')
@cache.cached(timeout=60 * 60)
def apps_info():
    return jsonify(services.fetch_all_pepper_apps_info())
