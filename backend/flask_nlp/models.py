# coding=utf-8
from flask import url_for

# 导入数据库实例
from flask_nlp import db


# Novel模型
class Novel(db.Model):
    __tablename__ = 'novels'
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(64), index=True)
    book_url = db.Column(db.String)
    book_img = db.Column(db.String)
    author = db.Column(db.String(64))
    type = db.Column(db.String(64), nullable=True)
    last_update = db.Column(db.String(64), nullable=True)
    profile = db.Column(db.Text, nullable=True)
    keyword = db.Column(db.String)
    page = db.Column(db.Integer)

    chapters = db.relationship('Chapter', backref='book', lazy='dynamic')

    __table_args__ = {'mysql_charset': 'utf8'}

    def to_json(self):
        json_novel = {
            'id': self.id,
            'book_name': self.book_name,
            'book_img': self.book_img,
            'author': self.author,
            'type': self.type,
            'last_update': self.last_update,
            'profile': self.profile,
        }
        return json_novel


#Chapter模型
class Chapter(db.Model):
    __tablename__ = 'chapters'
    id = db.Column(db.Integer, primary_key=True)
    chapter = db.Column(db.String(64))
    chapter_url = db.Column(db.String, index=True)

    content = db.relationship('Content', backref='chapter', lazy='dynamic')
    wordsegs = db.relationship('WordSeg', backref='chapter', lazy='dynamic')
    postagsegs = db.relationship('PostWordSeg',
                                 backref='chapter',
                                 lazy='dynamic')

    book_id = db.Column(db.Integer, db.ForeignKey('novels.id'))

    def to_json(self):
        json_chapter = {
            'id': self.id,
            'book_id': self.book_id,
            'chapter_name': self.chapter
        }

        return json_chapter


class Content(db.Model):
    __tablename__ = 'contents'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)

    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'))

    def to_json(self):
        json_content = {'id': self.chapter_id, 'content': self.content}

        return json_content


class WordSeg(db.Model):
    __tablename__ = 'wordsegs'
    id = db.Column(db.Integer, primary_key=True)

    wordseg = db.Column(db.String)

    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'))


class PostWordSeg(db.Model):
    __tablename__ = 'postcontentsegs'
    id = db.Column(db.Integer, primary_key=True)

    wordseg = db.Column(db.String)
    postag = db.Column(db.String)

    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'))


class Alembic(db.Model):
    __tablename__ = 'alembic_version'
    version_num = db.Column(db.String(32), primary_key=True, nullable=False)

    @staticmethod
    def clear_A():
        for a in Alembic.query.all():
            print(a.version_num)
            db.session.delete(a)
        db.session.commit()
        print('======== data in Table: Alembic cleared!')