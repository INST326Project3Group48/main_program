# the main program

class CareGivers:

    caregiver_info = {} # a dictionary that stores all the caregivers and ther information EX: Michael Girma:[3016548980, mike@gmail.com, 23, 8]

    def __init__(self, name, phone, email, hours_per_day, pay_rate=20):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.hours_per_day = hours_per_day

    # adds the instance of the class to our dictionary 
    def add_caregiver(self):
        CareGivers.caregiver_info[self.name.lower()] = [self.phone, self.email, self.hours_per_day, self.pay_rate]
        print("Caregiver has been added succesfully!")
    
    # allows user to edit any information about the caregives
    @classmethod # allows us to call method with name of the class and not an instance
    def edit_caregiver(cls, name):
        while True:
            edit_selection = input("P to edit phone number, E to edit email, H to edit the amount of hours per day, X to cancel")
            if edit_selection.lower() == "p":
                new_phone_number = input("please provide the new phone number.")
                CareGivers.caregiver_info[name.lower()][0] = new_phone_number
                break
            elif edit_selection.lower() == "e":
                new_email = input("Please provide the new email.")
                CareGivers.caregiver_info[name.lower()][1] = new_email
                break
            elif edit_selection.lower() == "h":
                new_hours = input("Please provide the new amount of hours that the specified caregiver will work.")
                CareGivers.caregiver_info[name.lower()][2] = new_hours
                break
            elif edit_selection.lower() == "x":
                break
            else:
                print("Please provide a valid character to edit the specified caregivers information.")
    
    # allows user to delete a caregiver
    def delete_caregiver(self, name):
        if name.lower() in CareGivers.caregiver_info.keys():
            del CareGivers.caregiver_info[name]
        else:
            print("That caregiver does not exist!")
    
    # allows user to view the caregivers
    @classmethod # allows us to call method with name of the class and not an instance
    def display_caregivers(cls):
        if not CareGivers.caregiver_info:
            print("No caregivers available")
            return

        print("CareGivers")
        print("-" * 50)
        for name, caregiver_info in CareGivers.caregiver_info.items():
            print(f"Name: {name.capitalize()}")
            print(f"Phone: {caregiver_info[0]}")
            print(f"Email: {caregiver_info[1]}")
            print(f"Hours/Day: {caregiver_info[2]}")
            print(f"Pay Rate: ${caregiver_info[3]}/hour")
            print("-" * 50)

# Example Instances Below
# caregiver1 = CareGivers("John Doe", "123-456-7890", "john@example.com", 8)
# caregiver2 = CareGivers("Jane Smith", "987-654-3210", "jane@example.com", 6)
# caregiver3 = CareGivers("Emily Smith", "987-654-3210", "emily@example.com", 7)
# caregiver4 = CareGivers("Michael Smith", "987-654-3210", "michael@example.com", 5)

# caregiver1.add_caregiver()
# caregiver2.add_caregiver()
# caregiver3.add_caregiver()
# caregiver4.add_caregiver()

# CareGivers.edit_caregiver("Emily Smith")

# CareGivers.display_caregivers()