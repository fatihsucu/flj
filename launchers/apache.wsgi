import sys
import os


sys.path.insert(
    0,
    os.path.join(os.path.abspath(os.path.dirname(__file__)) + '/../'))


import configs
conf = configs.get()

from app.libraries import loggerFactory
loggerFactory.setConfig(conf, defaultName='')
logger = loggerFactory.get()

from app.builder import createApp
application = createApp(conf)
application.secret_key = conf.SECRET_KEY

# https://github.com/botego/livechat/issues/1247
from launchers import monitor
monitor.start(interval=1.0)

application.run()
