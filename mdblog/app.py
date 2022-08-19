from flask import Flask
from flask import render_template

from .database import articles

flask_app = Flask(__name__)

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja")

@flask_app.route("/about/")
def view_about():
    return render_template("about.jinja")

@flask_app.route("/admin/")
def view_admin():
    return render_template("admin.jinja")

@flask_app.route("/articles/")
def view_articles():
    return render_template("articles.jinja", articles=articles.items())

@flask_app.route("/articles/<int:art_id>")
def view_article(art_id):
    article = articles.get(art_id)
    if article:
        return render_template("article.jinja", article=article)
    return render_template("article_not_found.jinja", art_id=art_id)

#@flask_app.route("/")
#def index():
#    return "<html> <body> <h1> Welcom Intruer </h1> </body> </html>"


#@flask_app.route("/")
#def index():
#    return "Hello World"

#@flask_app.route("/admin/")
#def view_admin():
#    return "Hello admin"

#@flask_app.route("/admin/<string:name>/", methods=["GET", "POST"])
#def view_admin_name(name):
#    return "Hello {}".format(name)

#@flask_app.route("/article/<int:art_id>/")
#def view_article(art_id):
#    return "Article #{}".format(art_id)

#@flask_app.route("/article/<int:art_id>/schwifty/<float:foo>")
#def view_schwifty_article(art_id, foo):
#    return "Article #{} schwifty: {}".format(art_id, foo)    
