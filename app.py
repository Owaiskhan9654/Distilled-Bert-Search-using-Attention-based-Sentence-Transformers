from flask import Flask, render_template, request
from ranking import rank


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search/results', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["input"]
    articlelink,score=rank(search_term)
    return render_template('results.html', res=articlelink ,score=score)

if __name__ == '__main__':
    app.run(debug=True)