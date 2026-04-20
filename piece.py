from playfunction import playNote

# melody = [
#     ("E4",1), ("D4",1), ("C4",1), ("D4",1),
#     ("E4",1), ("E4",1), ("E4",2),
#     ("D4",1), ("D4",1), ("D4",2)
# ]
#
# speed = 100


# Für Elise
melody = [
    ("E5",0.5), ("D#5",0.5), ("E5",0.5), ("D#5",0.5),
    ("E5",0.5), ("B4",0.5), ("D5",0.5), ("C5",0.5),
    ("A4",1),

    ("C4",0.5), ("E4",0.5), ("A4",0.5),
    ("B4",1),

    ("E4",0.5), ("G#4",0.5), ("B4",0.5),
    ("C5",1)
]
speed = 100

def playPiece():
    for note, duration in melody:
        playNote(note, duration, speed, "sine")