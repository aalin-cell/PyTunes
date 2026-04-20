from playfunction import playNote

anthem = [
    ("C4",1), ("D4",1), ("E4",2),
    ("C4",1), ("D4",1), ("E4",2),
    ("G4",2), ("E4",2)
]

speed = 100

for note, duration in anthem:
    playNote(note, duration, speed, "sine")