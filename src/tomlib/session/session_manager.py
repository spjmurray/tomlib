import requests

class SessionManager:
    # Use pylint :D
    host = None
    username = None
    password = None
    tls = None

    def __init__(self, host, username, password, tls=False):
        self.host = host
        self.username = username
        self.password = password
        self.tls = tls

    # Quick hack that allows you to expose a function as a property,
    # see below, no parentheses!
    @property
    def _scheme(self):
        if self.tls:
            return 'https'
        return 'http'

    def _url(self, path):
        return f'{self._scheme}://{self.host}{path}'

    @property
    def _auth(self):
        return (self.username, self.password)

    def post(self, path, body=None, headers=None):
        # Automatic encoding and Content-Type headers!
        r = requests.post(self._url(path), json=body, auth=self._auth, headers=headers)

        # Error checking!
        if r.status_code / 100 != 2:
                raise RuntimeError('ermahgerd')

        # Built in!
        return r.json()
