import json


class PostsDAO:
    def __init__(self, path: str) -> None:
        self.path = path

    def load_all(self) -> list[dict]:
        with open(self.path, 'r') as file:
            json_data = json.load(file)
        return json_data

    def get_all(self) -> list[dict]:
        posts = self.load_all()
        return posts

    def get_by_word(self, word: str) -> list[dict]:
        posts = self.load_all()
        chosen_posts = []
        for post in posts:
            if word in post['content']:
                chosen_posts.append(post)
        return chosen_posts

    def get_by_user(self, user_name) -> list[dict]:
        posts = self.load_all()
        user_posts = []
        for post in posts:
            if post['poster_name'] == user_name:
                user_posts.append(post)
        return user_posts

    def get_by_id(self, post_id: int) -> dict | None:
        posts = self.load_all()
        for post in posts:
            if post['pk'] == post_id:
                return post
        return None
