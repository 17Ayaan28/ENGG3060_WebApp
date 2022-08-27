create table Users (
    id serial,
    first_name NOT NULL,
    last_name NOT NULL,
    age integer NOT NULL,
    clinician_id integer NOT NULL,
    PRIMARY KEY (id)
    FOREIGN KEY (clinician_id) REFERENCES Clinicians(id)
);

create table Clinicians (
    id serial,
    first_name NOT NULL,
    last_name NOT NULL, 
);


create table Sessions (
    session_date DATE,
    leftScore int NOT NULL,
    rightScore int NOT NULL,
    patient_id integer NOT NULL,
    PRIMARY KEY (session_date)
    FOREIGN KEY (patient_id) REFERENCES Users(id)
);




