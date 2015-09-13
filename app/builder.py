# -*- coding: utf8 -*-
from flask import Flask, jsonify
from flask import render_template
import libraries.mongodb as mongodb
from app.libraries import loggerFactory
from app.libraries import celerySetter as celery
from app.libraries import loggerFactory, response
from app.modules.errors import BaseException



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

    @app.errorhandler(BaseException)
    def handle_exceptions(error):
        return jsonify({"status": error.__json__()})

    @app.errorhandler(Exception)
    def handle_exceptions(error):
        loggerFactory.get().error(error, exc_info=True)
        return jsonify({"status": {
            "type": "UncaughtError - " + error.__class__.__name__,
            "code": 500,
            "message": "something went wrong, and a notification about this" +
                    " just sent to the manager."}}), 500

    @app.route('/', methods=['GET'])
    def get():
        return "Welcome to FLJ API END-POINT. At the moment, there\
         is not any documentation. Sorry."
    return app


def createCeleryApp(config):
    mongodb.setDefaultConfig(config)
    celery.setCeleryConfig(config)
    app = celery.getCelery()
    from app.proxies import crawler
    return app
