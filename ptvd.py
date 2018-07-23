from flask_assets import Environment, Bundle
from collections import OrderedDict
from flask_caching import Cache
from flask import Flask


# -----------------------------------------------------------
# Boot


app = Flask(__name__, static_url_path='')
app.config.from_pyfile('config.py')

app.config['CACHE_TYPE'] = 'filesystem'
app.config['CACHE_DIR'] = 'storage/cache'

cache = Cache(app)
assets = Environment(app)

assets.cache = 'storage/webassets-cache/'

assets.register('js_app', Bundle('js/app.js', filters='jsmin', output='js/app.min.js'))
assets.register('css_app', Bundle('css/app.css', filters='cssutils', output='css/app.min.css'))

# -----------------------------------------------------------
# After-init imports


import routes
import commands
import services

app.jinja_env.globals.update(
    get_site_logo_url=services.get_site_logo_url
)

app.config['PEPPERS'] = OrderedDict([
    ('dealabs', {
        'name': 'Dealabs 🤘',
        'homepage': 'https://www.dealabs.com/',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'com.dealabs.apps.android'},
            services.Stores.ITUNES: {'id': '914813032', 'country': 'fr'}
        }
    }),
    ('mydealz', {
        'name': 'MyDealz',
        'homepage': 'https://www.mydealz.de/',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'com.tippingcanoe.mydealz'},
            services.Stores.ITUNES: {'id': '463557271', 'country': 'de'}
        }
    }),
    ('hotukdeals', {
        'name': 'HotUKDeals',
        'homepage': 'https://www.hotukdeals.com/',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'com.tippingcanoe.hukd'},
            services.Stores.ITUNES: {'id': '570702323', 'country': 'gb'}
        }
    }),
    ('promodescuentos', {
        'name': 'PromoDescuentos',
        'homepage': 'https://www.promodescuentos.com/',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'com.tippingcanoe.promodescuentos'},
            services.Stores.ITUNES: {'id': '889069686', 'country': 'mx'}
        }
    }),
    ('pelando-br', {
        'name': 'Pelando BR',
        'homepage': 'https://www.pelando.com.br/',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'com.tippingcanoe.pelando'},
            services.Stores.ITUNES: {'id': '1045614200', 'country': 'br'}
        }
    }),
    ('chollometro', {
        'name': 'Chollometro',
        'homepage': 'https://www.chollometro.com/',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'com.chollometro'},
            services.Stores.ITUNES: {'id': '1312754670', 'country': 'es'}
        }
    }),
    ('pelando-sg', {
        'name': 'Pelando SG',
        'homepage': 'https://www.pelando.sg/',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'sg.pelando.apps.android'},
            services.Stores.ITUNES: {'id': '1210638782', 'country': 'sg'}
        }
    }),
    ('pepper-kr', {
        'name': 'Pepper KR',
        'homepage': 'https://www.pepper.co.kr/',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'com.tippingcanoe.pepperkr'},
            services.Stores.ITUNES: {'id': '923455187', 'country': 'kr'}
        }
    }),
    ('buenosdeals', {
        'name': 'BuenosDeals',
        'homepage': 'https://www.buenosdeals.com/',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'com.tippingcanoe.buenosdeals'},
            services.Stores.ITUNES: {'id': '1024798115', 'country': 'us'}
        }
    }),
    ('pepper-nl', {
        'name': 'Pepper NL',
        'homepage': 'https://nl.pepper.com/',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'com.tippingcanoe.peppernl'},
            services.Stores.ITUNES: {'id': '923455114', 'country': 'nl'}
        }
    }),
    ('preisjaeger', {
        'name': 'Preisjäger',
        'homepage': 'https://www.preisjaeger.at/',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'com.preisjaeger'},
            services.Stores.ITUNES: {'id': '632117774', 'country': 'at'}
        }
    }),
    ('pepper-pl', {
        'name': 'Pepper PL',
        'homepage': 'https://www.pepper.pl/',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'com.tippingcanoe.pepperpl'},
            services.Stores.ITUNES: {'id': '923455061', 'country': 'pl'}
        }
    }),
    ('pepper-ru', {
        'name': 'Pepper RU',
        'homepage': 'https://www.pepper.ru/',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'ru.pepper'},
            services.Stores.ITUNES: {'id': '1341584717', 'country': 'ru'}
        }
    }),
    ('desidime', {
        'name': 'DesiDime',
        'homepage': 'https://www.desidime.com/',
        'logo': 'https://cdn0.desidime.com/topics/photos/874813/small/DD-store-icon.png',
        'stores': {
            services.Stores.GOOGLE_PLAY: {'id': 'app.desidime'},
            services.Stores.ITUNES: {'id': '1319895803', 'country': 'mz'}
        }
    }),
])
