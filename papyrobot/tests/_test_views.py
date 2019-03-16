import pytest

from papyrobot import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_example(client):
    response = client.get("/")
    assert response.status_code == 200

def test_ajax_no_response(client):
    response = client.get("/ajax?question=ggg")
    assert response.status_code == 200

def test_ajax_response(client):
    response = client.get("/ajax?question=Openclassrooms")
    assert response.status_code == 200

def test_ajax_response_wiki_second(client):
    response = client.get("/ajax?question=zone%2051")
    assert response.status_code == 200