from enum import Enum
from lxml import html
from ptvd import app
import requests


class Stores(Enum):
    GOOGLE_PLAY = 'google-play'
    ITUNES = 'itunes'

GOOGLE_PLAY_APP_URL = 'https://play.google.com/store/apps/details'
ITUNES_APP_URL = 'https://itunes.apple.com/{country}/app/whatever/id{id}'

requests = requests.Session()


def _fetch_and_parse(url, params):
    response = requests.get(url, params=params, timeout=3)

    response.raise_for_status()

    return html.fromstring(response.text)


def _fetch_google_play_app_info(id):
    params = {
        'id': id,
        'hl': 'en'
    }

    response_parsed = _fetch_and_parse(GOOGLE_PLAY_APP_URL, params=params)

    rating = None
    votes = None

    rating_container = response_parsed.xpath('//div[@class="K9wGie"]')

    if rating_container:
        rating_container = rating_container[0]

        rating = rating_container[0].text.strip()
        votes = rating_container[2].findtext('span[2]').strip()

    detail = {}

    rating_detail_container = response_parsed.xpath('//div[@class="VEF2C"]')

    if rating_detail_container:
        rating_detail_container = rating_detail_container[0]

        for stars_count, rating_bar in enumerate(reversed(rating_detail_container.xpath('//span[contains(@class, "L2o20d")]')), start=1):
            styles = _parse_styles(rating_bar.get('style'))

            detail[stars_count] = styles.get('width').rstrip('%')

    version = None

    additional_info_container = response_parsed.xpath('//div[@class="xyOfqd"]')

    if additional_info_container:
        additional_info_container = additional_info_container[0]

        version = additional_info_container.findtext('div[@class="hAyfc"][4]/span/div/span')

    return {
        'rating': rating,
        'votes': votes,
        'detail': detail,
        'version': version
    }


def _fetch_itunes_app_info(id, country):
    params = {
        'l': 'en',
        'platform': 'iphone'
    }

    response_parsed = _fetch_and_parse(ITUNES_APP_URL.format(id=id, country=country), params=params)

    rating = None
    votes = None

    rating_container = response_parsed.xpath('//div[contains(@class, "we-customer-ratings__stats")]')

    if rating_container:
        rating_container = rating_container[0]

        rating = rating_container[0].findtext('span').strip()
        votes = rating_container[1].text.replace('Ratings', '').strip()

    detail = {}

    rating_detail_container = response_parsed.xpath('//figure[@class="we-star-bar-graph"]')

    if rating_detail_container:
        rating_detail_container = rating_detail_container[0]

        for stars_count, rating_bar in enumerate(reversed(rating_detail_container.xpath('//div[@class="we-star-bar-graph__bar__foreground-bar"]')), start=1):
            styles = _parse_styles(rating_bar.get('style'))

            detail[stars_count] = styles.get('width').rstrip('%')

    version = None

    version_container = response_parsed.xpath('//p[contains(@class, "whats-new__latest__version")]')

    if version_container:
        version = version_container[0].text.replace('Version', '').strip()

    return {
        'rating': rating,
        'votes': votes,
        'detail': detail,
        'version': version
    }


def _parse_styles(styles):
    return {entry[0]: entry[1] for entry in [[kv.strip() for kv in style.strip().split(':', maxsplit=1)] for style in filter(None, styles.strip().split(';'))]}


def fetch_app_info(store, id, country=None):
    if store == Stores.GOOGLE_PLAY:
        return _fetch_google_play_app_info(id)
    elif store == Stores.ITUNES:
        return _fetch_itunes_app_info(id, country)
    else:
        raise ValueError()


def fetch_all_pepper_apps_info():
    ret = {}

    for site_id, site_info in app.config['PEPPERS'].items():
        ret[site_id] = {}

        for store, store_info in site_info['stores'].items():
            try:
                ret[site_id][store.value] = fetch_app_info(store, **store_info)
            except Exception as e:
                ret[site_id][store.value] = str(e)

    return ret


def get_site_logo_url(site_homepage):
    return site_homepage.replace('www.', 'assets.').replace('nl.', 'assets.') + 'assets/img/brandmark.png'
