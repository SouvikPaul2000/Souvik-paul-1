from flask import Flask, request, jsonify


app = Flask(__name__)


from src import routes