from . import SerializerMixin, validates, re, db
from datetime import datetime


class User(db.Model, SerializerMixin):
    # # # # # Table Name
    __tablename__ = 'users'

    # # # # # Attribute
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now())

    # # # # # Relationship
    entries = db.relationship('Entry', back_populates='user')

    # # # # # Serialize
    serialize_rules=('-entries',)

    # # # # # Representation
    def __repr__(self):
        return f""" 
            <User {self.id}
                username: {self.username}
                created_at: {self.created_at}
                />
        """

    # # # # # Property
    
    # # # # # Validate