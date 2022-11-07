from app import *
from app.models import Clinician, Patient, Session

def testdb():
    with app.app_context():
        #db.drop_all()
        #db.create_all()
        c = Patient(first_name="p1", last_name="p1",age=22,sex="male",clinician_id=2)
        #p = Session(session_datetime="2016-12-21 00:00:00", left_score=10, right_score=20, patient_id=2)
        db.session.add(c)
        db.session.commit()

        sessions = Session.query.all()
        for p in sessions:
            print(p.session_datetime)

if __name__ == "__main__":
    testdb()