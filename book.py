class Book:
	def __init__(self, id, title, author, fee):
		self.id = id
		self.title = title
		self.author = author
		self.fee = fee

	def __str__(self):
		return "{}: {} written by {} : rent fee {}".format(
			self.id, self.title, self.author, self.fee
		)