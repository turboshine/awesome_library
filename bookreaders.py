from datetime import datetime, date

def compute_status(old_date,current_date, book_status):
    
    days = (current_date - old_date).days

    
    if book_status in ["returned","completed"]:
        new_status = "in library"
    elif book_status == "reading" and days <= 60:
        new_status = "book in circulation"
    elif days > 60:
        new_status = "overdue"
    else:
        new_status = "NA"
    return new_status

def author_user_count(book_bundle):
    author_count = {}
    for book in book_bundle:
        author_count.setdefault(book.author, set()).add(book.user)
    return author_count
def author_hit_count(book_bundle):
    author_readers = author_user_count(book_bundle)
    author_hits = {author: len(users) for author, users in author_readers.items()}
    return author_hits

def user_log(book_bundle):
    Books("ARC", "Gamerville","abc","2024-06-01","reading","Alice")
    Books("ARC","Gamerville","abc","2024-07-01","completed","Alice"),
    result = {}
    for book in book_bundle:

        book_date = datetime.strptime(book.date, "%Y-%m-%d").date()
        current_date =date.today()

        new_status = compute_status(
            old_date = book_date,
            current_date = current_date,
            book_status = book.status
        )
    # make a dictionary with title as key and user and status as values

        title_info = result.setdefault(book.title, {'users':set(),'status':new_status,'date':book_date})
        title_info['users'].add(book.user)
         # keep the LATEST date for the title
        if book_date > title_info['date']:
            print(f"{book_date}modifiying date ********{title_info['date']}")
            title_info['status'] = new_status
            title_info['date'] = book_date 
       


    lines = ""
    for title , info in result.items():
        user_list = ",".join(info['users']) 
        status = info['status'] if info['status'] is not None else "NA"
        lines += f"{title:20} {user_list:20} {status:20} {str(info['date']):20}\n"
    print(f"Title                  Users                      Status                    Date")
    print("--------------------------------------------------------------------------------")
    return lines
    
class Books():
    def __init__(self, category, title, author, date, status, user):
        self.category = category
        self.title = title
        self.author = author
        self.date = date
        self.status = status
        self.user = user

    
        
book_list = [
    Books("ARC", "Gamerville","abc","2024-06-01","reading","Alice"),
    Books("ARC","Gamerville","abc","2024-07-01","completed","Alice"),
    Books("ARC","Gamerville","abc","2024-07-13","reading","Sagun"),
    Books("ARC","Gamerville","abc","2024-07-27","completed","Sagun"),
    Books("ARC","Harry Potter","J.K. Rowling","2024-08-01","reading","Eve"),
    Books("ARC","Harry Potter","J.K. Rowling","2024-09-05","completed","Eve"),
    Books("ARC","Lord of rings","J.K. Rowling","2024-09-10","reading","Bob"),
    Books("ARC","Lord of rings","J.K. Rowling","2025-09-10","completed","Bob"),
    Books("ARC","The lost year","xyz","2024-10-15","not returned","Bob"),
    Books("HomeLibrary","Mahabharatha","yashpalDas","2024-06-20","reading","Charlie"),
    Books("HomeLibrary","Dogman","davPilkey","2024-05-30","reading","David"),
    Books("HomeLibrary","Mahabharatha","yashpalDas","2024-08-25","completed","Charlie"),
]
# output: Gamerville : Alice,Sagun in the library 2024-07-27
#Dogman : David overdue 2024-05-30
print(user_log(book_list))

hits = author_hit_count(book_list)
for author, count in hits.items():
    print(f"Author: {author}, Users: {count}")


