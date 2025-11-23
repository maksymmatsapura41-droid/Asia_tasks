class ReportManager:
    def __init__(self, data):
        self.data = data

    def calculate_stats(self):
        return sum(self.data)/len(self.data)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self.data))

    def send_email(self, email):
        print(f"Sending report to {email}")
