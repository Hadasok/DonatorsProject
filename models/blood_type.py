from database import Database


class BloodType:

    query = 'SELECT * FROM BloodTypes'
    bloodtype_id_dic = {bloodtype.Blood: bloodtype.ID for bloodtype in Database.send_query(query)}

    def __init__(self, blood_type):
        self.blood_type = blood_type
        self.id = (
            BloodType.bloodtype_id_dic[blood_type]
            if blood_type in BloodType.bloodtype_id_dic
            else BloodType.bloodtype_id_dic['UNKNOWN']
        )

    def __int__(self):
        return int(self.id)

    def get_object(self):
        return {
            'id': self.id,
            'blood_type': self.blood_type
        }

