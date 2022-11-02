import json


class CommentsDAO:
    def __init__(self, path: str) -> None:
        self.path = path

    def load_all(self) -> list[dict]:
        with open(self.path, 'r') as file:
            json_data = json.load(file)
        return json_data

    def select_by_post(self, post_id) -> list[dict]:
        comments = self.load_all()
        selected_comments = []
        for comment in comments:
            if comment['post_id'] == post_id:
                selected_comments.append(comment)
        return selected_comments
