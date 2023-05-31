

## EXAMPLE-1

class IPL:
    semis='eee sala cum nambde'
    _finals='one more step away to trophy'
    __trophy='finally we made it'

    def heart(self):
        print('RCB has won the hearts but not the trophy')

    def _display(self):
        print('Protected display')

    def __happiness(self):
        print('No more heart winning only trophy')

rcb=IPL()
print(rcb.semis)
rcb.heart()
print(rcb._finals)
rcb._display()
print(rcb._IPL__trophy)
rcb._IPL__happiness()



## EXAMPLE-2


class Bag:
    pen="ElkosPen"
    _book="Pythonbook"
    __note="Djangonote"

    def writing(self):
        print("I am writing")

    def _reading(self):
        print(f"I am reading {self._book}")

    def __read(self):
        print(f"I am reading {self.__note}")

b=Bag()
#print(b.pen)
#print(b._book)
print(b._Bag__note)