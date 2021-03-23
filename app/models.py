from . import db
import enum
from sqlalchemy import Integer, Enum


class PropertyTypes(enum.Enum):
    """Defines the property types."""
    apartment = 'apartment'
    house = 'house'


class PropertyModel(db.Model):
    """The model for a housing property."""

    __tablename__ = 'properties'

    # Defining attributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    no_bedrooms = db.Column(db.Integer)
    description = db.Column(db.String(500))
    no_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.Numeric(10, 2))
    photo_path = db.Column(db.String(255))
    property_type = db.Column(Enum(PropertyTypes))

    # Initializing the Model, **kwargs is used to accept all arguments given
    def __init__(
            self, title, no_bedrooms, no_bathrooms, description,
            price, location, property_type, photo_path):

        super().__init__()

        self.title = title
        self.no_bedrooms = no_bedrooms
        self.no_bathrooms = no_bathrooms
        self.description = description
        self.price = price
        self.location = location
        self.property_type = property_type
        self.photo_path = photo_path
