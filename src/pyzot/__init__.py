from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pyzot.models import initialize_sql


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.scan('pyzot.models')
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    return config.make_wsgi_app()
