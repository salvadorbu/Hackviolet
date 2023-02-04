from canvasapi import Canvas

class CanvasBot:
    def __init__(self, url, key) -> None:
        self.canvas = Canvas(url, key)
        self.user = self.canvas.get_current_user()

    def get_user(self):
        return self.user        

    def get_assignements(self):
        assignments = []
        for assignment in self.canvas.get_todo_items()._get_next_page():
            due_date = str(assignment.assignment['due_at'])
            due_date = f"{due_date[5:7]}/{due_date[8:10]}"

            url = assignment.assignment['html_url']

            assignments.append((assignment.assignment['name'], due_date, url))

        print(assignments)
        return assignments


if __name__ == "__main__":
    url = "https://canvas.vt.edu"
    key = "4511~CSBkFbb31upwYZYNHWfENaVnF0xOdXbGPl9Kr55rDC5M4y3hr0QMx8wkvbLHQIxs"
    bot = CanvasBot(url, key)

    bot.get_assignements()