# Travis and Ron

class CellPhone:
    def __init__(self, manufacturer='none', model_number='none', retail_price=0):
        self.manufacturer = manufacturer
        self.model_number = model_number
        self.retail_price = retail_price

    def set_manufact(self):
        self.manufacturer = input('Enter the manufacturer:')
        #return self.manufacturer

    def set_model(self):
        self.model_number = input('Enter the model number:')
        return self.model_number

    def set_retail_price(self):
        self.retail_price = float(input('Enter the retail price:'))
        return self.set_retail_price

    def get_manufact(self):
        print('Manufacturer: {}' .format(self.manufacturer))

    def get_model(self):
        print('Model Number: {}' .format(self.model_number))

    def get_retail_price(self):
        print('Retail Price: ${:.2f}' .format(self.retail_price))

def main():
    user_input = CellPhone()
    user_input.set_manufact()
    user_input.set_model()
    user_input.set_retail_price()
    print('Here is the data that you entered:')
    user_input.get_manufact()
    user_input.get_model()
    user_input.get_retail_price()


if __name__ == "__main__":
    main()
