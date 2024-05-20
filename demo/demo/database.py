from sqlalchemy import create_engine
import urllib.parse

# Define the database connection
password_encoded = urllib.parse.quote_plus("oviya@1604")
engine = create_engine(f'mysql+mysqlconnector://root:{password_encoded}@localhost:3306/healthcare')
conn = engine.connect()

# Function to insert patient information
def insert_patient_info(name, age, gender, hypertension, diabetes, heart_disease, triage, location, accident, cause, dept):
    query = f"""
    INSERT INTO patient_data (Name, Age, Gender, Hypertension, Diabetes, `History of Heart Disease`, Triage, Location, Accident, `Cause of Accident`, Department)
    VALUES ('{name}', {age}, '{gender}', '{hypertension}', '{diabetes}', '{heart_disease}', '{triage}', '{location}', '{accident}', '{cause}', '{dept}')
    """
    conn.execute(query)
