import math

from flask import render_template, request, redirect, session, jsonify
import dao
from DemoApp.app import app, login
from flask_login import login_user


@app.route('/')
def index():
    kw = request.args.get("kw")
    cate = request.args.get("cate_id")
    page = request.args.get("page")

    pagenumber = math.ceil(dao.page_number() / app.config['PAGE_SIZE'] + 1)
    categories = dao.load_catagories()
    products = dao.load_products(kw, cate, page)
    return render_template('index.html', categories=categories, products=products, pagenumber=pagenumber)


@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


@app.route('/api/cart)', methods=['post'])
def add_to_cart():
    # cart = session.get()
    # data = request.json()

    # if cart:
    #     tạo
    # else
    #     cart++

    return jsonify({
        "total_amount ": 1,
        "tong_gia": 1000
    })


if __name__ == '__main__':
    from DemoApp.app import admin

    app.run(debug=True)
