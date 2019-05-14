from flask import Blueprint
from mytopia.application.blog.models import Article


blog = Blueprint("blog", __name__, template_folder='/sb')


@blog.route("/index")
def index():
    """首页"""
    # TODO: 添加分页功能
    article_list = Article.query.all()
    # article_list = "x"
    x = article_list
    if not article_list:
        x = 'Empty'
    return '<h1>This is the %s page</h1>' % x


@blog.route("/all")
def show_all():
    """所有文章"""
    return '<h1>Show all articles</h1>'


@blog.route("/<article_id>")
def show_detail(article_id):
    """返回特定文章"""
    return '<h1>Show one article</h1>'



