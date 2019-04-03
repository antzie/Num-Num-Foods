#!/usr/bin/env python2
# Version 3. 12-11-2018
# Added User Capability
# Added Dummy User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, FoodCategory, FoodItem, User

#engine = create_engine('postgresql://catalog:password@localhost/catalog')
engine = create_engine('sqlite:///grocerwithusers.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def deleteFoodItem(category_id, food_id):
    '''Deletes an item of food.
    '''
    deleted_food = session.query(FoodItem).filter_by(id=food_id).one()
    other_categories = session.query(FoodCategory).filter(
        FoodCategory.id != category_id).all()
    category = session.query(FoodCategory).filter_by(id=category_id).one()
    owner = getUserInfo(category.user_id)

    if request.method == 'POST':
        session.delete(deleted_food)
        session.commit()
        flash("Food item: " + deleted_food.name + " deleted!")
        return redirect(
            url_for(
                'showCategoryFood',
                category_id=deleted_food.foodcategory_id))


"""
# Dummy Test User
User1 = User(name="Cibicida",
             email="botBotBOT@email.com",
             picture="/static/css/hqdefault.jpg")
session.add(User1)
session.commit()
"""

# Foods for Category 'Vegetables'
"""
# Foods for Category 'Chocolate'
foodcategory2 = FoodCategory(name="Chocolate",
                             user_id=1)

session.add(foodcategory2)
session.commit()
"""

for row in session.query(User, User.name).all():
  print(row.User, row.name)

for category in session.query(FoodCategory).all():
  print category, category.name, category.image

for category in session.query(FoodCategory).filter_by(name='Dairy Products').all():
  print category.name
  print category.image
  # The below line updates the DB. 
  category.image = "https://raw.githubusercontent.com/antzie/Calla-Grocer-Catalogue/master/static/css/dairy_products.jpg"
# This line commits changes to the DB
#session.commit()