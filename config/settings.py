import os

class Config:
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGO_DB', 'bookapi'),
        'host': os.getenv('MONGO_HOST', 'localhost'),
        'port': int(os.getenv('MONGO_PORT', 27017))
    }

class TestConfig(Config):
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'testdatabase',
        'host': 'localhost',
        'port': 27017
    }


