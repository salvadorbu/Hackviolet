from canvasapi import Canvas

class CanvasBot:
    def __init__(self, url, key) -> None:
        self.canvas = Canvas(url, key)
        self.user = self.canvas.get_current_user()

    def get_user(self):
        return self.user
    
    def get_courses(self):
        courses = self.canvas.get_courses()._get_next_page()
        l = []
        for c in courses:
            try:
                l.append(c.name)
            except:
                pass
        return l

if __name__ == "__main__":
    url = "https://canvas.vt.edu"
    key = "4511~CSBkFbb31upwYZYNHWfENaVnF0xOdXbGPl9Kr55rDC5M4y3hr0QMx8wkvbLHQIxs"
    bot = CanvasBot(url, key)
    l = bot.get_courses()
    for i in l:
        print(i)