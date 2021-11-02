class Obj:
  def __init__(self, color, size):
    self.color = color
    self.size = size


obj = Obj("red", "m")

if not ("red" == obj.color or "xl" == obj.size):
	print("OK")
else:
	print("KO")

if not "red" == obj.color and not "xl" == obj.size:
	print("OK")
else:
	print("KO")
