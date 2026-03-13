import os
from datetime import datetime


class TestReporter:
    def __init__(self, test_name):
        self.test_name = test_name
        self.timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        os.makedirs("reports", exist_ok=True)
        os.makedirs("screenshots", exist_ok=True)

        self.report_path = f"reports/{self.test_name}_{self.timestamp}.txt"
        self.report_file = open(self.report_path, "w", encoding="utf-8")

        self.write_line("=" * 60)
        self.write_line(f"Test Name : {self.test_name}")
        self.write_line(f"Start Time: {self.timestamp}")
        self.write_line("=" * 60)

    def write_line(self, text):
        print(text)
        self.report_file.write(text + "\n")

    def attach_result(self, result, details=""):
        self.write_line(f"Result    : {result}")
        if details:
            self.write_line(f"Details   : {details}")

    def close(self):
        self.write_line("=" * 60)
        self.report_file.close()

        