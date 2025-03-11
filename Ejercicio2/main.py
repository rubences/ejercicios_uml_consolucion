from gales import Gales
from spencer import Spencer
from middleton import Middleton
from windsor import Windsor

def main():
    carlos = Gales("Carlos")
    diana = Spencer("Diana")
    guillermo = Gales("Guillermo")
    kate = Middleton("Kate")

    print(carlos)
    print(diana)
    print(guillermo)
    print(kate)

if __name__ == "__main__":
    main()