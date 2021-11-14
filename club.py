class Club:
    club_details = ["name", "city", "address", "timings", "slots"]

    # def __init__(self, **kwargs):
    #     self.name = kwargs.name
    #     self.city = kwargs.city
    #     self.address = kwargs.address
    #     self.timings = kwargs.timings
    #
    #     # To-Do: Remove slots from class
    #     self.slots = self.getSlots(self.timings)

    @classmethod
    def register_club(cls):
        new_club = {}

        print("Please enter club details: ")
        for item in cls.club_details:
            if item != 'slots':
                new_club[item] = input(f"Enter club {item}: ")
        # print(new_club)
        new_club['slots'] = cls.slots(new_club['timings'])
        return new_club

    @staticmethod
    def slots(timings):
        # print(timings)
        slots_available = timings.split('-')
        count = 0
        slots_ava = []
        # print(slots_available)
        for slot in range(int(slots_available[0]), int(slots_available[1])):
            count += 1
            # print(f"{count} : {slot} - {slot + 1}")
            slots_ava.append(f"{slot} - {slot + 1}")
        return slots_ava

    @staticmethod
    def getSlots(timings):
        timings = timings.replace(' ', '').replace('/', '-')
        timing = timings.split('-')
        # 10 - 18  (10 am to 6pm)
        slots_available = []
        for slot in timing:
            slots_available.append(slot)
        return slots_available
