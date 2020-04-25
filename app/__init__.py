from flask import Flask

app = Flask(__name__)

from site.controllers import default
