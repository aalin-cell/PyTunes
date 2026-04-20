import playfunction as pf
import time
from piece import playPiece
from anthem import playAnthem

def main():
    # pf.playNote('C4', "quarter", 100, "triangle")
    # pf.playNote('D4', "quarter", 100, "sine")
    # pf.playNote('E4', "quarter", 100, "square")

    # scale_check = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
    scale_check = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'B4', 'A4', 'G4', 'F4', 'E4', 'D4','C4']
    for scale in scale_check:
        pf.playNote(scale, "quarter", 100, "sine")
        # pf.playNote(scale, "quarter", 100, "triangle")
        # pf.playNote(scale, "quarter", 100, "square")


if __name__ == '__main__':
    print("PyTunes: Welcome to the playing function!")

    print("PyTunes: Checking Scale!")
    main()
    time.sleep(1.5)

    print("PyTunes: Playing Piece!")
    playPiece()
    time.sleep(1.5)

    print("PyTunes: Playing Anthem!")
    playAnthem()

    print("PyTunes: End of the play!")

