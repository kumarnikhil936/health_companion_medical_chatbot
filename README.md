# Health Companion as Part of the Freiburg Hackathon 2020
https://www.youtube.com/watch?v=uBWdI_2Q9yQ

**Inspiration**
> Inspiration is partly from the challenges of the Freiburg Hackathon 2020, as well as from our own values and desires.

**What it does**
> Provides solutions for appointments management, basic disease diagnostics and suggestions for treatment, interfacing the communication between users and services/institutions to make the overall process before seeing the doctor easier.

**Health Companion Web App and Mobile App Functionalities**

> HealthCompanion aims at optimizing the journey of an individual from the point of time any user would like to seek medical assistance. This is supported by an informed decision-making process, through a variety of functions including a chatbot, an appointment manager, modes of transportation, etc. 

> This application targets time optimization by helping users with early diagnosis and choosing the right professional and helps accommodate patients in vacant institutions. This is achieved by connecting individuals with health care institutes and adjacent services to ease communication.

> The process starts by the user communicating the symptoms and concerns to the associated Personal Companion which in our case is a chatbot. Analysis of the information will recommend the best advice based on the criticality of the case. 

> Nevertheless, if the user opts to visit a hospital, the app will start by providing information to help commute to the hospital.  Through the usage of a QR code that is generated, the required patient' information can be recorded and this helps to access the necessary services provided by the hospital. This limits the personal contact between the patient and health care staff.

**Design Prototype**

> To showcase the entire application, we have designed a prototype using Adobe XD, it includes a web-based application and a mobile application. The prototype helps better visualise the application with working components. Adobe XD provides cloud storage and backing up of files which played a key role to design the prototype by enabling better collaboration with the team members.


**Functionalities**

> Making an appointment:
The user can provide his/her location and other necessary details and the application will suggest a hospital/clinic/pharmacy in the vicinity, and later makes an appointment for him/her. Underneath it uses (proposed) GE Healthcare API to manage appointments. The functionality is built using Java, Java servlets and Hibernate as the middleware, and MySQL as the database. We also did unit testing in order to test the functionality of the component. It provides a dashboard which shows the availability of doctors and prompts the user for upcoming appointments.

> Analyse symptoms
The chatbot takes the symptoms from the user and runs machine learning classification algorithms to provide a probabilistic result on what the problem might be. It combines algorithms like Gaussian Naive-Bayes, Random Forrest and Decision Tree Classifiers, similar to [this project](https://github.com/Aniruddha-Tapas/Predicting-Diseases-From-Symptoms). 

> Search Institution
The user can provide his/her location information and the type of medical institution (hospital/clinic/pharmacy) s/he is looking for, and the chatbot application suggests the nearest possible match with availability information. 


**Chatbot**

> The chatbot is built on Python with the NLU based Rasa open-source machine learning framework, which uses the powerful Spacy library underneath. It can "understand messages, hold conversations, and connect to messaging channels and APIs." [Rasa](https://rasa.com/docs/rasa/)

> The bot can distinguish between time, date, and type of health institution. It can pick up names and contact details such as age, gender, location, and phone number of the user. The bot can also distinguish between symptoms.
With these pieces of information, it can perform actions such as _Make Appointment_, _Search Institution_, and _Analyse Symptoms_.
 
> The bot can provide information on the details of a made appointment. Such include the address, name and type of institution, date and time which correspond to that particular appointment. 


**Improvements and Future Work**

> Further improvement on the Chatbot would include adding more intents, example intent messages, more actions, more symptoms, and story samples - all of which are required for a good functioning bot. 

> _Make Appointment_ action needs to be properly adapted to the FHIR Appointment Architecture and the API of the GE Edison Digital Solutions for Scheduling (e.g. Appointment.status, Appointment.date, etc.).

> _Analyse Symptoms_ action needs to be fully integrated and improvement for better symptom analyzing APIs or ML Frameworks would be beneficial.


**How We built it**
> Python, Java, Adobe Premier Pro, Adobe Spark, Adobe XD, Spacy, GE Edison Digital Solutions, and more.

