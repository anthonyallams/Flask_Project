class Rating():
    __table__ = 'ratings'
    columns = ['id','userid','movieid','rating']

    
    def __init__(self,values) -> None:
        self.__dict__ = dict(zip(self.columns, values))