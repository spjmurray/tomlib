from tomlib.util import FunctionArgs
import tomlib.util.validators as validators

class VLAG:
    session = None

    def __init__(self, session):
        self.session = session

    # Note rather than define a million args in the signature, we have args
    # for required positional parameters, and kwargs for optional ones.
    def create(self, *args, **kwargs):
        parser = FunctionArgs()

        parser.add_positional_argument('name')
        parser.add_positional_argument('port', type=int, validator=validators.valid_port()) # validation of port ranges!
        parser.add_positional_argument('peer_port', path='peer-port', type=int, validator=validators.valid_port()) # non-identity mapped names!

        parser.add_optional_argument('mode', choices=['active-standby', 'active-active']) # enumerations!
        parser.add_optional_argument('lacp_timeout', path='lacp-timeout', choices=['slow', 'fast'])
        parser.add_optional_argument('lacp_mode', path='lacp-mode', choices=['off', 'passive', 'active'])
        parser.add_optional_argument('failover_move_l2', path='failover-move-l2', type=bool, converter=lambda x: str(x).lower()) # use of boolean types, then conversion using a lambda!
        parser.add_optional_argument('lacp_fallback', path='lacp-fallback', choices=['individual', 'bundle'])
        parser.add_optional_argument('lacp_fallback_timeout', path='lacp-fallback-timeout', type=int, validator=validators.bounded_int_inclusive(30, 60), converter=str) # arbitrary range checks then coversion to a string using the builtin constructor!
        parser.add_optional_argument('lacp_port_priority', path='lacp-port-priority', type=int, validator=validators.valid_port(), converter=str)

        return self.session.post('/some/fictional/path', parser.parse(*args, **kwargs))
