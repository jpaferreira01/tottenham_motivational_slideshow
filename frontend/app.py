from flask import Flask, render_template
from title_message import get_title_message

app = Flask(__name__)

@app.route('/')
def home():
    message = get_title_message()
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)