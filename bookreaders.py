class Books():
    def __init__(self, category, title, author, date, status, user):
        self.category = category
        self.title = title
        self.author = author
        self.date = date
        self.status = status
        self.user = user


def user_log(categories):
    for category in categories:
        Books.append(category)
    result = {}
    if category.status == "returned":
        new_status = "in library"
    elif category.status == "not returned":
        new_status = "fine"
    elif category.status == "reading":
        new_status = "book in circulation"
    else:
        new_status = "NA"

    for b in Books:
        result.setdefault(b.title,{
        b.user : set(),
        b.status : new_status
        })
        result[b.title]["user"].add(b.user)
        result[b.title]["status"]= new_status
    return result
                
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
print(user_log(categories))
# print("Authors chimed in:")
# print("-----------------------")
# print(author_hits(()))