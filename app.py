
from member import Member
from membership import Membership
from library import Library


def help_text():
	print("""
	*******************************************
		Welcome to library management system

	1: create a new member
		a)1: cost $5
		b)2: cost $10
		c)3: cost $20
	2: list available books
	3: members list
	4: rent a book
	5: return a book
	6: help text
	7: quit the app
	*********************************************
	""")


if __name__ == '__main__':
	library = Library()
	help_text()
	while True:
		user_input = input("Choose an option between 1 and 7? ")
		if user_input not in "1234567":
			print("invalid input !! enter a option between 1 and 7?  ")
		if user_input=='6':
			help_text()
		elif user_input=='7':
			print("goodbye!")
			break
		elif user_input=='1':
			typ = input("Enter membership type between 1, 2 or 3? ")
			start_date = input("enter start date? ")
			mem_type = Membership(typ, start_date)
			name = input("Full name ? ")
			age = input("age? ")
			address = input("address? ")
			member = Member(2, name, age, address, mem_type)
			library.add_new_member(member)
		elif user_input=='2':
			library.show_books()
		elif user_input=='3':
			library.members()
		elif user_input=='4':
			book_id = int(input("choose a book from the list by passing its id? "))
			member = library.get_member(2)
			book = library.get_book(book_id)
			library.rent_book(book, member)
			library.list_rentals()
		elif user_input=='5':
			book_id = int(input("Enter book id found on the back of the book? "))
			member_id = int(input("Enter membership number? "))
			member = library.get_member(member_id)
			library.return_book(book_id, member)
		else:
			pass

