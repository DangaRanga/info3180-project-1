from . import db


class Property(db.Model):
    """The model for a housing property."""

    __tablename__ = 'properties'

    # Defining attributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    no_bedrooms = db.Column(db.Integer)
    no_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.Numeric(10, 2))
    photo_path = db.Column(db.String(255))

    # Initializing the Model, **kwargs is used to accept all arguments given
    def __init__(self, **kwargs):
        super(Property, self).__init__(**kwargs)
