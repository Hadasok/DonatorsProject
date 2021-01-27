from database import Database


class Donation:
    query = 'SELECT * FROM Donations'
    donations_id_dic = {
        donation.Donation: {'id': donation.ID, 'description': donation.Description}
        for donation in Database.send_query(query)
    }

    def __init__(self, donation):
        self.id = Donation.donations_id_dic[donation]['id']
        self.donation = donation
        self.description = Donation.donations_id_dic[donation]['description']

    def __int__(self):
        return int(self.id)

    def get_object(self):
        return {
            'id': self.id,
            'donation': self.donation,
            'description': self.description
        }