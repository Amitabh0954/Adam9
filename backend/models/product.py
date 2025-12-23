from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    category = db.relationship('Category', backref='products')

    def __repr__(self) -> str:
        return f"Product('{self.name}', '{self.price}')"