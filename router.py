from werkzeug.middleware.dispatcher import DispatcherMiddleware
from my_app import app1, app2
from flask import Flask

base_app = Flask(__name__)

app = DispatcherMiddleware(base_app, {
    '/app1': app1.server,
    '/app2':  app1.server,
})

print(app)