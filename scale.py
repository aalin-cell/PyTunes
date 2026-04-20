from playfunction import playNote

# Notes for scale
scale = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]

speed = 100  # BPM

# Up
for note in scale:
    playNote(note, 1, speed, "sine")

# Down
for note in reversed(scale):
    playNote(note, 1, speed, "sine")