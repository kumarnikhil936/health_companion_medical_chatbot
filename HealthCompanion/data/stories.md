## story_1
* greet
 - utter_ask_howcanhelp
* make_appointment
 - utter_ask_name
* inform{"contact_name": "Nikhil"}
 - utter_ask_phone_number
* inform{"contact_phone": "1234567890"}
 - utter_ask_gender
* inform{"contact_gender": "Male"}
 - utter_ask_age
* inform{"contact_age": "26"}
 - utter_ask_institution
* inform{"institution_type":"hospital"}
 - utter_ask_location
* inform{"contact_location":"Paderborn"}
 - utter_ask_date
* inform{"date":"28 May"}
 - utter_ask_time
* inform{"time": "10 AM"}
 - action_search_institution
 - slot{"institution_name": "City Hospital"}
 - slot{"institution_address": "Street 20, Paderborn"}
 - slot{"institution_phone": "1234568966"}
* affirm
 - utter_ack_makeappointment
 - action_make_appointment
* thankyou
 - utter_goodbye
 
## story_2
* greet
 - utter_ask_howcanhelp
* make_appointment
 - utter_ask_name
* inform{"contact_name": "Niki"}
 - utter_ask_phone_number
* inform{"contact_phone": "14424567890"}
 - utter_ask_gender
* inform{"contact_gender": "Female"}
 - utter_ask_age
* inform{"contact_age": "26"}
 - utter_ask_institution
* inform{"institution_type":"pharmacy"}
 - utter_ask_location
* inform{"contact_location":"Aachen"}
 - utter_ask_date
* inform{"date":"22 May"}
 - utter_ask_time
* inform{"time": "11 AM"}
 - action_search_institution
 - slot{"institution_name": "City Pharmacy"}
 - slot{"institution_address": "Street 22, Aachen"}
 - slot{"institution_phone": "1234532326"}
* affirm
 - utter_ack_makeappointment
 - action_make_appointment
* thankyou
 - utter_goodbye

 ## story_4
* greet
 - utter_ask_howcanhelp
* search_institution
 - utter_ask_institution
* inform{"institution_type":"Doctor"}
 - utter_ask_location
* inform{"contact_location":"Dubai"}
 - action_search_institution
 - slot{"institution_name": "Doctor Abdul Jabaar"}
 - slot{"institution_address": "ArabianRanches 43, Dubai"}
 - slot{"institution_phone": "00413256889003"}
* thankyou
 - utter_goodbye

## story_5
* greet
 - utter_ask_howcanhelp
* make_appointment
 - utter_ask_name
* inform{"contact_name": "George"}
 - utter_ask_phone_number
* inform{"contact_phone": "388132398213"}
 - utter_ask_gender
* inform{"contact_gender": "Male"}
 - utter_ask_age
* inform{"contact_age": "45"}
 - utter_ask_institution
* inform{"institution_type":"Doctor"}
 - utter_ask_location
* inform{"contact_location":"Berlin"}
 - utter_ask_date
* inform{"date":"2 Jul"}
 - utter_ask_time
* inform{"time": "5 PM"}
 - action_search_institution
 - slot{"institution_name": "Dr Mueller"}
 - slot{"institution_address": "Gassestr 14, Berlin"}
 - slot{"institution_phone": "6123442412"}
* affirm
 - utter_ack_makeappointment
 - action_make_appointment
* thankyou
 - utter_goodbye

## story_6
* greet
 - utter_ask_howcanhelp
* search_institution
 - utter_ask_institution
* inform{"institution_type":"Clinic"}
 - utter_ask_location
* inform{"contact_location":"Amsterdam"}
 - action_search_institution
 - slot{"institution_name": "Clinic for the Diseased"}
 - slot{"institution_address": "Vondelparkstr 12, Amsterdam"}
 - slot{"institution_phone": "003618721992"}
* thankyou
 - utter_goodbye

## story_7
* greet
 - utter_ask_howcanhelp
* get_diagnose
 - utter_ask_symptoms
* inform{"symptom1": "fever"}
* inform{"symptom2": "headache"}
 - action_analyse_symptoms
* thankyou
 - utter_goodbye

## story_8
* greet
 - utter_ask_howcanhelp
* get_diagnose
 - utter_ask_symptoms
* inform{"symptom1": "bloating"}
* inform{"symptom2": "nausea"}
 - action_analyse_symptoms
* thankyou
 - utter_goodbye
