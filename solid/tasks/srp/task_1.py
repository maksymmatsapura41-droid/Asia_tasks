class Movie:
    def __init__(self, title, rating, duration):
        self.title = title
        self.rating = rating
        self.duration = duration

class MoviePlay:
    @staticmethod
    def play(movie):
        print(f"Playing {movie.title}")

class MovieSaver:
    @staticmethod
    def save_to_db(movie):
        print(f'saving {movie.title} to local storage')

class MovieNotification:
    @staticmethod
    def send_notification(movie):
        print(f'{movie.title} is released')

class MovieManager(MovieSaver, MovieNotification):
    def __init__(self):
        self.movie_player = MoviePlay()


movie1 = Movie('Movie1', 8.0, 90)

movie_manager = MovieManager()
# movie_manager.save_to_db(movie1)
# movie_manager.send_notification(movie1)
movie_manager.movie_player.play(movie1)

    

