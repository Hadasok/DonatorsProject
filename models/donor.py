from datetime import datetime
from .blood_type import BloodType
from .donation import Donation


class Donor:

    def __init__(self, email, name, birthdate, gender, blood_type, donations, phone):
        self.email = email
        self.name = name
        self.birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        self.gender = 1 if gender == 'זכר' else 0
        self.blood_type = int(BloodType(blood_type))
        self.donations = [int(Donation(donation)) for donation in donations]
        self.phone = phone



    def get_object(self):
        return (
            self.email,
            self.name,
            self.gender,
            self.birthdate,
            self.phone,
            self.blood_type,
        )