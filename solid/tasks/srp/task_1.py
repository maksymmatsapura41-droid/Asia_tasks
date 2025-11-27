class Movie:
    def __init__(self, title, rating, duration):
        self.title = title
        self.rating = rating
        self.duration = duration

    def play(self):
        print(f"Playing {self.title}")

    def save_to_db(self):
        pass

    def send_notification(self):
        pass
