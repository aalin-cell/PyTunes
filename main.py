import playfunction as pf

def main():
    pf.playNote('C4', "quarter", 100, "triangle")
    pf.playNote('D4', "quarter", 100, "sine")
    pf.playNote('E4', "quarter", 100, "square")

if __name__ == '__main__':
    print("PyTunes: Welcome to the playing function!")
    main()
