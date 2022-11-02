# Импорты стандартных модулей
from flask import Flask, render_template, request, json

# Импорты собственных модулей
from dao.posts_dao import PostsDAO
from dao.comments_dao import CommentsDAO

# Импорты блюпринтов
from api.views import api_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# pytest ругается ворнингом на эту 👆🏻 запись конфига. Предлагает "вместо этого
# установить вон то 👇🏻", но я вообще не смог нагуглить что именно имеется ввиду
# хотя и очень старался
# app.json.ensure_ascii
app.register_blueprint(api_blueprint)
posts_dao = PostsDAO('./data/posts.json')
comments_dao = CommentsDAO('./data/comments.json')


@app.route('/')
def page_feed() -> str:
    posts = posts_dao.get_all()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:pk>')
def page_post(pk: int) -> str:
    post = posts_dao.get_by_id(pk)
    comments = comments_dao.select_by_post(pk)
    if post:
        return render_template('post.html', post=post, comments=comments, comments_qty=len(comments))
    else:
        return '404! Такого поста не существует'


@app.route('/user/<user_name>')
def page_user(user_name: str) -> str:
    posts = posts_dao.get_by_user(user_name)
    if posts:
        return render_template('user-feed.html', posts=posts)
    else:
        return '404! Такого пользователя не существует'


@app.route('/search')
def page_search_by_word() -> str:
    search_word = request.args.get('s')
    if search_word:
        posts = posts_dao.get_by_word(search_word)
    else:
        return '404! Запрос не корректный, попробуйте еще 100500 раз'
    return render_template('search.html', posts=posts, posts_qty=len(posts))


@app.errorhandler(404)
def page_not_found(e):
    return "404! Что-то пошло не так и вы зашли куда-то не нуда. Лучше не надо."


@app.errorhandler(500)
def page_not_found(e):
    return "500! Похоже на сервере что-то сломалось или не работает как нужно..."


if __name__ == '__main__':
    app.run()
