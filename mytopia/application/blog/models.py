from mytopia.application.extensions import db
from sqlalchemy import Table, Column, String, Integer, DATETIME, Text


class Article(db.Model):
    """文章"""
    __tablename__ = 'article'

    id = Column('id', Integer, primary_key=True)
    title = Column('article_title', String(80), nullable=False)
    content = Column('article_content', Text)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)

    pub_time = Column('pub_time', DATETIME, nullable=False)
    update_time = Column('update_time', DATETIME, nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.title


class Category(db.Model):
    """文章分类"""
    __tablename__ = 'category'

    id = Column('id', Integer, primary_key=True)
    category = Column('category_name', String(32), default='杂')

    def __repr__(self):
        return '<Category %r>' % self.category


if __name__ == '__main__':
    db.create_all()
