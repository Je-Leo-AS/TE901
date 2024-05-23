from declaratives import *

class actor(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    def __init__(self, **kwargs):
        super(actor, self).__init__(**kwargs)



class movieActors(Base):
    __tablename__ = 'MovieActors'
    id = Column(Integer, primary_key=True)
    actor_id = Column(Integer, ForeignKey('actors.id', ondelete='CASCADE'), nullable=False)
    movie_id = Column(Integer, ForeignKey('movie.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, **kwargs):
        super(actor, self).__init__(**kwargs)
    
class movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    studio = Column(String)

    def __init__(self, **kwargs):
        super(movie, self).__init__(**kwargs)

class movieReviewList(Base):
    __tablename__ = 'movieReviewList'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movie.id', ondelete='CASCADE'), nullable=False)
    reviewID = Column(String)

    def __init__(self, **kwargs):
        super(movieReviewList, self).__init__(**kwargs)

class movieDirectors(Base):
    __tablename__ = 'movieDirectors'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movie.id', ondelete='CASCADE'), nullable=False)
    directors_id = Column(Integer, ForeignKey('directors.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, **kwargs):
        super(movieDirectors, self).__init__(**kwargs)

class director(Base):
    __tablename__ = 'directors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, **kwargs):
        super(director, self).__init__(**kwargs)

class movieGeneres(Base):
    __tablename__ = 'movieGeneres'
    id = Column(Integer, primary_key=True)
    genere_id = Column(Integer, ForeignKey('Genere.id', ondelete='CASCADE'), nullable=False)
    movie_id = Column(Integer, ForeignKey('movie.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, **kwargs):
        super(movieGeneres, self).__init__(**kwargs)

class Genere(Base):
    __tablename__ = 'Genere'
    id = Column(Integer, primary_key=True)
    genere_id = Column(Integer, ForeignKey('directors.id', ondelete='CASCADE'), nullable=False)
    name = Column(String)

    def __init__(self, **kwargs):
        super(Genere, self).__init__(**kwargs)

class MovieSessions(Base):
    __tablename__ = 'MovieSessions'
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('sessions.id', ondelete='CASCADE'), nullable=False)
    movie_id = Column(Integer, ForeignKey('movie.id', ondelete='CASCADE'), nullable=False)
    def __init__(self, **kwargs):
        super(MovieSessions, self).__init__(**kwargs)

class session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    session_id = Column(DateTime,nullable=False)
    movie_id = Column(String, nullable=False)
    def __init__(self, **kwargs):
        super(session, self).__init__(**kwargs)

class sessionClient(Base):
    __tablename__ = 'sessionClients'
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('sessions.id', ondelete='CASCADE'), nullable=False)
    movie_id = Column(String, nullable=False)
    def __init__(self, **kwargs):
        super(sessionClient, self).__init__(**kwargs)

class client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    def __init__(self, **kwargs):
        super(client, self).__init__(**kwargs)

class sessionReviewList(Base):
    __tablename__ = 'sessionReviewList'
    id = Column(Integer, primary_key=True)
    review_id = Column(Integer, ForeignKey('sessionReview.id', ondelete='CASCADE'), nullable=False)
    def __init__(self, **kwargs):
        super(sessionReviewList, self).__init__(**kwargs)

class sessionReview(Base):
    __tablename__ = 'sessionReview'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id', ondelete='CASCADE'), nullable=False)
    rating = Column(String, nullable=False)
    review = Column(String, nullable=False)
    def __init__(self, **kwargs):
        super(sessionReview, self).__init__(**kwargs)