# network_python
Network Automation Scripts Collection
This collection contains a series of progressively complex Python scripts designed for network automation tasks. Each script is built upon the previous one, introducing new concepts and functionalities at each step.

Prerequisites
Python 3.x
Required Python libraries: netmiko, flask, smtplib, concurrent.futures, csv, email.mime.text, email.mime.application, email.mime.multipart, email.mime.base, os
Install the required libraries using the following command:
sh
Copy code
pip install -r requirements.txt
Scripts Overview
Part 1: Basic SSH Connection
Purpose: Connects to a single device via SSH and executes a show command.
Usage: Replace the IP address and command in the script with the desired values and run the script.
Part 2: Multiple Commands
Purpose: Executes multiple commands on a single device.
Usage: Replace the IP address and list of commands in the script with the desired values and run the script.
Part 3: Multiple Devices
Purpose: Executes multiple commands on multiple devices.
Usage: Replace the list of IP addresses and commands in the script with the desired values and run the script.
Part 4: Reading Devices from a File
Purpose: Reads a list of devices from a file and executes multiple commands on each device.
Usage: Replace the filename, IP addresses, and commands in the script with the desired values and run the script.
Part 5: Output to a File
Purpose: Executes multiple commands on multiple devices and writes the output to a file.
Usage: Replace the filename, IP addresses, and commands in the script with the desired values and run the script.
Part 6: Output to a CSV File
Purpose: Executes multiple commands on multiple devices and writes the output to a CSV file.
Usage: Replace the filename, IP addresses, and commands in the script with the desired values and run the script.
Part 7: Error Handling
Purpose: Introduces error handling to manage failed connections or command executions.
Usage: Replace the filename, IP addresses, and commands in the script with the desired values and run the script.
Part 8: Interactive Command Entering
Purpose: Allows the user to interactively enter the show commands.
Usage: Run the script and follow the prompts to enter the commands.
Part 9: Function Usage
Purpose: Refactors the script to use functions, improving code organization and readability.
Usage: Replace the filename, IP addresses, and commands in the script with the desired values and run the script.
Part 10: Multithreading
Purpose: Implements multithreading to execute commands on multiple devices simultaneously.
Usage: Replace the filename, IP addresses, and commands in the script with the desired values and run the script.
Part 11: Email Results
Purpose: Executes multiple commands on multiple devices and emails the results as a CSV file.
Usage: Replace the email address, filename, IP addresses, and commands in the script with the desired values and run the script.
Part 20: Flask Hello World
Purpose: Creates a basic Flask web application that returns "Hello, World!".
Usage: Run the script and access the application at http://localhost:9443/.
Part 21: Flask with Form Submission
Purpose: Extends the Flask application to render an HTML form and handle form submissions.
Usage: Run the script, access the application at http://localhost:9443/cmds, and submit the form.
Part 22: Flask with Command Runner
Purpose: Integrates the Flask application with the command runner to execute commands on form submission.
Usage: Run the script, access the application at http://localhost:9443/cmds, enter the required information in the form, and submit it.
Conclusion
This collection provides a comprehensive introduction to network automation using Python, covering basic to advanced topics. Each script is standalone but builds upon the concepts introduced in the previous ones. Users are encouraged to modify and extend these scripts to suit their specific needs and environment.

This README provides a concise overview of each script and its usage. You can expand each section with more details, examples, and any additional instructions as needed.
