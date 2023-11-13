from flask import render_template,request
import dao
from DemoApp.app import app, login


@app.route('/')
def index():
    kw = request.args.get("kw")
    navbar =  dao.load_nav()
    categories = dao.load_categories(kw)
    return render_template('index.html', nav = navbar, categories = categories)

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

@app.route('/admin/login', methods = ['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    get_user(username)

    return redirect(url_for('template/admin/login.html'))



if __name__ == '__main__' :
    from DemoApp.app import admin
    app.run(debug=True)
