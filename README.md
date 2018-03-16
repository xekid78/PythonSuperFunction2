# PythonSuperFunction2
super()関数を使って親クラスのメンバ変数を変える

## 処理
super()メソッドを使って、JewelryBoxクラスから親クラスのコンストラクタの変数を変えて出力。

## コード
```
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
```

## 出力結果  
```
宝箱を開いた。鋼鉄の剣を手に入れた。
宝箱はキラキラと輝いている
宝箱を開いた。魔法の指輪を手に入れた。
```
  
## 開発環境
| 開発ツール |  |
|:-|:-|
| OS | Windows10 |
| 仮想化ソフト | Oracle VM VirtualBox 5.2 |
| 構築ソフト | Vagrant 2.0.2 |
| 仮想化上OS | CentOS 6.9 |
| SSHクライアント | PuTTY 0.6.8 |
| FTPクライアント | Cyberduck 6.3.5 |
| エディタ | Atom 1.24.0 |
| 開発言語 | Python 3.6.4 |
