# KeystrokeInspector
## 1. Introduction:
The Improved Keylogger is a Python script designed for keystroke monitoring on a host system. This program captures user keystrokes and periodically sends them via email to a specified address. It uses the pynput library for keyboard monitoring and smtplib for email communication.
## 2. Key Features:
+ **Stealth Operation:** The keylogger operates discreetly in the background without user awareness.
+ **Email Reporting:** Captured keystrokes are sent via email to a designated address at regular intervals.
+ **Customizable Reporting Interval:** Users can configure the reporting interval based on their preferences.
+ **Dynamic Key Handling:** The script handles both character and non-character key presses intelligently.
## 3. Implementation:
+ **Class Structure:** The keylogger is implemented as a class, ImprovedKeyLogger, with methods for handling key events, appending to logs, sending emails, and reporting.
+ **Threading:** Threading is used to create a timer that periodically triggers the email reporting function.
+ **Exception Handling:** The script includes basic exception handling to manage errors during email sending.
## 4. Code Walkthrough:
+ **Initialization:** The class is initialized with parameters for reporting interval, target email address, and sender's email credentials.
+ **Key Press Handling:** The on_key_press method processes key presses, handling both character and non-character keys. Special keys like space and escape are appropriately managed.
Log Management: The append_to_log method appends the processed key to the log.
+ **Email Sending:** The send_email method uses the smtplib library to send an email with the accumulated log to the specified email address.
+ **Reporting Loop:** The report_and_send_email method sends an email if there are logged keystrokes and schedules itself to run after a specified interval.
+ **Logging Start:** The start_logging method initializes the keyboard listener and starts the reporting loop.
## 5. Usage:
Example Usage: The script demonstrates its usage by initializing an instance of the ImprovedKeyLogger class with a target email address, sender's email password, and reporting interval. The start_logging method is then called to begin the keystroke monitoring.
## 6. Security and Ethical Considerations:
+ **User Consent:** Keystroke logging raises ethical concerns. It should only be used with explicit consent and for legitimate purposes.
+ **Secure Email Credentials:** Storing and transmitting email credentials should be done securely. Consider using secure methods and encryption.
## 7. Conclusion:
The Improved Keylogger with Email Reporting provides a simple yet powerful tool for monitoring keystrokes on a system. Its discreet operation and email reporting feature make it suitable for scenarios where user activity tracking is necessary, with proper ethical considerations and user consent.

