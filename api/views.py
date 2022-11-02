# Стандартные импорты
from flask import Blueprint, jsonify
import logging

# Импорты собственных модулей
from dao.posts_dao import PostsDAO


api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api')
posts_dao = PostsDAO('./data/posts.json')

# Куча строчек для подключения и настройки логгера. Хорошо бы если бы их как то
# Более компактно написать можно было... Разве что выносить в отдельный файл...
logger_api = logging.getLogger('logger_api')
formatter_api = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler = logging.FileHandler('api.log')
file_handler.setFormatter(formatter_api)
logger_api.addHandler(file_handler)
logger_api.setLevel('INFO')


@api_blueprint.route('/posts')
def api_posts():
    posts = posts_dao.get_all()
    logger_api.info('Запрошены все посты')
    return jsonify(posts)


@api_blueprint.route('/posts/<int:post_id>')
def api_post_by_id(post_id: int):
    logger_api.info(f'Запрошен пост ID:{post_id}')
    post = posts_dao.get_by_id(post_id)
    if post:
        return jsonify(post)
    else:
        logger_api.warning(f'Запрошенный ID:{post_id} не существует')
        return jsonify([{'error': 'такого ID не существует'}])
