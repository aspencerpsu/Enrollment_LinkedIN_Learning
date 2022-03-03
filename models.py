from datetime import datetime
from unicodedata import name
from application import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    courses = db.relationship("Course", secondary="enrollment")

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseID = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String(), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(), nullable=False)
    term = db.Column(db.Enum("Fall", "Spring", "Fall, Spring", name="PeriodPiece"), nullable=False)
    users = db.relationship("User", secondary="enrollment")


class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    dateEnrolled = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user = db.relationship(User, backref=db.backref("Enrollment", cascade="all, delete-orphan"))
    course = db.relationship(Course, backref=db.backref("Enrollment", cascade="all, delete-orphan"))
