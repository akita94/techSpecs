TechSpecs Tracker
TechSpecs Tracker is a Python GUI application that displays detailed system information of the system it's running on. The application uses Tkinter for the user interface and modules like platform and psutil to fetch and display system information.

Features
Displays information about the operating system (name, version, architecture).
Displays details about the processor (model, frequency, number of cores).
Displays information about the RAM (total, available).
Displays details about the hard disk (total space, used space, free space, usage percentage).
Displays information about the power supply (simulated).
Displays details about the CPU cooling (simulated).
Displays details about the motherboard (on Windows only, using WMIC).
Displays details about the graphics card (on Windows only, using WMIC).
Displays details about the operating system (build name, installed updates).
Requirements
Python 3.x installed on your system.
The following modules need to be installed:
psutil
tkinter (usually included with Python)
Installation and Usage
Clone the repository:

bash
Copier le code
git clone https://github.com/yourusername/TechSpecs-Tracker.git
cd TechSpecs-Tracker
Install dependencies:
Make sure the required modules are installed:

bash
Copier le code
pip install psutil
Run the application:

bash
Copier le code
python TechSpecs.py
Usage:
Once the application is launched, it will display system details in a user-friendly interface.

Author
Add your author information here.

License
This project is licensed under the MIT License.
