from flask import Flask, render_template, request, redirect

from point_table import PointTable

app = Flask(__name__)

point_table = PointTable()


@app.route('/')
def index():
    return render_template("index.html", games=point_table.get_games())


@app.route('/add_game', methods=['POST'])
def add_game():
    try:
        score = request.form.get('score')
        point_table.add_game(score)
        return redirect('/')
    except Exception as err:
        return render_template("index.html", games=point_table.get_games(), error=str(err))


app.run()
