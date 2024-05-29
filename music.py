class Music:

    def __init__(self,rank,song_name,singer,last_week,peak_position,weeks_on_chart) -> None:
        self.rank = rank
        self.song_name = song_name
        self.singer = singer
        self.last_week = last_week
        self.peak_position = peak_position
        self.weeks_on_chart = weeks_on_chart
    
    def toDBCollection(self):
        return{
            'Rank': self.rank,
            'Song Name': self.song_name,
            'Singer': self.singer,
            'Last Week': self.last_week,
            'Peak Position': self.peak_position,
            'Weeks on Chart':self.weeks_on_chart
        }