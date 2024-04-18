import os

from cryptography.fernet import Fernet
from datetime import datetime
from dotenv import load_dotenv
from website import db
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy_utils import EncryptedType

# , expression, and_, or_

this_directory = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(this_directory, "../.env"))

key = os.environ.get("ENCRYPTION_KEY")
cipher = Fernet(key)


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(EncryptedType(String, key), nullable=False)
    username = Column(EncryptedType(String, key), nullable=False, unique=True)
    hashed_password = Column(String(300), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    # Maps to the organisation table
    organisation_id = Column(Integer, ForeignKey("organisations.id"))

    def __repr__(self):
        return "<User {}>".format(self.name)

    def get_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            username=self.username,
            timestamp=self.timestamp,
        )


class Organisation(db.Model):
    __tablename__ = "organisations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    code = db.Column(db.String(30), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=db.func.now())

    def get_dict(self):
        return dict(
            id=self.id,
            timestamp=self.timestamp,
            name=self.name,
            code=self.code,
        )


class SecurityForm(db.Model):
    __tablename__ = "security_form"
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=db.func.now())

    # Maps to the user table
    user_id = db.Column(
        db.Integer,
        ForeignKey(
            "users.id",
            name=f"fk_{__tablename__}_users",
            ondelete="CASCADE",
        ),
    )
    armedGroupsPresence = db.Column(db.String(50))
    reportOfViolence = db.Column(db.String(50))
    localEnforcementPresence = db.Column(db.String(50))
    securityRiskComments = db.Column(db.String(500))
    incidentsReported = db.Column(db.String(50))
    riskToRelief = db.Column(db.String(50))
    incidentsComments = db.Column(db.String(500))

    def get_dict(self):
        return dict(
            id=self.id,
            timestamp=self.timestamp,
            name=self.name,
            code=self.code,
            user_id=self.user_id,
            armedGroupsPresence=self.armedGroupsPresence,
            reportOfViolence=self.reportOfViolence,
            localEnforcementPresence=self.localEnforcementPresence,
            securityRiskComments=self.securityRiskComments,
            incidentsReported=self.incidentsReported,
            riskToRelief=self.riskToRelief,
            incidentsComments=self.incidentsComments,
        )
