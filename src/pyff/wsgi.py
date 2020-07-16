from wsgiref.simple_server import make_server
from .api import mkapp
from .repo import MDRepository
from .logs import get_log

log = get_log(__name__)

md = MDRepository()
log.debug("before mkapp")
app = mkapp(md=md)
log.debug("after mkapp")

def app_factory(global_config, **local_config):
    print("in app_factory entry")
    log.debug("in app_factory entry")
    local_config['md'] = md
    app = mkapp(global_config, **local_config)
    print("in app_factory exit")
    log.debug("in app_factory exit")
    return app


def server_runner(*args):
    print("in server_runner entry")
    log.debug("in server_runner entry")
    _app = args[0]
    local_config = args[1]
    port = int(local_config.get('bind_address', 8080))
    host = local_config.get('port', '0.0.0.0')
    s = make_server(host, port, _app)
    print("in server_runner before serve_forever")
    log.debug("in server_runner before serve_forever")
    s.serve_forever()
    print("in server_runner exit")
    log.debug("in server_runner exit")


def main():
    print("in main() entry")
    log.debug("in main() entry")
    server_runner(mkapp(md=md), bind_address='0.0.0.0', port=8080)
    log.debug("in main() exit")


if __name__ == '__main__':
    print("__name__ is __main__")
    log.debug("__name__ is __main__")
    main()

