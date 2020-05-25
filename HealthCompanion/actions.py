from rasa_sdk import Action
from rasa_sdk.events import SlotSet


def search(institution_type, contact_location, dispatcher):
    """
    Suggest a pharmacy in the proximity to contact_location.
    :param dispatcher:
    :param institution_type:
    :param contact_location:
    :return:
    """
    if institution_type == "pharmacy":
        institution_name = "City Pharmacy"
        institution_address = "City Strasse, Paderborn"
        institution_phone = "12323457890"
        dispatcher.utter_message(text="Found a {} named {} on {}. The contact number is {}".format(institution_type,
                                                                                                   institution_name,
                                                                                                   institution_address,
                                                                                                   institution_phone))
    else:
        # for all other institutions
        institution_name = "City Hospital"
        institution_address = "City Strasse, Paderborn"
        institution_phone = "12332227890"
        dispatcher.utter_message(text="Found a {} named {} on {}. The contact number is {}".format(institution_type,
                                                                                                   institution_name,
                                                                                                   institution_address,
                                                                                                   institution_phone))
        return institution_name, institution_address, institution_phone


def make_appointment(institution_name, contact_name, contact_age, contact_phone, contact_gender, date, time,
                     dispatcher):
    """
    Make appointment in the given hospital for the contact.
    :param dispatcher:
    :param institution_name:
    :param contact_name:
    :param contact_age:
    :param contact_phone:
    :param contact_gender:
    :param date:
    :param time:
    :return:
    """
    appointment_status = "approved"
    dispatcher.utter_message(text="Appointment done for {} in {} for {} {}".format(contact_name,
                                                                                   institution_name, date, time))
    # make a call to some API to actually book the appointment.
    return appointment_status


def diagnose_symptoms(symptom1, symptom2=None, symptom3=None, dispatcher=None):
    """
    Diagnose symptoms and suggest what might be wrong.
    :param dispatcher:
    :param symptom1:
    :param symptom2:
    :param symptom3:
    :return:
    """
    # symptom1 can't be empty or None
    flu_symptoms = [None, "headache", "fever", "chills", "cough", "sore throat", "runny nose", "fatigue"]
    diarrhea_symptoms = [None, "nausea", "bloating", "loose stools", "abdominal pain", "abdominal cramps"]
    diagnosis_results = "I am not sure. Please see a doctor!"

    if symptom1 in flu_symptoms[1:] and symptom2 in flu_symptoms and symptom3 in flu_symptoms:
        diagnosis_results = "This looks like Flu to me"
    elif symptom1 in diarrhea_symptoms[1:] and symptom2 in diarrhea_symptoms and symptom3 in diarrhea_symptoms:
        diagnosis_results = "It looks like you have got Diarrhea"

    return diagnosis_results


def greet_user(contact_gender, contact_name):
    """
    Greet the user.
    :param contact_gender:
    :param contact_name:
    :return:
    """
    attribute = "handsome" if contact_gender == "Male" else "beautiful"
    return "Hi {}, Good day! You look {} as ever.".format(contact_name, attribute)


class ActionSearchInstitution(Action):
    """
    Search for a hospital, pharmacy, specialist, etc.
    """

    def name(self):
        """
        Return name.
        :return:
        """
        return "action_search_institution"

    def run(self, dispatcher, tracker, domain):
        """
        Run API.
        :param dispatcher:
        :param tracker:
        :param domain:
        :return:
        """
        institution_type = tracker.get_slot("institution_type")
        contact_location = tracker.get_slot("contact_location")

        dispatcher.utter_message(text="Looking for a {} near you!".format(institution_type))

        institution_name, institution_address, institution_phone = search(institution_type, contact_location,
                                                                          dispatcher)
        return [SlotSet("institution_name", institution_name),
                SlotSet("institution_address", institution_address),
                SlotSet("institution_phone", institution_phone)]


class ActionMakeAppointment(Action):
    """
    Make appointments.
    """

    def name(self):
        """
        Return name.
        :return:
        """
        return "action_make_appointment"

    def run(self, dispatcher, tracker, domain):
        """
        Run API.
        :param dispatcher:
        :param tracker:
        :param domain:
        :return:
        """
        contact_name = tracker.get_slot("contact_name")
        contact_age = tracker.get_slot("contact_age")
        contact_gender = tracker.get_slot("contact_gender")
        contact_phone = tracker.get_slot("contact_phone")
        institution_name = tracker.get_slot("institution_name")
        date = tracker.get_slot("date")
        time = tracker.get_slot("time")

        dispatcher.utter_message(text="Making an appointment for you!")

        appointment_status = make_appointment(institution_name, contact_name, contact_age, contact_phone,
                                              contact_gender, date, time, dispatcher)
        return [SlotSet("appointment_status", appointment_status)]


class ActionAnalyseSymptoms(Action):
    """
    Analyse the symptoms.
    """

    def name(self):
        """
        Return name.
        :return:
        """
        return "action_analyse_symptoms"

    def run(self, dispatcher, tracker, domain):
        """
        Run API.
        :param dispatcher:
        :param tracker:
        :param domain:
        :return:
        """
        symptom1 = tracker.get_slot("symptom1")
        symptom2 = tracker.get_slot("symptom2")
        symptom3 = tracker.get_slot("symptom3")
        contact_name = tracker.get_slot("contact_name")

        diagnosis_results = diagnose_symptoms(symptom1, symptom2, symptom3, dispatcher)

        dispatcher.utter_messege(text="Hey {}, {}".format(contact_name, diagnosis_results))

        return [SlotSet("diagnosis_results", diagnosis_results)]


class ActionGreetUser(Action):
    """
    Greets the user using his name.
    """

    def name(self):
        """
        Returns name.
        :return: 
        """
        return "action_greet_user"

    def run(self, dispatcher, tracker, domain):
        """
        Run API.
        :param dispatcher: 
        :param tracker: 
        :param domain: 
        :return: 
        """
        contact_name = tracker.get_slot("contact_name")
        contact_gender = tracker.get_slot("contact_gender")

        if contact_name is None or contact_gender is None:
            greeting = "Hello, Good day!"
            return [SlotSet("greeting", greeting)]

        greeting = greet_user(contact_gender, contact_name)

        return [SlotSet("greeting", greeting)]
