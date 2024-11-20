import calendar

class AvailabilityGenerator:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        days_in_month = calendar.monthrange(year, month)[1] # returns a tuple with month, and # of days in that month, we store the # of days in this variable
        self.availability = {day: {"AM": "available", "PM": "available"} for day in range(1, days_in_month + 1)} # creates a dict with each day of the month being keys, and AM/PM avilability being the value, does this for the amount of days stored in the variable days_in_month

    # sets the availability for specified caregiver 
    def create_availability(self, day, shift, status, name):
        if day in self.availability and shift.upper() in self.availability[day]:
            self.availability[day][shift.upper()] = status
            print(f"{name} updated availability for Day {self.month}/{day}/{self.year}, {shift.upper()} shift to {status}.")
        else:
            print("Invalid day or shift. Use 'AM' or 'PM' for the shift.")
    
    # allows the user to view the monthky availability for the caregiver
    def display_availability(self, name):
        print(f"Availability for {name} in {calendar.month_name[self.month]},{self.year}:")
        for day, shifts in self.availability.items():
            print(f"{calendar.month_name[self.month]} {day}: \nAM - {shifts['AM']}\nPM - {shifts['PM']}")

    

class CareGivers:

    caregiver_info = {} # a dictionary that stores all the caregivers and ther information EX: Michael Girma:[3016548980, mike@gmail.com, 23, 8]

    def __init__(self, name, phone, email, hours_per_day, pay_rate=20):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.hours_per_day = hours_per_day
        self.month_availability = None # placeholder for avilability
    
    # generates the default availability for a specified month
    def create_monthly_availability(self, year, month):
        self.monthly_availability = AvailabilityGenerator(year, month) # all AM/PM shifts of everyday of the specified month are set to available
        print(f"{self.name}'s availability for {calendar.month_name[month]} {year} has been created.")
    
    # allows user to update avilability for specific days of the month
    def update_availability(self, day, shift, status):
        if self.monthly_availability:
            self.monthly_availability.create_availability(day, shift, status, self.name)
        else:
            print("Please create your monthly availability.")
    
    # allows user to view their avilability for a specified month
    def display_availability(self):
        if self.monthly_availability:
            self.monthly_availability.display_availability(self.name)
        else:
            print("Please create your monthly availability.")

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
        
