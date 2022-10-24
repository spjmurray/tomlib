from tomlib.session import SessionManager
from tomlib.features import VLAG

class PluribusAPI():
    session = None
    vlag = None

    def __init__(self, host, username, password):
        self.session = SessionManager(host, username, password)

        self.vlag = VLAG(self.session)
        # ... etc, don't use inheritance it's a pain in the butt
