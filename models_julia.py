from db import Base, db

class Expenses(Base):
    __tablename__ = "expenses"
    idexpenses = db.Column(db.INTEGER, primary_key=True)
    item = db.Column(db.VARCHAR(45), nullable=False)
    price = db.Column(db.INTEGER, nullable=False)
    date = db.Column(db.DATETIME(10), nullable=False)

db.create_all()