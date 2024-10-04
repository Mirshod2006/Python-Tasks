class Card():
    def __init__(self,card_number,card_type):
        self.__number=card_number
        self.__type=card_type
    
    def info(self):
        if self.__number.isdigit():
            _info=f"Card Number:{self.__number}\nCard Type:{self.__type}"
        else:
            _info=f"Card Level:{self.__number}\nCard Type:{self.__type}"
        return _info
    def get_name(self):
        return self.__number

    def get_type(self):
        return self.__type

    def setter_type(self,type):
        self.__type=type

    def setter_number(self,number):
        self.__number=number

diamond = Card("10","diamond")
print(diamond.info())