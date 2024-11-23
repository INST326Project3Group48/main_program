# INST326 OOP Project 03

By: Amber Lin, Vashawn Robinson, Michael Girma

## The Project

Everyone will do the same project this time. This is a group project, so you must work in your assigned groups. Include the link to your group's GitHub repository (one link per group). 
Use comments in your code to document your solution. If you need to write comments to the grader, add a markdown cell immediately above your code solution and add your comments there. 
Be sure to read and follow all the requirements and the Notebook Instructions at the bottom of this notebook. Your grade may depend on it!


## 1. A Scheduling Program

My wife is responsible for scheduling caregivers for her 93 year-old mother. Currently she writes out the schedule on a monthly calendar and photocopies it for everyone. 
I want all of you to help me write a program to help her with scheduling. While this is a specific application, this program will be broadly useful and adaptable to any scheduling needs for small businesses, clubs, and more.

## Requirements 

Care is required 12 hours per day, 7 days a week. There are two shifts each day: 7:00 AM - 1:00 PM, and 1:00 PM to 7:00 PM. There are a total of 8 caregivers. Some are family members and some are paid. 
Each caregiver has their own availability for shifts that is generally the same from month to month, but there are exceptions for work, vacations, and other responsibilities. Your program should do the following:

1. Manage caregivers and their schedules. Attributes include: name, phone, email, pay rate, and hours.
2. Each caregiver should have their own availability schedule where they can indicate their availability for each shift. Availability categories are 'preferred', 'available' (default), and 'unavailable'.
3.  Create a care schedule that covers AM and PM shifts and displays caregiver names on a calendar (see example). The schedule should accomodate caregivers' individual schedules and availability preferences. The python calendar module provides options for creating HTML calendars. Sample code for the HTML calendar is in the project folder.
4.  Paid caregivers are paid weekly at $20/hr. Your program should calculate weekly pay based on assigned hours. Provide a separate pay report that lists weekly (gross: hours x rate) amounts to each caregiver, along with weekly and monthly totals. The report can be a text document, or presented in GUI or HTML format.

## Group Requirements 

1. Your submitted project should follow OOP principles like abstraction, encapsulation, inheritance, and polymorphism as appropriate. Your program should use classes.
2. Select a group leader who will host the group's project repository on their GitHub.
3. Create the group repository and add a main program document. See example.
4. Create branches off the main program for each group member, and assign part of the program to each member.
5. Each member should work on their branch.
6. When each member is finished, merge the branches back into the main program. You may use 'merge' or 'pull requests', your choice.
7. iterate and debug as necessary.

### Working With HTML
Since this is a course on python, not HTML, you are not expected to know HTML. 
Therefore, you may copy applicable portions of the sample code or use AI to write the HTML portions of your application. Ypu should write the main python code yourself.

### What You Need To Turn In

1. Include your group number and the names of all group members in the signature block at the top of this notebook.
2. In the cell below, paste the link to your project repository. One link per group. The grader will review the activity and history provided by GitHub. To add a hyperlink to a Jupyter markdown cell, follow the instructions in the cell below.
3. Below the GitHub Repository Link cell is a code cell. Copy and paste your final program code into this cell.


### GitHub Repository Link

Example: [INST326_Fall2024/Projects/Project03](https://github.com/sdempwolf/INST326_Fall_2024/tree/main/Projects/Project03) 

Edit the link code below with your information, then run this cell. Test the link! It should take you to your GitHub project repository.
> [external link text](http://url_here)


## NoteBook Instructions 

Before turning in your notebook

1. Make sure you have renamed the notebook file as instructed
2. Make sure you have included your signature block and that it is correct according to the instructions
3. Comment your code as necessary
4. Run all code cells and double check that they run correctly. If you can't get your code to run correctly and you want partial credit, add a note for the grader in a new markdown cell directly above your code solution.

Turn in your notebook by uploading it to ELMS<br>
IF the exercises involve saved data files, put your notebook and the data file(s) in a zip folder and upload the zip folder to ELMS


