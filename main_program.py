# the main program
import calendar

# Class to manage caregiver availability
class AvailabilityGenerator:
    def __init__(self, year, month):
        self.year = year
        self.month = month
         # returns a tuple with month, and # of days in that month, we store the # of days in this variable
        days_in_month = calendar.monthrange(year, month)[1] 
         # creates a dict with each day of the month being keys, and AM/PM avilability being the value, does this for the amount of days stored in the variable days_in_month
        self.availability = {day: {"AM": "available", "PM": "available"}
                             for day in range(1, days_in_month + 1)}

    # Set availability for a specific day and shift
    def create_availability(self, day, shift, status, name):
        valid_statuses = ["preferred", "available", "unavailable"]
        if day in self.availability and shift.upper() in self.availability[day]:
            if status in valid_statuses:
                self.availability[day][shift.upper()] = status
                print(
                    f"{name} updated availability for Day {self.month}/{day}/{self.year}, {shift.upper()} shift to {status}.")
            else:
                print("Invalid status. Use 'preferred', 'available', or 'unavailable'.")
        else:
            print("Invalid day or shift. Use 'AM' or 'PM' for the shift.")

    # Allows the user to view the monthky availability for the caregiver
    def display_availability(self, name):
        print(
            f"Availability for {name} in {calendar.month_name[self.month]},{self.year}:")
        for day, shifts in self.availability.items():
            print(
                f"{calendar.month_name[self.month]} {day}: \nAM - {shifts['AM']}\nPM - {shifts['PM']}")


# A dictionary that stores all the caregivers and ther information EX: Michael Girma:[3016548980, mike@gmail.com, 23, 8]
class CareGivers:
    caregiver_info = {}  # Stores all caregivers' details

    def __init__(self, name, phone, email, hours_per_day, pay_rate=20):
        self.name = name
        self.phone = phone
        self.email = email
        self.pay_rate = pay_rate
        self.hours_per_day = hours_per_day
        self.monthly_availability = None # placeholder for avilability

    # Requirement 1: Add a caregiver
    # Generates the default availability for a specified month
    def add_caregiver(self): 
        CareGivers.caregiver_info[self.name.lower()] = [
            self.phone, self.email, self.hours_per_day, self.pay_rate]
        print("Caregiver has been added successfully!")

    # Allows user to edit any information about the caregives
    @classmethod # allows us to call method with name of the class and not an instance
    def edit_caregiver(cls, name):
        while True:
            edit_selection = input(
                "P to edit phone number, E to edit email, H to edit the amount of hours per day, X to cancel: ")
            if edit_selection.lower() == "p":
                new_phone_number = input(
                    "Please provide the new phone number: ")
                CareGivers.caregiver_info[name.lower()][0] = new_phone_number
                break
            elif edit_selection.lower() == "e":
                new_email = input("Please provide the new email: ")
                CareGivers.caregiver_info[name.lower()][1] = new_email
                break
            elif edit_selection.lower() == "h":
                new_hours = input(
                    "Please provide the new number of hours per day: ")
                CareGivers.caregiver_info[name.lower()][2] = int(new_hours)
                break
            elif edit_selection.lower() == "x":
                break
            else:
                print("Invalid input. Please try again.")

    # Allows user to delete a caregiver
    def delete_caregiver(self, name):
        if name.lower() in CareGivers.caregiver_info.keys():
            del CareGivers.caregiver_info[name.lower()]
            print(f"Caregiver {name.capitalize()} deleted successfully.")
        else:
            print("That caregiver does not exist!")

    # Allows user to view the caregivers
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

    # Requirement 2: Create monthly availability
    def create_monthly_availability(self, year, month):
        self.monthly_availability = AvailabilityGenerator(year, month)
        print(
            f"{self.name}'s availability for {calendar.month_name[month]} {year} has been created.")

    # Update caregiver availability
    def update_availability(self, day, shift, status):
        if self.monthly_availability:
            self.monthly_availability.create_availability(
                day, shift, status, self.name)
        else:
            print("Please create your monthly availability first.")

    # Display caregiver availability
    def display_availability(self):
        if self.monthly_availability:
            self.monthly_availability.display_availability(self.name)
        else:
            print("Please create your monthly availability first.")

    # Requirement 4: Calculate weekly and monthly pay
    def calculate_pay(self):
        if self.hours_per_day:
            weekly_pay = self.hours_per_day * 7 * self.pay_rate
            monthly_pay = weekly_pay * 4  # Approximation for 4 weeks in a month
            print(f"Weekly Pay for {self.name}: ${weekly_pay}")
            print(f"Monthly Pay for {self.name}: ${monthly_pay}")
        else:
            print(f"{self.name} has no hours specified.")

