from jatek import Jatek

def fo_fuggveny() -> None:
    j: Jatek = Jatek()
    while True:
        j.frissit()
        j.rajzol()

if __name__ == "__main__":
    fo_fuggveny()