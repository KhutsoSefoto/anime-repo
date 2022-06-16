from flask import Flask, render_template, request, flash
import pandas as pd
import main
import time
import csv

app = Flask(__name__)
app.secret_key = "mango_645"


@app.route("/hello/")
def index():
    flash("WELCOME TO MY ANIME CORNER!")
    return render_template("index.html")


@app.route("/results/", methods=["POST", "GET"])
def results():
    match = True
    type = str(request.form['type_input']).lower()
    mood = str(request.form['mood_input']).lower()

    if request.method == 'POST':
        types = request.form['type_input']
        moods = request.form['mood_input']
        if not types:
            flash("Anime type is required!")
        elif not moods:
            flash("Anime genre is required!")
        elif not types and not moods:
            flash("Anime type & genre are required!")
        else:
            pass

    timeout = 60
    timeout_start = time.time()
    while(time.time() < timeout_start + timeout):
        if main.find_anime(type, mood) == match:
            break
    file = open("results.csv", "r")
    reader = csv.reader(file)
    anime_info = list(reader)
    anime_img = anime_info[0]
    file.close()

    return render_template("results.html", anime_info=anime_info, anime_img=anime_img)


if __name__ == '__main__':
    app.run(debug=True)
