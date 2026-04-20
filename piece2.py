# Für Elise
from playfunction import playNote

fur_elise = [
    ("E5",0.5), ("D#5",0.5), ("E5",0.5), ("D#5",0.5),
    ("E5",0.5), ("B4",0.5), ("D5",0.5), ("C5",0.5),
    ("A4",1),

    ("C4",0.5), ("E4",0.5), ("A4",0.5),
    ("B4",1),

    ("E4",0.5), ("G#4",0.5), ("B4",0.5),
    ("C5",1)
]

speed = 100

for note, duration in fur_elise:
    playNote(note, duration, speed, "sine")