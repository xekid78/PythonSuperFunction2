class Box(object):
    def __init__(self, item):
        self.myItem = item

    def open(self):
        print("宝箱を開いた。" + self.myItem + "を手に入れた。")

class JewelryBox(Box):
    def __init__(self, item):
        super(JewelryBox, self).__init__(item)

    def look(self):
        print("宝箱はキラキラと輝いている")

box = Box("鋼鉄の剣")
box.open()

jewelryBox = JewelryBox("魔法の指輪")
jewelryBox.look()
jewelryBox.open()
