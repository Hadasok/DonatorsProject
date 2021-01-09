class Donation:
    def __init__(self, id, donation, description):
        self.id = id
        self.donation = donation
        self.description = description

    def get_object(self):
        return {
            'id': self.id,
            'donation': self.donation,
            'description': self.description
        }