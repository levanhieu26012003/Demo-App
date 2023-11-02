from flask import render_template,request
import dao
from DemoApp.app import app


@app.route('/')
def index():

    kw = request.args.get("kw")

    navbar =  dao.load_nav()
    categories = dao.load_categories(kw)
    return render_template('index.html', nav = navbar, categories = categories)

if __name__ == '__main__' :
    app.run(debug=True)
