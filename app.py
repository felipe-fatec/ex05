from prometheus_client import Summary
import random
import time
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from prometheus_client import Info
import logging
from flask import Flask
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
app = Flask(__name__)

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

i = Info('my_build_version', 'Description of info')
i.info({'version': '0.0.1', 'buildhost': 'felipe@server'})

# Métricas
# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

@app.route('/')
def hello_world():
    logging.info('Este é um log simples.')
    process_request(random.random())
    return 'Hello, World!'

TASK1_TIME = Summary('task1_processing_seconds', 'Time spent processing request')

@TASK1_TIME.time()
def slow():
    """A dummy function that takes some time."""
    time.sleep(30)
   

@app.route('/slow')
def gera_alerta():
    logging.info('Vai Gerar um alerta')
    slow()
    return 'slow'
