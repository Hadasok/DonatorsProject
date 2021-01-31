from datetime import datetime
from .blood_type import BloodType
from .donation import Donation


class Request:

    def __init__(self, description, email, date,  blood_types, donations, phone):
        self.description = description
        self.email = email
        self.date = date
        self.blood_types = [int(BloodType(blood_type)) for blood_type in blood_types]
        self.donations = [Donation(donation) for donation in donations]
        self.phone = phone

    def create_blood_types_filter(self):
        str_blood_types = '('

        # Check if all blood types are included (All blood types except for unknown type
        # or unknown blood type itself in blood types list)
        if len(self.blood_types) >= BloodType.bloodtypes_count - 1 or\
           0 in self.blood_types or\
           len(self.blood_types) == 0:
            return None

        if len(self.blood_types) >= 1:
            str_blood_types += '(Donors.BloodType = {}) '.format(self.blood_types[0])

        for index in range(1, len(self.blood_types)):
            str_blood_types += 'OR (Donors.BloodType = {})'.format(self.blood_types[index])

        str_blood_types += ')'

        return str_blood_types

    def create_donations_filter(self):
        str_donations = '('

        if len(self.donations) == Donation.donations_count or len(self.donations) == 0:
            return None

        if len(self.donations) >= 1:
            str_donations += '(DonorsDonations.DonationID = {}) '.format(self.donations[0].id)

        for index in range(1, len(self.donations)):
            str_donations += 'OR (DonorsDonations.DonationID = {})'.format(self.donations[index].id)

        str_donations += ')'

        return str_donations

    def create_sql_query(self):
        sql_query = 'SELECT DISTINCT Donors.Email, Donors.Name FROM Donors, BloodTypes, DonorsDonations WHERE (DonorsDonations.DonorsEmail = Donors.Email)'
        donation_filter = self.create_donations_filter()
        blood_filter = self.create_blood_types_filter()
        sql_query += ' AND {}'.format(donation_filter) if donation_filter else ''
        sql_query += ' AND {}'.format(blood_filter) if blood_filter else ''

        return sql_query

    def get_donation_description(self):
        donation_str = ''
        if len(self.donations) >= 1:
            donation_str = self.donations[0].donation

        for index in range(1, len(self.donations)):
            donation_str += ', ' + self.donations[index].donation

        return ('{}' + '\n\n' + 'תיאור התרומה:' + '\n' + '{}').format(donation_str, self.description)

    def get_contact_details(self):
        return '{}\n{}'.format(self.phone, self.email)

    def __repr__(self):
        donation_request_details = (
            'נודה להתגייסותך לתרומת דם נדרשת:' + '\n\n' +
            '{}' + '\n\n' +
            'הבקשה בתוקף עד תאריך:' + '\n' +
            '{}' + '\n\n' +
            'פרטים ליצירת קשר:'+ '\n' +
            '{}' + '\n\n' +
            'תודה על היותך חלק ממאגר התורמים.'
        ).format(self.get_donation_description(), self.date, self.get_contact_details())

        return donation_request_details
