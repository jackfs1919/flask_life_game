from flask import Flask, render_template
import game_of_life
import webbrowser

app = Flask(__name__)


@app.route("/")
def index():
    game_of_life.GameOfLife(25, 25)
    return render_template("index.html")


@app.route("/live")
def live():
    new_game = game_of_life.GameOfLife()
    # if new_game.couter:
    #     new_game.form_new_generation
    # else:
    #     new_game.couter += 1
    new_game.form_new_generation()
    return render_template("live.html", new_game=new_game)


if __name__ == "__main__":
    webbrowser.open_new_tab("http://127.0.0.1:5000")
    app.run(debug=True)