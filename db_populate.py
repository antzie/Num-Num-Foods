#!/usr/bin/env python2
# Version 3. 12-11-2018
# Added User Capability
# Added Dummy User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, FoodCategory, FoodItem, User

engine = create_engine('sqlite:///grocerwithusers.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Dummy Test User
User1 = User(name="Cibicida",
             email="botBotBOT@email.com",
             picture="/static/css/hqdefault.jpg")
session.add(User1)
session.commit()


# Foods for Category 'Vegetables'
foodcategory1 = FoodCategory(name="Vegetables",
                             user_id=1)

session.add(foodcategory1)
session.commit()

FoodItem1 = FoodItem(
    name="Potato",
    description=(
        "A healthy root vegetable that is "
         + "best turned into unhealthy chips"),
    price="$2",
    foodcategory=foodcategory1,
    user_id=1)

FoodItem2 = FoodItem(
    name="Lettuce",
    description=(
        "A green, tasteless vegetable that is an unnecesssary"
        + " ingredient in burgers but is the primary ingredient"
        + " in salads "),
    price="$3",
    foodcategory=foodcategory1,
    user_id=1
)

FoodItem3 = FoodItem(
    name="Kale",
    description=(
         "A dark-green leafy vegetable that is supposed to be "
        + " good for you and, naturally, tastes awful."),
    price="$5",
    foodcategory=foodcategory1,
    user_id=1)

FoodItems_list = [FoodItem1, FoodItem2, FoodItem3]
for Item in FoodItems_list:
    session.add(Item)
    session.commit()

print 'Catgory1: Vegetables successfully populated'


# Foods for Category 'Chocolate'
foodcategory2 = FoodCategory(name="Chocolate",
                             user_id=1)

session.add(foodcategory2)
session.commit()

FoodItem1 = FoodItem(name="Milk Chocolate",
                     description="The elixir of life.",
                     price="$5",
                     foodcategory=foodcategory2,
                     user_id=1
                     )

FoodItem2 = FoodItem(
    name="Dark Chocolate",
    description=(
        "Supposed to be better for your health than milk chocolate."
        + " Who cares. It's still chocolate. "
          + "60"
          + '%'
        + " cocoa"),
    price="$5.50",
    foodcategory=foodcategory2,
    user_id=1)

FoodItem3 = FoodItem(
    name="White Chocolate",
    description=(
        "Chocolate with the lowest percentage of cocoa and"
        + " the highest percentage of milk. But it's still"
        + " got chocolate in the title"),
    price="$5",
    foodcategory=foodcategory2,
    user_id=1)


FoodItems_list = [FoodItem1, FoodItem2, FoodItem3]
for Item in FoodItems_list:
    session.add(Item)
    session.commit()

print 'Catgory2: Chocolate successfully populated'


# Foods for Category 'Dairy'

foodcategory3 = FoodCategory(name="Dairy Products",
                             user_id=1)

session.add(foodcategory3)
session.commit()


FoodItem1 = FoodItem(
    name="Milk",
    description=(
        "Self-explanatory. Mostly needed for coffee "
         + " i.e. Lattes, Cappucinos etc. "),
    price="$5",
    foodcategory=foodcategory3,
    user_id=1)

FoodItem2 = FoodItem(
    name="Cheddar Cheese",
    description="A necessary ingredient for some burgers.",
    price="$5.50",
    foodcategory=foodcategory3,
    user_id=1
)

FoodItem3 = FoodItem(
    name="Blue Veined Cheese",
    description=(
        "Cheese that has been carefully 'aged' i.e. euphemism for moldy."),
    price="$5",
    foodcategory=foodcategory3,
    user_id=1)


FoodItems_list = [FoodItem1, FoodItem2, FoodItem3]
for Item in FoodItems_list:
    session.add(Item)
    session.commit()


print 'Catgory3: Dairy successfully populated'


print "Committed items to database"
