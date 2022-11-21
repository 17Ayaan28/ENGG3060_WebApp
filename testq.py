from app import *
from app.models import Clinician, Patient, Session, Admin
from werkzeug.security import generate_password_hash

def testdb():
    with app.app_context():
        
        #db.drop_all()
        #db.create_all()
        #c = Clinician(first_name="c1", last_name="c1", password_hash="pbkdf2:sha256:260000$P0NBrrFywUaUTZiE$2e635e5bbd0c62aa976a29f51a8a4eda4d127eef4d774583f41fdc9b2fc5860e")
        #p = Patient(first_name="p1", last_name="p1",age=22,sex="male",clinician_id=3)
        s = Session(total_block_count=3, block_timestamps="3.3,6.4,7.9", patient_id=6, patient_hand="left")
        #a = Admin(first_name="a1",last_name="a1",password_hash="pbkdf2:sha256:260000$EQMiF5Xq03OkCwim$734a3c345c402dcc6a3498f9524596762e1241bc880442fbd9933ff8346f4475")
        db.session.add(s)
        #db.session.add(p)
        #db.session.add(s)
        db.session.commit()

        #sessions = Session.query.filter_by(patient_id=4, patient_hand="left").order_by("session_starttime")
        #for p in sessions:
        #    print(p.session_starttime)

    #arr = [12.300,1.002, 35.70,40.300]

    #st = []

    #for a in arr:
    #    st.append(str(a))

    #print(st)

    #fl = []
    #for s in st:
    #    fl.append(float(s))
    
    #print(fl)

if __name__ == "__main__":
    testdb()