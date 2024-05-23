from declaratives import *


class movie(Base):
    __tablename__ = 'filmes'
    id = Column(Integer, primary_key=True)
    actor_id = Column(Integer, ForeignKey('atores.id', ondelete='CASCADE'), nullable=False)
    actor = relationship('filmes', backref='atores')

    def __init__(self, **kwargs):
        super(movie, self).__init__(**kwargs)


class actor(Base):
    __tablename__ = 'atores'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, **kwargs):
        super(actor, self).__init__(**kwargs)

