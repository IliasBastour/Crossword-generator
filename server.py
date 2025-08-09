from flask import Flask, request, jsonify, render_template
from wordsearch import WordSearch

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    words = request.form.get("words")
    width = int(request.form.get("width"))
    height = int(request.form.get("height"))
    try:
        ws = WordSearch(words, width=width, height=height)
        ws.generate()

        grid = ws.get_grid_as_list()

        return render_template("crossword.html", grid=grid)
    except ValueError as e:
        error_msg = str(e)
        return render_template(
            "index.html", 
            error=error_msg, 
            previous_words=words,
            previous_width=width,
            previous_height=height
        )

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")