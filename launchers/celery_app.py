# -*- coding: utf8 -*-
import sys
import os

sys.path.insert(
    0,
    os.path.join(os.path.abspath(os.path.dirname(__file__)) + '/../'))

import configs
conf = configs.get()
from app.libraries import loggerFactory
# loggerFactory.setConfig(conf, defaultName='celeryWorker')
# logger = loggerFactory.get()

# logger.info('----------------------------------------')
# logger.info('-------- STARTING CELERY WORKERS')
# logger.info('-------- Config: {}'.format(conf.NAME))
# logger.info('----------------------------------------')

from app.builder import createCeleryApp

app = createCeleryApp(conf)
