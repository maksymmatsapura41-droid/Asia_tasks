class Report:
    def __init__(self, data):
        self.data = data

    def calculate_stats(self):
        return sum(self.data)/len(self.data)

class ReportSaver:
    def save_to_file(self, report, filename):
        with open(filename, 'w') as f:
            f.write(str(report.data))

class EmailSender:
    def send_email(self, report, email):
        print(f"Sending report to {email}")
