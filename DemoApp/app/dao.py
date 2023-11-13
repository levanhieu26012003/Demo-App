from models import Product, Category, User

def load_nav():
    return Category.query.all()

def load_categories(kw):
    products = Product.query
    if kw:
        products = products.filter(Product.name.contains(kw))
    return products


def get_user_by_id(user_id):
    return User.query.get(user_id)