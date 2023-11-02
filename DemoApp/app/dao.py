from models import Products, Category

def load_nav():
    return Category.query.all()

def load_categories(kw):
    products = Products.query
    if kw:
        products = products.filter(Products.name.contains(kw))
    return products