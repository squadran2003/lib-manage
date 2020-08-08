from book import Book

external_books = [
	{'id':0,'name':'Girl, Woman, Other', 'author': 'Bernardine Evaristo','fee':5},
	{'id':1,'name':'Skincare The Ultimate No-Nonsense Guide', 'author': 'Caroline Hirons','fee':10},
	{'id':2,'name':"Why I'm No Longer Talking to White People About Race", 'author': 'Reni Eddo-Lodge','fee':20},
	{'id':3,'name':'The Boy, The Mole, The Fox and The Horse', 'author': 'Charlie Mackesy','fee':35},
	{'id':4,'name':'No Mercy', 'author': 'Martina Cole','fee':12},
	{'id':5,'name':'Where the Crawdads Sing', 'author': 'Delia Owens','fee':34},
	{'id':6,'name':'The Secret of Cold Hill', 'author': 'Peter James','fee':12},
	{'id':7,'name':'John Grisham', 'author': 'Paperback','fee':14},
	{'id':8,'name':'Natives Race and Class in the Ruins of Empire', 'author': 'Akala','fee':17},
	{'id':9,'name':'Queenie', 'author': 'Candice Carty-Williams','fee':20},



]


class Library:
	books = []
	members_list = []
	# rentals will be a list of dictionaries
	rentals = []

	def __init__(self):
		self.create_books()

	def create_books(self):
		for i in range(len(external_books)):
			id = external_books[i]['id']
			name = external_books[i]['name']
			author = external_books[i]['author']
			fee = external_books[i]['fee']
			self.books.append(Book(id = id, title=name, author=author, fee=fee))

	def add_new_member(self, member):
		self.members_list .append(member)

	def get_book(self, id):
		for book in self.books:
			if id==book.id:
				return book
		print("sorry cannot find that book!")

	def get_member(self, id):
		for member in self.members_list:
			if id==member.id:
				return member
		print("No member with that id found!")

	def members(self):
		print("*******************")
		print("Library members list!")
		for i in range(len(self.members_list)):
			print(self.members_list[i])

	def show_books(self):
		print("*******************")
		print("List of avaliable books to rent!")
		for i in range(len(self.books)):
			print(self.books[i])

	def remove_book(self, book):
		index  = -1
		for i in range(len(self.books)):
			if book.id == self.books[i].id:
				index = i
		self.books.pop(index)

	def rent_book(self, book, member):
		self.rentals.append({
				book:member
			})
		self.remove_book(book)

	def return_book(self, book_id, member):
		book = None
		index = -1
		for i in range(len(self.rentals)):
			for key, val in self.rentals[i].items():
				if book_id == key.id:
					index = i
					book = key
		self.rentals.pop(index)
		self.books.append(book)


	def list_rentals(self):
		print("*******************")
		print("Books rented out")
		for i in range(len(self.rentals)):
			print("{} rented by {}".format(
				list(self.rentals[i].keys())[0].title, list(self.rentals[i].values())[0].name
			))

	def add_book(self, book):
		self.books.append(book)