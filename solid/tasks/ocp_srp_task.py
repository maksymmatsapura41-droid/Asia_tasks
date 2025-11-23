class Report:
    def __init__(self, data, report_type):
        self.data = data
        self.report_type = report_type

    def process(self):
        stats = sum(self.data) / len(self.data)
        if self.report_type == "text":
            content = f"Text Report\nStats: {stats}\nData: {self.data}"
        elif self.report_type == "pdf":
            content = f"PDF Report\nStats: {stats}\nData: {self.data}"
        elif self.report_type == "html":
            content = f"<h1>HTML Report</h1><p>Stats: {stats}</p>"
        else:
            raise ValueError("Unknown report type")

        with open(f"report.{self.report_type}", "w") as f:
            f.write(content)

        print(f"Sending {self.report_type} report via email...")
