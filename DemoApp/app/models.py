from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from DemoApp.app import app, db
from sqlalchemy.orm import relationship


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    avatar = Column(String(255), default='https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1')

    def __str__(self):
        return self.name

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    product = relationship("Product", backref="category", lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    image = Column(String(255))
    price = Column(Float)
    catagory_Id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        # db.drop_all()
        db.create_all()
        import hashlib
        u = User(name = "Admin", username = "admin", password = str(hashlib.md5('123456'.encode('utf-8')).hexdigest()))
        db.session.add(u)
        db.session.commit()

        #
        # c1 = Category(name = "Samsung")
        # c2 = Category(name = "Apple")
        # c3 = Category(name="China")
        # db.session.add_all([c1,c2,c3])
        # db.session.commit()

        #
        # p1 = Product(name = "Galaxy Ultra",image = "https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1",price = 20,catagory_Id = 1)
        # p2 = Product(name = "Galaxy S8",image = "https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1",price = 30,catagory_Id = 1)
        # p3 = Product(name = "Iphone 15Pro",image = "https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1",price = 40,catagory_Id = 2)
        # p4 = Product(name = "Redmi 8",image = "https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1",price = 10,catagory_Id = 3)
        # p5 = Product(name = "Iphone X",image = "https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1",price = 5,catagory_Id = 2)
        # p6 = Product(name = "Redmi 6",image = "https://th.bing.com/th/id/OIP.sG3uELc_wRRSpvGfwsvnPQHaHa?pid=ImgDet&rs=1",price = 4,catagory_Id = 3)
        #
        # db.session.add_all([p1,p2,p3,p4,p5,p6])
        # db.session.commit()
