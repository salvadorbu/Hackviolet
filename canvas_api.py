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
            course_id = assignment.assignment['course_id']
            assignment_id = assignment.assignment['id']
            url = assignment.assignment['html_url']

            assignments.append((assignment.assignment['name'], due_date, url, course_id, assignment_id))

        return assignments
    
    def submit_assignment(self, course_id, assignment_id, submit_file):
        course = self.canvas.get_course(course_id)
        assignment = course.get_assignment(assignment_id)
        assignment.submit({"submission_type": "online_upload"}, file=submit_file)


if __name__ == "__main__":
    url = "https://canvas.vt.edu"
    key = "4511~CSBkFbb31upwYZYNHWfENaVnF0xOdXbGPl9Kr55rDC5M4y3hr0QMx8wkvbLHQIxs"
    bot = CanvasBot(url, key)
    file = open("C:\\Users\\salva\\Downloads\\submission.pdf", mode="rb")
    ass = bot.get_assignements()
    bot.submit_assignment(167776, 1690075, file)