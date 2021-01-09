class Donor:
    def __init__(self, timestamp, email, name, birthdate, gender, blood_type, donations, phone):
        self.timestamp = timestamp
        self.email = email
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.blood_type = blood_type
        self.donations = donations
        self.phone = phone

    def get_object(self):
        return {
            'timestamp': self.timestamp,
            'email': self.email,
            'name': self.name,
            'birthdate': self.birthdate,
            'gender': self.gender,
            'blood_type': self.blood_type,
            'donations': self.donations,
            'phone': self.phone
        }