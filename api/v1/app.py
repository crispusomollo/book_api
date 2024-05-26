# book_api/app.py

from flask import Flask
from api.v1.views.books import books_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(books_bp, url_prefix='/api/v1')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port="5000", debug=True)

