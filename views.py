from flask import Blueprint, render_template, request
import pandas as pd
from csv import DictReader

views = Blueprint(__name__, "views")
with open("all_NFL_players_ever.csv") as f:
    player_names = [row["Player"] for row in DictReader(f)]



@views.route("/", methods=["POST", "GET"])
def home():
    
    #return render_template('index.html', team = "Colts")
    return render_template('search.html', playernames = player_names)