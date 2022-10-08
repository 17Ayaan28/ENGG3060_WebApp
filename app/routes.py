from app import app
import psycopg2
import os
from flask import render_template, request, flash, redirect, url_for
from app import app
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Clinician, Patient, Session
from app.forms import LoginForm, admin_LoginForm, create_patient, create_clinician
from app import db

#os.environ['DATABASE_URL']
DATABASE_URL = "postgres://ogbfzoaaronfll:ecff3f409a340d77f10ac744e1a9bf17e8fc92c70785189375a3a9c0349c60bd@ec2-3-214-2-141.compute-1.amazonaws.com:5432/dbi0i183fng1ot"

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/')
@app.route('/index')
def index():
    return "Home"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('patients'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Clinician.query.filter_by(first_name=form.first_name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('patients'))
    return render_template('login.html', title='Sign In', form=form)

@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/adminlogin')
def admin_login():
    form = admin_LoginForm()

    if form.validate_on_submit():
        user = Clinician.query.filter_by(first_name=form.first_name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('adminlogin'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('patients'))
    return render_template('adminlogin.html', title='Sign In', form=form)

@app.route('/createpatient')
def createPatient():
    form = create_patient()
    patient = Patient(first_name=form.first_name.data,last_name=form.last_name.data,age=form.age.data,sex=form.sex.data)
    db.session.add(patient)
    db.session.commit()

@app.route('/patients')
@login_required
def showPatients():
    patients = Patient.query.filter_by(clinician_id=current_user.id)
    return render_template('showPatients.html', patient_list=patients)

@login_required
@app.route('/sessions/<pid>') 
def showSessions(pid):

    sessions = Session.query.filter_by(patient_id=2)
    return render_template('showSessions.html', Sessions=sessions)

@app.route('/patientProgess/<pid>')
def getPateintProgress(pid):

    sessions=Session.query.filter_by(patient_id=pid)

    if sessions == None:
        print("No records found")
        return
    
    left_hand_count = []
    right_hand_count = []
    session_date = []

    for s in sessions:
        left_hand_count.append(s.left_score)
        right_hand_count.append(s.right_score)
        session_date.append(s.session_datetime)
    
    return render_template('getPatientProgress.html', leftCount=left_hand_count, sessionCount=session_date)



    