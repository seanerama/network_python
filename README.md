# Network Automation Scripts Collection 🌐

## Overview 🌟
This repository houses a series of Python scripts designed to teach how to automate various network administration tasks, each script increases in complexity and functionality. The scripts leverage libraries like Netmiko for establishing SSH connections to network devices and Flask for rendering a user-friendly web interface.

## 📁 Repository Contents

### 🛠️ Basic Network Interaction Scripts
1. **Part 1:** Initiates a simple SSH connection to a device, executes a 'show' command, and prints the result.
2. **Part 2:** Builds upon Part 1 by allowing the execution of multiple 'show' commands.
3. **Part 3:** Extends functionality to handle multiple devices.
4. **Part 4:** Introduces reading IP addresses from a text file.
5. **Part 5:** Outputs the results to a file.
6. **Part 6:** Outputs the results to a CSV file.
7. **Part 7:** Implements error handling for SSH connections and command executions.
8. **Part 8:** Allows interactive command entering.
9. **Part 9:** Refactors the script to use functions, enhancing readability and maintainability.
10. **Part 10:** Introduces multithreading for concurrent processing of multiple devices.
11. **Part 11:** Adds the capability to email the results to the user.

### 🌐 Flask Web Application
20. **Part 20:** A 'Hello World' Flask app, serving as an introduction to Flask.
21. **Part 21:** Enhances the Flask app to render templates and handle form submissions.
22. **Part 22:** Integrates the Flask app with the network command runner, allowing users to input commands and IP addresses and receive results via the web interface.

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Pip (Python Package Installer)

### Installation
1. Clone this repository to your local machine.
   ```sh
   git clone seanerama/network_python
