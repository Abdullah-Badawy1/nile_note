# import pytest
# from website import create_app

# @pytest.fixture
# def app():
#     app = create_app()
#     app.config.update({
#         "TESTING": True,
#     })
#     yield app

# @pytest.fixture
# def client(app):
#     return app.test_client()

# def test_home_page(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert b"Welcome" in response.data

from questgen import main
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
