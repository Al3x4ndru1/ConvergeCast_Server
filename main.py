from flask import Flask, render_template
from scripts.Backend import create_app
app = Flask(__name__)

app = create_app()

if __name__ == '__main__':
    app.run(host='10.33.16.19', port=5000, debug=True)