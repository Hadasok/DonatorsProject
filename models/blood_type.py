class BloodType:
    def __init__(self, id, blood_type):
        self.blood_type = blood_type
        self.id = id

    def get_object(self):
        return {
            'id': self.id,
            'blood_type': self.blood_type
        }

