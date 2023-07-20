class FeedType:
    """
    FeedType.
    """
    def __init__(self, ration, name, amount, ts):
        self.ration = ration
        self.name = name
        self.amount = amount
        self.ts = ts
    
    def to_json(self):
        return {
            'ration': self.ration.to_json(),
            'name': self.name,
            'amount': self.amount,
            'ts': self.ts
        }