from furnitureitem import FurnitureItem
from automobile import Automobile
from vendor import Vendor

def main() -> None:
    #################################
    #### Furniture demonstration ####
    #################################
    
    # seth = Vendor[int]('Seth')

    # Vendor is not a class. It's a generic class. It's an "incomplete class"
    # that has some missing pieces.

    # However, Vendor[FurnitureItem] is an ACTUAL class.
    john = Vendor[FurnitureItem]('John')
    john.add_to_stock(FurnitureItem('Couch', 100.00))
    # john.add_to_stock(Automobile('Honda', 1998, 'Accord', 2500.00))
    
    print("John's information prior to selling his couch:")
    john.print()
    print()

    john.sell(0)

    print("John's information after selling his couch:")
    john.print()

    print()
    print()

    ##################################
    #### Automobile demonstration ####
    ##################################

    samantha = Vendor[Automobile]('Samantha')
    samantha.add_to_stock(Automobile('Ford', 2001, 'Taurus', 2000.00))

    print("Samantha's information prior to selling her Ford Taurus:")
    samantha.print()
    print()
    
    samantha.sell(0)

    print("Samantha's information after selling her Ford Taurus:")
    samantha.print()

if __name__ == '__main__':
    main()

