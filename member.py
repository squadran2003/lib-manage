class Member:

	books_rented = []

	def __init__(self, id, name, age, address, membership):
		self.name = name
		self.age = age
		self.address = address
		self.membership = membership
		self.id = id

	def checkout(self, book):
		self.books_rented.append(book)
		print("successfully checkout of {}".format(book))

	def checkin(self, book):
		book_index = -1
		for i in range(len(self.books_rented)):
			book.id = self.books_rented[i].id
			book_index = i
		self.books_rented.pop(i)
		print("{} checked in successfully")


	def __str__(self):
		return "{} {} years old living at {}".format(
			self.name, self.age, self.address
		)