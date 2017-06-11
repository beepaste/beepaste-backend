import time


# TODO MUST clean up

class _Missing(object):
    """
    Copyright (c) 2015 by Armin Ronacher and contributors.  See AUTHORS
    in FLASK_LICENSE for more details.
    """
    def __repr__(self):
        return 'no value'

    def __reduce__(self):
        return '_missing'


_missing = _Missing()


class UpdateDictMixin(object):
    """
    Copyright (c) 2015 by Armin Ronacher and contributors.  See AUTHORS
    in FLASK_LICENSE for more details.
    """

    on_update = None

    def calls_update(name):
        def oncall(self, *args, **kw):
            rv = getattr(super(UpdateDictMixin, self), name)(*args, **kw)
            if self.on_update is not None:
                self.on_update(self)
            return rv
        oncall.__name__ = name
        return oncall

    def setdefault(self, key, default=None):
        modified = key not in self
        rv = super(UpdateDictMixin, self).setdefault(key, default)
        if modified and self.on_update is not None:
            self.on_update(self)
        return rv

    def pop(self, key, default=_missing):
        modified = key in self
        if default is _missing:
            rv = super(UpdateDictMixin, self).pop(key)
        else:
            rv = super(UpdateDictMixin, self).pop(key, default)
        if modified and self.on_update is not None:
            self.on_update(self)
        return rv

    __setitem__ = calls_update('__setitem__')
    __delitem__ = calls_update('__delitem__')
    clear = calls_update('clear')
    popitem = calls_update('popitem')
    update = calls_update('update')
    del calls_update


class CallbackDict(UpdateDictMixin, dict):

    """A dict that calls a function passed every time something is changed.
    The function is passed the dict instance.
    Copyright (c) 2015 by Armin Ronacher and contributors.  See AUTHORS
    in FLASK_LICENSE for more details.
    """

    def __init__(self, initial=None, on_update=None):
        dict.__init__(self, initial or ())
        self.on_update = on_update

    def __repr__(self):
        return '<%s %s>' % (
            self.__class__.__name__,
            dict.__repr__(self)
        )


class SessionDict(CallbackDict):
    def __init__(self, initial=None, sid=None):
        def on_update(self):
            self.modified = True

        super().__init__(initial, on_update)

        self.sid = sid
        self.modified = False


def _calculate_expires(expiry):
    expires = time.time() + expiry
    return time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime(expires))


class BaseSessionInterface:
    def _delete_cookie(self, request, response):
        response.cookies[self.cookie_name] = request['session'].sid
        response.cookies[self.cookie_name]['expires'] = 0
        response.cookies[self.cookie_name]['max-age'] = 0

    def _set_cookie_expiration(self, request, response):
        response.cookies[self.cookie_name] = request['session'].sid
        response.cookies[self.cookie_name]['expires'] = _calculate_expires(self.expiry)
        response.cookies[self.cookie_name]['max-age'] = self.expiry
        response.cookies[self.cookie_name]['httponly'] = self.httponly

        if self.domain:
            response.cookies[self.cookie_name]['domain'] = self.domain