#Requirement 3:HTML For the Calendar
# Availability options
AVAILABILITY_OPTIONS = ["preferred", "available", "unavailable"]
# Caregivers schedule
class CareSchedule:
    def __init__(self):
        self.caregivers = {}
        self.schedule = self.create_default_schedule()

    # Default schedule for a week
    @staticmethod
    def create_default_schedule():
        schedule = {}
        for day in range(1, 8):  # 7 days a week (Mon-Sun)
            schedule[day] = {
                "7:00AM - 1:00PM": {"status": "available", "caregiver": None},
                "1:00PM - 7:00PM": {"status": "available", "caregiver": None},
            }
        return schedule

    # Add caregiver to the system
    def add_caregiver(self, name, phone, email, hours_per_day, pay_rate=20):
        self.caregivers[name.lower()] = {
            "phone": phone,
            "email": email,
            "hours_per_day": hours_per_day,
            "pay_rate": pay_rate,
        }
        print(f"Caregiver {name} added successfully!")

    # Assign a caregiver to a shift based on their availability
    def assign_shift(self, day, shift, caregiver_name, status):
        if caregiver_name.lower() in self.caregivers:
            self.schedule[day][shift] = {"status": status, "caregiver": caregiver_name}
            print(
                f"Shift on {calendar.day_name[day - 1]} {shift} assigned to {caregiver_name} as {status}."
            )
        else:
            print(f"Caregiver {caregiver_name} not found.")

    # Generate the HTML schedule
    def display_schedule_as_html(self):
        html_schedule = """
        <html>
        <head>
            <title>Care Schedule</title>
            <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }
                th, td {
                    border: 1px solid black;
                    padding: 10px;
                    text-align: center;
                }
                th {
                    background-color: #f2f2f2;
                }
                td {
                    height: 100px;
                    vertical-align: top;
                }
            </style>
        </head>
        <body>
            <h1>Weekly Care Schedule</h1>
            <table>
                <tr>
                    <th>Mon</th>
                    <th>Tue</th>
                    <th>Wed</th>
                    <th>Thu</th>
                    <th>Fri</th>
                    <th>Sat</th>
                    <th>Sun</th>
                </tr>
                <tr>
        """

        # Fill in the schedule
        for day in range(1, 8):
            morning = self.schedule[day]["7:00AM - 1:00PM"]
            afternoon = self.schedule[day]["1:00PM - 7:00PM"]
            html_schedule += f"<td><b>Morning:</b> {morning['status']} ({morning['caregiver'] or 'None'})<br>"
            html_schedule += f"<b>Afternoon:</b> {afternoon['status']} ({afternoon['caregiver'] or 'None'})</td>"

        html_schedule += """
                </tr>
            </table>
        </body>
        </html>
        """

        # Save to an HTML file
        with open("care_schedule.html", "w") as file:
            file.write(html_schedule)
        print("HTML care schedule generated successfully!")



class Driver:
    def __init__(self):
        self.availability_generator = AvailabilityGenerator(2024, 11)
        self.care_schedule = CareSchedule()

    def add_sample_caregivers(self):
        print("\n--- Adding Caregivers ---")
        self.care_schedule.add_caregiver("Amber", "3015551234", "amber@gmail.com", 8)
        self.care_schedule.add_caregiver("Michael", "3016548980", "mike@gmail.com", 6)

    def assign_shifts(self):
        print("\n--- Assigning Shifts ---")
        self.care_schedule.assign_shift(4, "7:00AM - 1:00PM", "Amber ", "preferred")
        self.care_schedule.assign_shift(6, "1:00PM - 10:00PM", "Michael", "available")
        self.care_schedule.assign_shift(3, "7:00AM - 1:00PM", "Amber", "preferred")
        self.care_schedule.assign_shift(1, "6:00AM - 2:00PM", "Michael","available")

    def manage_availability(self):
        print("\n--- Managing Availability ---")
        self.availability_generator.create_availability(5, "AM", "preferred", "Amber")
        self.availability_generator.create_availability(5, "PM", "preferred", "Amber")
        self.availability_generator.create_availability(2, "PM", "available", "Michael")
        self.availability_generator.display_availability("Amber")

    def generate_html_schedule(self):
        print("\n--- Generating HTML Schedule ---")
        self.care_schedule.display_schedule_as_html()

    def calculate_caregiver_pay(self):
        print("\n--- Calculating Caregiver Pay ---")
        for name, details in self.care_schedule.caregivers.items():
            caregiver = CareGivers(
                name.capitalize(),
                details["phone"],
                details["email"],
                details["hours_per_day"],
                details["pay_rate"],
            )
            caregiver.calculate_pay()

    def run(self):
        self.add_sample_caregivers()
        self.assign_shifts()
        self.manage_availability()
        self.calculate_caregiver_pay()
        self.generate_html_schedule()


# Main Program
if __name__ == "__main__":
    driver = Driver()
    driver.run()
