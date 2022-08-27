import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
#postgres://hquttncnerkymd:8eacdafdc5ccadddd5506d7a0887886b0c6460ffe0b419da730b9f95c6fbba6d@ec2-54-165-178-178.compute-1.amazonaws.com:5432/dbvmsf4nunrpal
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
            );""")

cur = conn.cursor()

for c in commands:
    cur.execute(c)

cur.close()
conn.commit()