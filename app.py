from flask import Flask, render_template, request
from findwords import find_difficult_words

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    difficult_words = []
    if request.method == 'POST':
        text = request.form['text']
        if text:
            difficult_words = find_difficult_words(text)

    return render_template("index.html", difficult_words=difficult_words)

if __name__ == "__main__":
    app.run(debug=True)
