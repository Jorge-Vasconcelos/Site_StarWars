from flask import Flask

app = Flask(__name__)

from models.api_endpoints import *
from controllers.views import *

if __name__ == '__main__':
    app.run(debug=True)
