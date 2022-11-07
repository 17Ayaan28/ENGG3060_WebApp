
create table Patients (
    p_id serial,
    first_name text NOT NULL,
    last_name text NOT NULL,
    age integer NOT NULL,
    clinician_id integer NOT NULL,
    PRIMARY KEY (p_id),
    FOREIGN KEY (clinician_id) REFERENCES Clinicians(c_id)
);

create table Admin (
    admin_id serial;
    first_name text NOT NULL;
    last_name text NOT NULL;
    PRIMARY KEY (admin_id)
);

create table Clinicians (
    c_id serial,
    first_name text NOT NULL,
    last_name text NOT NULL,
    PRIMARY KEY (c_id)
);

create table Sessions (
    session_datetime timestamp,
    leftScore int NOT NULL,
    rightScore int NOT NULL,
    patient_id int NOT NULL,
    PRIMARY KEY (session_datetime),
    FOREIGN KEY (patient_id) REFERENCES Patients(p_id)
);    




