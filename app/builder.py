# -*- coding: utf8 -*-
from flask import Flask
from flask import render_template
import libraries.mongodb as mongodb
from app.libraries import loggerFactory


def createApp(config, url_prefix=None):
    from app.libraries import loggerFactory
    app = Flask(__name__)

    mongodb.setDefaultConfig(config)
    app.config.from_object(config)

    from routes import jobs
    from routes import accounts

    app.register_blueprint(
        jobs.getBlueprint(config), url_prefix=url_prefix)
    app.register_blueprint(
        accounts.getBlueprint(config), url_prefix=url_prefix)

    @app.route('/', methods=['GET'])
    def get():
        return "Welcome to FLJ API END-POINT. At the moment, there\
         is not any documentation. Sorry."
    return app


# def createCeleryApp(config):
#     mongodb.setDefaultConfig(config)
#     celery.setCeleryConfig(config)
#     mailer.setMailerConfig(config)
#     app = celery.getCelery()
#     from livechat.proxies import widgets
#     return app
