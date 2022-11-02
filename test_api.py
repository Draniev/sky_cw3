import pytest
from app import app


def test_app():
    response = app.test_client().get('/')
    assert response.status_code == 200, 'Похоже сервер не работает'


def test_api_posts():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200, 'Похоже сервер не работает'
    assert type(response.json) == list, 'Похоже что возвращается не верный тип данных'
    for post in response.json:
        post_keys = post.keys()
        for key in ('poster_name', 'poster_avatar', 'pic', 'content', 'pk'):
            assert key in post_keys, 'Ну штош, давайте проверим каждый ключ в каждом посте :)'


def test_api_post():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200, "Похоже сервер не работает (не выдаёт ответ 200)"
    assert type(response.json) == dict, 'Получили не верный тип данных'

    json_keys = response.json.keys()
    for key in ('poster_name', 'poster_avatar', 'pic', 'content', 'pk'):
        assert key in json_keys, 'Кажется набор ключей не совсем верный'
