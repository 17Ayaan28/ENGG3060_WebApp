from app import *
from app.models import Clinician, Patient, Session

def testdb():
    with app.app_context():
        #db.drop_all()
        #db.create_all()
        #c = Clinician(first_name="Ross", last_name="Black",password_hash='pbkdf2:sha256:260000$kOIma7dkBE02WyYL$d9d241cc834b619dd4677602e9ccd8000d5995d5e81c7b487874810e322e8409')
        #p = Session(session_datetime="2016-12-21 00:00:00", left_score=10, right_score=20, patient_id=2)
        #db.session.add(p)
        #db.session.commit()

        sessions = Session.query.all()
        for p in sessions:
            print(p.session_datetime)

if __name__ == "__main__":
    testdb()