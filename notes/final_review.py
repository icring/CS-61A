class Coffee:
	warmth = 2
	def __init__(self, warmth):
		self.warmth = warmth
	def holiday(self, cheer):
		def buzz(self, sugar):
			yield sugar(self, cheer) + self.warmth
			cal = self.buzz
			while True:
				yield sugar(self, next(cal)) + self.warmth
		return buzz

class Latte(Coffee):
	@property
	def buzz(self):
		return iter([self.warmth for _ in range(Latte.warmth)])

	def stir(self, drink):
		self.warmth += 1
		return drink * drink

frap, mocha = Coffee(2), Latte(1)
Latte.holiday, Coffee.buzz = frap.holiday(5), frap.holiday(5)
chai = mocha.holiday(lambda self, x: x + 1)
vanilla = frap.buzz(Latte.stir)