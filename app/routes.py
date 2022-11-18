from app import app
import psycopg2
import os
from werkzeug.security import generate_password_hash
from flask import render_template, request, flash, redirect, url_for
from app import app
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Clinician, Patient, Session, Admin
from app.forms import LoginForm, admin_LoginForm, create_patient, create_clinician
from app import db

#os.environ['DATABASE_URL']
DATABASE_URL = "postgres://ogbfzoaaronfll:ecff3f409a340d77f10ac744e1a9bf17e8fc92c70785189375a3a9c0349c60bd@ec2-3-214-2-141.compute-1.amazonaws.com:5432/dbi0i183fng1ot"

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
os.environ["admin_login"] = "0"


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('showPatients'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Clinician.query.filter_by(first_name=form.first_name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('showPatients'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/adminlogin', methods=['GET', 'POST'])
def admin_login():
    #print(session.get("admin"))
    #var = app.config['ADMIN_LOGIN']
    var = os.environ['admin_login']
    print(var)
    if (var == "1"):
        return render_template('adminhome.html')
    else:
        form = admin_LoginForm()
        if form.validate_on_submit():
            admin = Admin.query.filter_by(first_name=form.first_name.data).first()
            if admin is None or not admin.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('admin_login'))
            os.environ["admin_login"] = "1"
            return redirect(url_for('admin_home'))
        return render_template('admin_login.html', form=form)

@app.route('/adminhome')
def admin_home():
    var = os.environ['admin_login']
    print(var)
    if (var == "1"):
        return render_template('adminhome.html')
    else:
        return redirect(url_for('admin_login'))

@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/createpatient', methods=['GET', 'POST'])
def createPatient():

    form = create_patient()
    if form.validate_on_submit():
        patient = Patient(first_name=form.first_name.data,last_name=form.last_name.data,age=form.age.data,sex=form.sex.data, condition=form.condition.data, affected_hand=form.affected_hand.data, dominant_hand=form.dominant_hand.data, clinician_id=form.clinician_id.data)
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('createPatient'))

    return render_template('addpatient.html', form=form) 



@app.route('/createclinician', methods=['GET', 'POST'])
def createClinician():

    form = create_clinician()
    if form.validate_on_submit():
        hash = generate_password_hash(form.password.data)
        clinician = Clinician(first_name=form.first_name.data,last_name=form.last_name.data,password_hash=hash)
        db.session.add(clinician)
        db.session.commit()
    return render_template('addclinician.html', form=form) 


@app.route('/patients')
@login_required
def showPatients():
    patients = Patient.query.filter_by(clinician_id=current_user.id)
    return render_template('showPatients.html', patient_list=patients)

@login_required
@app.route('/sessions/<pid>') 
def showSessions(pid):

    sessions = Session.query.filter_by(patient_id=pid)
    return render_template('showSessions.html', Sessions=sessions,patient_id=pid)

@login_required
@app.route('/sessionperformance/<starttime>') 
def showSessionPerformance(starttime):

    print(starttime)
    left_session = Session.query.filter_by(session_starttime=starttime, patient_hand="left")
    #right_session = Session.query.filter_by(session_starttime=starttime, patient_hand="right")

    if left_session == None:
        print("No records found")
        left_timestamps = []
    else:
        left_str = left_session[0].block_timestamps
        left_timestamps = left_str.split(",")

    #if right_session == None:
    #    print("No records found")
    right_timestamps = []
    #else:
    
        #right_str = right_session[0].block_timestamps
        #right_timestamps = right_str.split(",")

    ma = len(left_timestamps)
    x_vals = []
    i = 1
    while (i <= ma):
        x_vals.append(i)
        i = i + 1


    return render_template('sessionPerformance.html', left_ts=left_timestamps, right_ts=right_timestamps, X_vals=x_vals) 


@login_required
@app.route('/patientProgress/<pid>')
def getPateintProgress(pid):

    left_sessions = Session.query.filter_by(patient_id=pid, patient_hand="left").order_by("session_starttime")

    right_sessions = Session.query.filter_by(patient_id=pid, patient_hand="right").order_by("session_starttime")

    if left_sessions == None:
        print("No records found")
        return
    
    if right_sessions == None:
        print("No records found")
        return
    
    left_block_count_list = []
    right_block_count_list = []
    session_date_list = []

    avg_male = []

    for s in left_sessions:
        left_block_count_list.append(s.total_block_count)
        session_date_list.append(s.session_starttime)
        avg_male.append(80)
    
    for s in right_sessions:
        right_block_count_list.append(s.total_block_count)
    
    
    return render_template('getPatientProgress.html', leftCount=left_block_count_list, rightCount=right_block_count_list,sessionDates=session_date_list, patient_id=pid, avg_level=avg_male)



    