from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    # Name
    __tablename__ = 'user'

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class FoodCategory(Base):
    __tablename__ = 'foodcategory'

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    # foreign keys
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class FoodItem(Base):
    __tablename__ = 'fooditem'

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(8))

    # foreign keys
    foodcategory_id = Column(Integer, ForeignKey('foodcategory.id'))
    foodcategory = relationship(FoodCategory)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
        }


#engine = create_engine('postgresql://catalog:password@localhost/catalog')
engine = create_engine('sqlite:///grocerwithusers.db')

Base.metadata.create_all(engine)
