# _*_ coding: utf-8 _*_
from flask import render_template
from . import main_bp
from .. import constant
from ..models import db
from ..models.models import Article


@main_bp.route('/')
def index():
    articles = db.query(Article).filter_by(state=constant.ARTICLE_STATE_ON).all()
    return render_template('index.html', articles=articles)
