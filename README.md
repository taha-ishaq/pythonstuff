AccountTester Tool
This is a simple Python tool to test accounts using a provided username and password list. Please follow the instructions below to set up and use the tool.

Requirements
Before using the tool, ensure that you have Python installed on your system.

1. Install Python
If you don’t have Python installed, download and install it from the official website:
Download Python

Make sure to add Python to your system's PATH during installation.

2. Install Required Libraries
Once Python is installed, you need to install the required libraries. You can do this by running the following command in your project directory:

bash
Copy
Edit
pip install -r requirements.txt
This will install all the necessary dependencies for the tool to function properly.

Usage
1. Open the Tool
Navigate to the folder where the tool files are located and run the following command to start the tool:

bash
Copy
Edit
python AccountTester.py
2. Input Username
When prompted, enter the username you want to test.

3. Provide the Password File Path
The tool will ask for a password file path. If you have a custom password list, provide the full path to that file.

If you don’t have a custom password list, you can simply use the default password.txt file that is included with the tool. Just provide the path to the file, which will be in the same folder as AccountTester.py by default.

4. Wait for the Process to Complete
This process may take some time depending on the number of passwords to test and the speed of your connection. Do not turn off your computer while the tool is running, as it may cause incomplete testing.

Important Notes
Make sure to have the correct paths for the password file if you are using a custom one.
The tool might take some time to complete depending on the number of passwords in the list.
