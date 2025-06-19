from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv(f'.env.{os.getenv("ENV")}')

app = Flask(__name__)
app.config['DEBUG'] = os.getenv('DEBUG', 'False') == 'True'


@app.route('/')
def hello():
    return f"Hello from CI Pipeline! Debug Mode: {app.config['DEBUG']}"


if __name__ == '__main__':
    app.run()
