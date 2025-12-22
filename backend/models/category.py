from datetime import datetime
from backend.config.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

product_categories = db.Table('product_categories',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    children = db.relationship('Category', backref=db.backref('parent', remote_side=[id]), lazy=True)
    products = db.relationship('Product', secondary=product_categories, backref=db.backref('categories', lazy='dynamic'))

    def __repr__(self) -> str:
        return f'<Category {self.name}>'