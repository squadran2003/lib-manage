class Membership:
	types = {
		"1":"5", "2":"10", "3":"20"
	}
	currency = '$'
	fee = ""

	def __init__(self, type, open_date, closing_date=None):
		self.type = type
		self.open_date = open_date
		self.closing_date = closing_date

	def get_fee(self):
		if self.type not in ["1","2","3"]:
			raise ValueError("Invliad Membership ship, acceptable values are 1, 2 or 15")
		self.fee = self.currency+self.types.get(str(self.type),"5")


	def __str__(self):
		return self.fee