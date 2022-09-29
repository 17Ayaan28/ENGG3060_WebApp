from app import app
import psycopg2
import os
from flask import render_template, request
from app import app

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
    
@app.route('/patient')
def getPateintProgress():

    cur = conn.cursor()

    getSessions = """select * from sessions where patient_id = 1 order by session_datetime"""

    cur.execute(getSessions)
    record = cur.fetchall()

    if record == None:
        print("No records found")
        return
    
    left_hand_count = []
    right_hand_count = []
    session_date = []

    for session in record:
        left_hand_count.append(session[1])
        right_hand_count.append(session[2])
        session_date.append(session[0])
    print("--------------------------------")
    left_hand_count = [10,20,30,40,50]
    session_date = [1,2,3,4,5]
    
    return render_template('getPatientProgress.html', leftCount=left_hand_count, sessionCount=session_date)

@app.route('/sessions') 
def showSessions():
    
    patient_id = request.args.get("patient_id", default="", type=str)
    print(patient_id)

    cur = conn.cursor()

    getSessions = """select * from sessions where patient_id = %s """

    cur.execute(getSessions, patient_id)
    record = cur.fetchall()

    if record == None: 
        print("The patient has no BBT sessions")
        return

    sessions = []
    for rec in record:
        sessions.append(rec[0])
    
    return render_template('showSessions.html', Sessions=sessions)

    