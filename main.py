from flask import Flask, render_template
from game_of_life import GameOfLife
import webbrowser

app = Flask(__name__)


@app.route("/")
def index():
    GameOfLife(25, 25)
    return render_template("index.html")


@app.route("/live")
def live():
    new_game = GameOfLife
    new_game.form_new_generation
    return render_template("live.html", new_game=new_game)


if __name__ == "__main__":
    webbrowser.open_new_tab("http://127.0.0.1:5000")
    app.run(debug=True)