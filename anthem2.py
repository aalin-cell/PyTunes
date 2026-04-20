# Indian National Anthem (Jana Gana Mana)
from playfunction import playNote

anthem = [
    ("G4",1), ("A4",1), ("B4",2),
    ("A4",1), ("G4",1), ("E4",2),
    ("G4",1), ("A4",1), ("B4",2),
    ("A4",1), ("G4",1), ("E4",2)
]

speed = 90

for note, duration in anthem:
    playNote(note, duration, speed, "sine")