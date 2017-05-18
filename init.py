from blog.models import engine, db
from blog.models.models import *


def init():
    Base.metadata.create_all(engine)


def write(title, content):
    article = Article(title=title, content=content)
    db.add(article)
    db.commit()

if __name__ == '__main__':
    init()
