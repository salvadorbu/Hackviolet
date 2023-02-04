from canvasapi import Canvas
import datetime
from datetime import date
class CanvasBot:
    def __init__(self, url, key) -> None:
        self.canvas = Canvas(url, key)
        self.user = self.canvas.get_current_user()

    def get_user(self):
        return self.user

    def is_current_semester(self, created_date):
        year = st[0:4]
        month = st[5:7]
        semester = ""

        if month == ("06" or "07"):
          semester = "Fall"
        else:
            semester = "Spring"
            year = str(int(year))
        return self.sem_to_string(str(date.today())) == self.sem_to_string(created_date)
    
    def get_courses(self):
        paginated = self.user.get_courses()._get_next_page()
        courses = []
        for p in paginated:
            try:
                courses.append((str(p.created_at_date), p.id))
            except:
                pass
        return courses
        

    def get_assignements(self):
        assignments = self.canvas.get_todo_items()._get_next_page()
        


if __name__ == "__main__":
    url = "https://canvas.vt.edu"
    key = "4511~CSBkFbb31upwYZYNHWfENaVnF0xOdXbGPl9Kr55rDC5M4y3hr0QMx8wkvbLHQIxs"
    bot = CanvasBot(url, key)

    bot.get_assignements()