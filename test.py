
def user_log(categories):
    result = {}
   # title = categories.title
    # user = categories.user
    # status = categories.status
    for category in categories:
        if category.status == "returned":
            new_status = "in library"
        elif category.status == "not returned":
            new_status = "fine"
        elif category.status == "reading":
            new_status = "book in circulation"
        else:
            new_status = "NA"
    # make a dictionary with title as key and user and status as values

        book_list = result.setdefault(category.title, {'user':set(),'status':new_status})
        book_list['user'].add(category.user)
        book_list['status'] = new_status
        #result[category.title] = {category.user, category.status}
      #print(category.title, category.user)  
    #to build the output dictionary
    lines = ""
    for title , info in result.items():
        user_list = ",".join(info['user']) 
        lines += f"{title}          {user_list}                {info['status']}\n"
    print(f"Title                  Users                      Status")
    print("---------------------------------------------------------")
    return lines
    
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

print(user_log(categories))


