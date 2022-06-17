from flask import Flask, render_template, request, flash, session
import pandas as pd
import main
from forms import Search
import time
import csv

app = Flask(__name__)
app.secret_key = "mango_645"


@app.route('/')
@app.route("/hello/", methods=["POST", "GET"])
def index():
    form = Search()
    if form.validate_on_submit():
        type = str(form.type.data).lower()
        mood = str(form.mood.data).lower()
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(err_msg)
    return render_template("index.html", form=form)


@app.route("/results/", methods=["POST", "GET"])
def results():
    match = True
    type = str(request.form['type']).lower()
    mood = str(request.form['mood']).lower()

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
