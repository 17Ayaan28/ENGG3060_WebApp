from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return Clinician.query.get(int(id))

class Clinician(UserMixin, db.Model):
    __tablename__ = "clinicians"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text(), nullable=False)
    last_name = db.Column(db.Text(), nullable=False)
    password_hash = db.Column(db.Text(), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Clinician {}>'.format(self.id)

class Patient(db.Model):
    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text(), nullable=False)
    last_name = db.Column(db.Text(), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Text(), nullable=False)
    condition = db.Column(db.Text(), nullable=True)
    affected_hand = db.Column(db.Text(), nullable=True)
    dominant_hand = db.Column(db.Text(), nullable=True)
    clinician_id = db.Column(db.Integer, db.ForeignKey("clinicians.id"), nullable=False)


class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text(), nullable=False)
    last_name = db.Column(db.Text(), nullable=False)
    password_hash = db.Column(db.Text(), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Session(db.Model):
    __tablename__ = "sessions"
    session_starttime = db.Column(db.DateTime, nullable=False, primary_key=True, default="now()")
    total_block_count = db.Column(db.Integer, nullable=False)
    block_timestamps = db.Column(db.Text(), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    patient_hand = db.Column(db.Text(),nullable=False)