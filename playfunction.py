import time
import pyvisa
from notedictionary import note_dict
from functiondictionary import function_dict
from durationdict import durationDict

rm = pyvisa.ResourceManager()
device = rm.open_resource("USB0::0x0957::0x2607::MY59001073::0::INSTR")

device.timeout = 1000
# device.write("OUT1:LOAD 33")
# device.write("OUT2:LOAD 33")

def playNote(note, noteDuration, pieceSpeed = 100, function = "sine"):

    frequency = note_dict[note]
    waveform = function_dict[function]

    # Duration calculation
    quarter_note_time = 60 / pieceSpeed
    if isinstance(noteDuration, str):
        duration = quarter_note_time * durationDict.get(noteDuration)
    else: # if number
        duration = quarter_note_time * noteDuration

    command1 = f"SOUR1:APPL:{waveform} {frequency}, 30 mVPP, 0 V"
    command2 = f"SOUR2:APPL:{waveform} {frequency}, 30 mVPP, 0 V"

    device.write(command1)
    device.write(command2)

    device.write("OUTP1 ON")
    device.write("OUTP2 ON")

    time.sleep(duration)

    device.write("OUTP1 OFF")
    device.write("OUTP2 OFF")

    # time.sleep(0.05)