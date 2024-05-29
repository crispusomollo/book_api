# book_api/app.py

from flask import Flask
from config.settings import Config
from models.user import mongo
from api.v1.views.users import user_bp
from api.v1.views.books import book_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)

    app.register_blueprint(user_bp, url_prefix='/api/v1')
    app.register_blueprint(book_bp, url_prefix='/api/v1')

    return app

if __name__ == "__main__":
    app = create_app()
<<<<<<< HEAD
    app.run(host="0.0.0.0", port="5003", debug=True)
=======
    app.run(debug=True)
>>>>>>> d479d4d7100abdf1f8b85101bd8786ce772b6b61

