from flask_admin import Admin, BaseView, expose
from DemoApp.app import db, app
from models import Product, Category
from flask_admin.contrib.sqla import ModelView


class MyCategory(ModelView):
    column_list = ['id', 'name', 'product']


class MyProduct(ModelView):
    column_list = ['id', 'name', 'category']


class StaticsView(BaseView):
    @expose("/")
    def index(self):
        return self.render('admin/statics.html')


admin = Admin(app=app, name="QUAN LY BAN HANG", template_mode='bootstrap4')
admin.add_view(MyCategory(Category, db.session))
admin.add_view(MyProduct(Product, db.session))
admin.add_view(StaticsView(name = "Thong ke bao cao"))
