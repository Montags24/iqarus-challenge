import os

from cryptography.fernet import Fernet
from datetime import datetime
from dotenv import load_dotenv
from website import db
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
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
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    code = Column(String(30), unique=True, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    def get_dict(self):
        return dict(
            id=self.id,
            timestamp=self.timestamp,
            name=self.name,
            code=self.code,
        )


class SecurityForm(db.Model):
    __tablename__ = "security_form"
    id = Column(Integer, primary_key=True)
    longitude = Column(Float)
    latitude = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    # Maps to the user table
    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            name=f"fk_{__tablename__}_users",
            ondelete="CASCADE",
        ),
    )
    armedGroupsPresence = Column(String(50))
    reportOfViolence = Column(String(50))
    localEnforcementPresence = Column(String(50))
    securityRiskComments = Column(String(250))
    incidentsReported = Column(String(50))
    riskToRelief = Column(String(50))
    incidentsComments = Column(String(250))

    def get_dict(self):
        return dict(
            id=self.id,
            longitude=self.longitude,
            latitude=self.latitude,
            timestamp=self.timestamp,
            user_id=self.user_id,
            armedGroupsPresence=self.armedGroupsPresence,
            reportOfViolence=self.reportOfViolence,
            localEnforcementPresence=self.localEnforcementPresence,
            securityRiskComments=self.securityRiskComments,
            incidentsReported=self.incidentsReported,
            riskToRelief=self.riskToRelief,
            incidentsComments=self.incidentsComments,
        )
