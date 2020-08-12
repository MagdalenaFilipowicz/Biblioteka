class Movies:
    def __init__(self, name, year, genre, number_of_plays):
        self.name = name
        self.year = year
        self.genre = genre
        self.number_of_plays = number_of_plays

    def __repr__(self):
        return f"{self.name}, ({self.year}), {self.genre}, {self.number_of_plays}"
   
    def play(self):
        self.number_of_plays = int(self.number_of_plays) + 1
        return self.number_of_plays
        
class Series(Movies):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
    
    def __repr__(self):
        return f"{self.name}, S{self.season:02d}E{self.episode:02d}"

movies_series=[]
movie= Movies(name='Titanic', year='1967',genre='comedy', number_of_plays='67')
serial= Series(name='The Simpsons', year='1957',genre='thriller', number_of_plays='89', episode=5, season=6)
print(movie.play(), serial.play())
print(serial)
movies_series.append(movie)
movies_series.append(serial)
print(movies_series)






