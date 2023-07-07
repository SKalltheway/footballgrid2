from flask import Blueprint, render_template, request, send_from_directory
import pandas as pd
import os

views = Blueprint(__name__, "views")

@views.route('/templates/static\autocomplete.js')
def serve_static(filename):
    return views.send_static_file("autocomplete.js")
 
@views.route('/all_NFL_players_ever_real.csv')
def serve_csv():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(root_dir, 'all_NFL_players_ever_real.csv')


@views.route("/", methods=["POST", "GET"])
def home():
    
    #return render_template('index.html', team = "Colts")
    return render_template('temp.html')