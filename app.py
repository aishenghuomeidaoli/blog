# _*_ coding: utf-8 _*_
from blog import create_app

app = create_app()

if __name__ == '__main__':
    host = app.config.get('HOST')
    port = app.config.get('PORT')
    debug = app.config.get('DEBUG')
    app.run(host=host, port=port, debug=debug)
