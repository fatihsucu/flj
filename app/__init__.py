# -*- coding: utf8 -*-

# https://github.com/botego/livechat/issues/471
from json import JSONEncoder


def _default(self, obj):
    return getattr(obj.__class__, "__json__", _default.default)(obj)

# save unmodified default, and replace it
_default.default = JSONEncoder().default
JSONEncoder.default = _default
