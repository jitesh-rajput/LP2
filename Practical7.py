# Expert System for Hospitals and Medical Facilities

def find_medical_facilities(symptoms):
    # Define the rules for matching symptoms with medical facilities
    rules = {
        'fever': ['Hospital', 'Clinic'],
        'cough': ['Hospital', 'Clinic'],
        'headache': ['Clinic'],
        'stomach pain': ['Hospital'],
        'injury': ['Emergency Room'],
    }

    facilities = set()
    #for symptom in symptoms:
    if symptoms in rules:
        facilities.update(rules[symptoms])

    if facilities:
        print("Based on your symptoms, we recommend the following medical facilities:")
        for facility in facilities:
            print("- " + facility)
    else:
        print("We couldn't find any specific medical facilities for your symptoms.")

# Example usage
user_symptoms = input("Enter your symptoms :- ")
find_medical_facilities(user_symptoms)
