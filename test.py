import os
from turtle import right
from venv import create
import psycopg2

DATABASE_URL = "postgres://ogbfzoaaronfll:ecff3f409a340d77f10ac744e1a9bf17e8fc92c70785189375a3a9c0349c60bd@ec2-3-214-2-141.compute-1.amazonaws.com:5432/dbi0i183fng1ot"

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
#postgres://hquttncnerkymd:8eacdafdc5ccadddd5506d7a0887886b0c6460ffe0b419da730b9f95c6fbba6d@ec2-54-165-178-178.compute-1.amazonaws.com:5432/dbvmsf4nunrpal

def createTables():

    cur = conn.cursor()
    

    commands = ("""
                create table Clinicians (
                    c_id serial,
                    first_name text NOT NULL,
                    last_name text NOT NULL,
                    PRIMARY KEY (c_id)
                );
                """,

                """
                create table Patients (
                    p_id serial,
                    first_name text NOT NULL,
                    last_name text NOT NULL,
                    age integer NOT NULL,
                    clinician_id integer NOT NULL,
                    PRIMARY KEY (p_id),
                    FOREIGN KEY (clinician_id) REFERENCES Clinicians(c_id)
                );""",
                """
                create table Sessions (
                    session_datetime timestamp,
                    leftScore int NOT NULL,
                    rightScore int NOT NULL,
                    patient_id int NOT NULL,
                    PRIMARY KEY (session_datetime),
                    FOREIGN KEY (patient_id) REFERENCES Patients(p_id)
                );    
                """
                )

    for c in commands:
        cur.execute(c)

    cur.close()
    conn.commit()
    

def dropTables():

    cur = conn.cursor()

    droptables = ("""drop table if exists clinicians cascade""",
                  """drop table if exists sessions cascade""",
                  """drop table if exists patients cascade""")

    for d in droptables:
        cur.execute(d)
    
    cur.close()
    conn.commit()


def addRows():
    add_clinician = """ INSERT INTO clinicians (first_name, last_name) VALUES (%s,%s)"""
    c1 = ("c1", "c1")

    add_patient = """ INSERT INTO patients (first_name, last_name, age, clinician_id) VALUES (%s,%s,%s,%s)"""
    p1 = ("p1", "p1", 22, 1)



    add_session = """ INSERT INTO sessions (session_datetime, leftScore, rightScore, patient_id) VALUES (%s,%s,%s,%s)"""
    s1 = ("2016-06-22 19:10:25", 30, 45, 1)

    cur = conn.cursor()
    cur.execute(add_clinician, c1)
    cur.execute(add_patient, p1)
    cur.execute(add_session, s1)
    
    cur.close()
    conn.commit()




def getPateintProgress(patient_id):

    cur = conn.cursor()

    getSessions = """select * from sessions where patient_id = %s order by session_datetime"""

    cur.execute(getSessions, str(patient_id))
    record = cur.fetchall()
    if record == None:
        print("No records found")
        return

    left_hand_performance_data = []
    right_hand_performance_data = []
    session_date = []

    for session in record:
        left_hand_performance_data.append(session[1])
        right_hand_performance_data.append(session[2])
        session_date.append(session[0])

    print(left_hand_performance_data)
    print(session_date)

    cur.close()

def getSession():

    cur = conn.cursor()

    getSessions = """delete from sessions where patient_id = '6'"""
    #d = ''
    cur.execute(getSessions)
    conn.commit()
    cur.close()


if __name__ == "__main__":
    getSession()