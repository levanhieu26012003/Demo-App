from sqlalchemy import Column, Integer, String, Float, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from DemoApp.app import app, db
from sqlalchemy.orm import relationship
class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    productId = relationship("Products", backref="category", lazy=True)



class Products(db.Model):
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    image = Column(String(255))
    price = Column(Float)
    catagoryId = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == "__main__":
    with app.app_context():
        # c1 = Category(name = "Samsung")
        # c2 = Category(name = "Apple")
        # c3 = Category(name="China")
        # db.session.add_all([c1,c2,c3])
        # db.session.commit()


        c1 = Products(name = "Galaxy Ultra",image = "https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1",price = 20,catagoryId = 1)
        c2 = Products(name = "Galaxy S8",image = "https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1",price = 30,catagoryId = 1)
        c3 = Products(name = "Iphone 15Pro",image = "https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1",price = 40,catagoryId = 2)
        c4 = Products(name = "Redmi 8",image = "https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1",price = 10,catagoryId = 3)
        c5 = Products(name = "Iphone X",image = "https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1",price = 5,catagoryId = 2)
        c6 = Products(name = "Redmi 6",image = "https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1",price = 4,catagoryId = 3)

        db.session.add_all([c1,c2,c3,c4,c5,c6])
        db.session.commit()

        # db.create_all()

