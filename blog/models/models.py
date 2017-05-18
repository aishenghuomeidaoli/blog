# _*_ coding: utf-8 _*_
from sqlalchemy import Column, Integer, String, Text
from . import Base, TimeModel
from .. import constant


class Article(Base, TimeModel):
    title = Column(String)
    content = Column(Text)
    state = Column(Integer, default=constant.ARTICLE_STATE_ON)

    def __repr__(self):
        return '<Article (id={0}, title={1}, state={2}, created_at={3}, updated_at={4})>' \
            .format(self.id, self.title.encode('utf-8'), self.state, self.created_at, self.updated_at)
