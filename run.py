import webapps.server.app as server

server.app.run(host=server.app.config['HOST'], port=server.app.config['PORT'])
