from werkzeug.middleware.dispatcher import DispatcherMiddleware
from app_1 import app1
from app_2 import app2
from flask import Flask

#unused base app
base_app = Flask(__name__)

app = DispatcherMiddleware(base_app, {
    '/app1': app1.server,
    '/app2':  app1.server,
})

