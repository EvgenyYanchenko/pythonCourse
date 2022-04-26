class House():
    """Описание дома"""
    def __init__(self, street, number):
        """Свойства дома"""
        self.street = street
        self.number = number
        self.pod = 1

    def build(self):
        """Строим дом"""
        print("Dom na ulice "+self.street+", nomer "+self.number+" imeet "+str(self.pod)+" podjezdov.")


class ProspectHouse(House):
    def __init__(self, prospect, number):
        super().__init__(self,number)
        self.prospect = prospect

housePr1 = ProspectHouse("Masherova",22)


print(housePr1.number)



