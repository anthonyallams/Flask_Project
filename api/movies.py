class Movie():
    __table__ = 'movies'
    columns = ['id','movieid','title','genres']
    
    def __init__(self,values):
        self.__dict__ = dict(zip(self.columns, values))