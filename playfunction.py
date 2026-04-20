import time
import pyvisa
from notedictionary import note_dict
from functiondictionary import function_dict
from durationdict import durationDict

rm = pyvisa.ResourceManager()
device = rm.open_resource("YOUR_RESOURCE_ADDRESS")

device.timeout = 1000

def playNote(note, noteDuration, pieceSpeed = 100, function = "sine"):

    frequency = note_dict[note]
    waveform = function_dict[function]

    # Duration calculation
    quarter_note_time = 60 / pieceSpeed
    if isinstance(noteDuration, str):
        duration = quarter_note_time * durationDict.get(noteDuration)
    else: # if number
        duration = quarter_note_time * noteDuration

    command = f"SOUR1:APPL:{waveform} {frequency}, 30 mVPP, 0 V"
    device.write(command)

    device.write("OUTP1 ON")
    time.sleep(duration)
    device.write("OUTP1 OFF")

    # time.sleep(0.05)