from main import db #(an object class)

class User(db.Model): #notice that User our class extends (inherits)  db.Model
     __tablename__= 'userregister' #this is the name we want the table in database to have.
     id=db.Column(db.Integer, primary_key=True)
     firstname=db.Column(db.String(20), unique=False, nullable=False)
     lastname = db.Column(db.String(20), unique=False, nullable=False)
     othernames = db.Column(db.String(20), unique=False, nullable=True)
     email = db.Column(db.String(50), unique=True, nullable=False)
     password = db.Column(db.String(256), unique=False, nullable=False)

  # represent the object when it is queried for.

 def __repr__(self):
    return '<Register {}>'.format(self.id)