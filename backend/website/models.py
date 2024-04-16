# from datetime import datetime, timedelta
# from flask import current_app as app
from website import db

from sqlalchemy.sql import func

# , expression, and_, or_


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=False, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    created_timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return "<User {}>".format(self.name)


class Organisation(db.Model):
    __tablename__ = "organisations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    code = db.Column(db.String(30), unique=True, nullable=False)
    created_timestamp = db.Column(
        db.DateTime(timezone=True), server_default=db.func.now()
    )


# Many to many relationship table
class UserOrganisation(db.Model):
    __tablename__ = "users_organisations"
    __table_args__ = (
        db.UniqueConstraint(
            "user_id", "organisation_id", name="unique_user_organisation"
        ),
    )
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", name=f"fk_{__tablename__}_users", ondelete="CASCADE"),
        nullable=False,
    )
    organisation_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "organisations.id",
            name=f"fk_{__tablename__}_organisations",
            ondelete="CASCADE",
        ),
        nullable=True,
    )
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    created_timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
