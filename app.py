from flask import Flask,request,render_template
import pandas as pd
import numpy as np
from flask import jsonify
from sklearn.naive_bayes import MultinomialNB
import pickle
app=Flask(__name__)


symptoms=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
        'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
        'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
        'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
        'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
        'Impetigo']



@app.route('/',methods=['GET','POST'])
def home():
    return render_template("home.html",len=len(symptoms),symptoms=symptoms)

@app.route('/',methods=['GET','POST'])
def func():
    if request.method=='POST':
        l2=[]
        for x in range(0,len(symptoms)):
            l2.append(0)
        model=pickle.load(open('model.pkl','rb'))
        symp1=request.form.get("symp1")
        symp2=request.form.get("symp2")
        symp3=request.form.get("symp3")
        symp4=request.form.get("symp4")
        symp5=request.form.get("symp5")
        test_input=[symp1,symp2,symp3,symp4,symp5]

        for i in range(0,len(symptoms)):
            for j in test_input:
                if(j==symptoms[i]):
                    l2[i]=1
        answer='no'
        test_input=[l2]
        print("Symptom 1 is:",symp1)
        predict=model.predict(test_input)       
        op=predict[0]
        ans='no'
        for a in range(0,len(disease)):
            if(disease[op]==disease[a]):
                ans='yes'
                break
        if ans=='yes':
            answer=disease[op]
        
        print("value is",op)
        return render_template("home.html",ans=answer)

@app.route('/upload',methods=['GET','POST'])
def upload():
        l2=[]
        for x in range(0,len(symptoms)):
            l2.append(0)
        model=pickle.load(open('model.pkl','rb'))
        symp1=request.form.get("symp1")
        symp2=request.form.get("symp2")
        symp3=request.form.get("symp3")
        symp4=request.form.get("symp4")
        symp5=request.form.get("symp5")
        test_input=[symp1,symp2,symp3,symp4,symp5]

        for i in range(0,len(symptoms)):
            for j in test_input:
                if(j==symptoms[i]):
                    l2[i]=1
        answer='no'
        test_input=[l2]
        print("Symptom 1 is:",symp1)
        predict=model.predict(test_input)       
        op=predict[0]
        ans='no'
        for a in range(0,len(disease)):
            if(disease[op]==disease[a]):
                ans='yes'
                break
        if ans=='yes':
            answer=disease[op]
        return jsonify({"ans":answer})

if __name__ == '__main__':
    app.run(debug=True)