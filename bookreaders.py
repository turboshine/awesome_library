class Books():
    def __init__(self, category, title, author, date, status, user):
        self.category = category
        self.title = title
        self.author = author
        self.date = date
        self.status = status
        self.user = user

categories = [
    Books("ARC", "Gamerville","abc","2024-06-01","Reading","Alice"),
    Books("ARC","Gamerville","abc","2024-07-01","completed","Alice"),
    Books("ARC","Gamerville","abc","2024-07-13","reading","Sagun"),
    Books("ARC","Gamerville","abc","2024-07-27","completed","Sagun"),
    Books("ARC","The lost year","xyz","2024-10-15","not returned","Bob"),
    Books("HomeLibrary","Mahabharatha","yashpalDas","2024-06-20","Reading","Charlie"),
    Books("HomeLibrary","Dogman","davPilkey","2024-05-30","reading","David"),
    Books("HomeLibrary","Mahabharatha","yashpalDas","2024-08-25","completed","Charlie"),
]
print("Book in circulation:")
print("-----------------------")
print(user_log())
print("Authors chimed in:")
print("-----------------------")
print(author_hits(()))
