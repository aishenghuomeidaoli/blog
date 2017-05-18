# _*_ coding: utf-8 _*_
import datetime
from sqlalchemy import create_engine, Column, Integer, DateTime, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from config import Config

engine = create_engine(Config.SQL_URL)
Session = sessionmaker(bind=engine)


class BaseModel(object):
    """创建模型基类

    """
    @declared_attr
    def __tablename__(cls):
        """使用类名小写作为数据库表名"""
        return cls.__name__.lower()

    # 创建id列, 作为主键, 自增
    id = Column(Integer, Sequence('id_seq'), primary_key=True, autoincrement=True)


class TimeModel(object):
    """定义模型时间基类

    """
    # 定义创建时间列, 默认当前时间; 定义修改时间列, 更新时使用当前时间
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.datetime.now())

Base = declarative_base(cls=BaseModel)
db = Session()
