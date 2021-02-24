import os

from dotenv import load_dotenv

from app import create_app

basedir = os.path.abspath(os.path.dirname(__file__))

if os.path.exists(os.path.join(basedir, '.env')):
    load_dotenv(os.path.join(basedir, '.env'))

app = create_app('dev')

if __name__ == '__main__':
    app.run()
