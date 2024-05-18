import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv
from math import radians, sin, cos, sqrt, atan2
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
            category="security",
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

    def distance_to(self, lat, lng):
        """
        Returns the great-circle distance in kilometers between the instance and a point.
        """
        R = 6371  # Earth's radius in kilometers

        dlat = radians(lat - self.latitude)
        dlng = radians(lng - self.longitude)

        a = (
            (sin(dlat / 2) * sin(dlat / 2) + cos(radians(self.latitude))).real
            * cos(radians(lat).real)
            * sin(dlng / 2)
            * sin(dlng / 2)
        )

        c = 2 * atan2(sqrt(a), sqrt(1 - a)).real

        d = R * c

        return d


class InfrastructureForm(db.Model):
    __tablename__ = "infrastructure_form"
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
    roadCondition = Column(String(50))
    roadDamage = Column(String(50))
    roadAccess = Column(String(50))
    roadComments = Column(String(250))
    buildingIntegrity = Column(String(50))
    buildingType = Column(String(50))
    buildingDamage = Column(String(50))
    buildingComments = Column(String(250))
    utilityPower = Column(String(50))
    utilityWater = Column(String(50))
    utilityComms = Column(String(50))
    utilityComments = Column(String(250))

    def get_dict(self):
        return dict(
            id=self.id,
            category="infrastructure",
            longitude=self.longitude,
            latitude=self.latitude,
            timestamp=self.timestamp,
            user_id=self.user_id,
            roadCondition=self.roadCondition,
            roadDamage=self.roadDamage,
            roadAccess=self.roadAccess,
            roadComments=self.roadComments,
            buildingIntegrity=self.buildingIntegrity,
            buildingType=self.buildingType,
            buildingDamage=self.buildingDamage,
            buildingComments=self.buildingComments,
            utilityPower=self.utilityPower,
            utilityWater=self.utilityWater,
            utilityComms=self.utilityComms,
            utilityComments=self.utilityComments,
        )

    def distance_to(self, lat, lng):
        """
        Returns the great-circle distance in kilometers between the instance and a point.
        """
        R = 6371  # Earth's radius in kilometers

        dlat = radians(lat - self.latitude)
        dlng = radians(lng - self.longitude)

        a = (
            (sin(dlat / 2) * sin(dlat / 2) + cos(radians(self.latitude))).real
            * cos(radians(lat).real)
            * sin(dlng / 2)
            * sin(dlng / 2)
        )

        c = 2 * atan2(sqrt(a), sqrt(1 - a)).real

        d = R * c

        return d


class CommunicationsForm(db.Model):
    __tablename__ = "communications_form"
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
    commsInfrastructure = Column(String(50))
    commsPhoneAndInternet = Column(String(50))
    commsAvailability = Column(String(50))
    commsAlternative = Column(String(50))
    commsComments = Column(String(250))
    connectElectricity = Column(String(50))
    connectFuelAvailability = Column(String(50))
    connectBackupPower = Column(String(50))
    connectLocalControl = Column(String(250))
    connectComments = Column(String(250))

    def get_dict(self):
        return dict(
            id=self.id,
            category="communications",
            longitude=self.longitude,
            latitude=self.latitude,
            timestamp=self.timestamp,
            user_id=self.user_id,
            commsInfrastructure=self.commsInfrastructure,
            commsPhoneAndInternet=self.commsPhoneAndInternet,
            commsAvailability=self.commsAvailability,
            commsAlternative=self.commsAlternative,
            commsComments=self.commsComments,
            connectElectricity=self.connectElectricity,
            connectFuelAvailability=self.connectFuelAvailability,
            connectBackupPower=self.connectBackupPower,
            connectLocalControl=self.connectLocalControl,
            connectComments=self.connectComments,
        )

    def distance_to(self, lat, lng):
        """
        Returns the great-circle distance in kilometers between the instance and a point.
        """
        R = 6371  # Earth's radius in kilometers

        dlat = radians(lat - self.latitude)
        dlng = radians(lng - self.longitude)

        a = (
            (sin(dlat / 2) * sin(dlat / 2) + cos(radians(self.latitude))).real
            * cos(radians(lat).real)
            * sin(dlng / 2)
            * sin(dlng / 2)
        )

        c = 2 * atan2(sqrt(a), sqrt(1 - a)).real

        d = R * c

        return d
