from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Campuses(Base):
    __tablename__ = "campuses"

    id = Column(Integer, primary_key=True)
    name = Column(String(52), nullable=False)
    slug = Column(String(52), unique=True, nullable=False)

    def __repr__(self):
        return f"<Campuses(name='{self.name}', slug='{self.slug}')>"


class Tribes(Base):
    __tablename__ = "tribes"

    id = Column(Integer, primary_key=True)
    name = Column(String(21), nullable=False)
    slug = Column(String(21), unique=True, nullable=False)
    campus_id = Column(Integer, ForeignKey("campuses.id"), nullable=False)
    master = Column(String(52), nullable=False)
    parallel = Column(String(21), nullable=False)
    visibility = Column(Boolean, default=False)
    capacity = Column(Integer, default=0)
    curr_points = Column(Integer, default=0)
    prev_points = Column(Integer, default=0)

    campus = relationship("Campuses", back_populates="tribes")

    def __repr__(self):
        return f"<Tribes(name='{self.name}', slug='{self.slug}')>"


class Tournaments(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    campus_id = Column(Integer, ForeignKey("campuses.id"), nullable=False)
    tribe_id = Column(Integer, ForeignKey("tribes.id"), nullable=False)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)

    campus = relationship("Campuses", back_populates="tournaments")
    tribe = relationship("Tribes", back_populates="tournaments")

    def __repr__(self):
        return (
            f"<Tournaments(name='{self.name}', start='{self.start}', end='{self.end}')>"
        )


class Peers(Base):
    __tablename__ = "peers"

    id = Column(Integer, primary_key=True)
    name = Column(String(21), nullable=False)
    campus_id = Column(Integer, ForeignKey("campuses.id"), nullable=False)
    curr_tribe_id = Column(Integer, ForeignKey("tribes.id"), default=1)
    prev_tribe_id = Column(
        Integer, ForeignKey("tribes.id"), nullable=True, default=None
    )
    level = Column(Integer, nullable=False)
    wave = Column(String(21), nullable=False)
    curr_points = Column(Integer, default=0)
    prev_points = Column(Integer, default=0)

    campus = relationship("Campuses", back_populates="peers")
    curr_tribe = relationship("Tribes", foreign_keys=[curr_tribe_id])
    prev_tribe = relationship("Tribes", foreign_keys=[prev_tribe_id])

    def __repr__(self):
        return f"<Peers(name='{self.name}', level='{self.level}', wave='{self.wave}')>"


Campuses.tribes = relationship("Tribes", order_by=Tribes.id, back_populates="campus")
Campuses.tournaments = relationship(
    "Tournaments", order_by=Tournaments.id, back_populates="campus"
)
Campuses.peers = relationship("Peers", order_by=Peers.id, back_populates="campus")
Tribes.tournaments = relationship(
    "Tournaments", order_by=Tournaments.id, back_populates="tribe"
)

from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///../django_app/db.sqlite3"
)  # замените на ваш URL базы данных
Base.metadata.create_all(engine)
