✅ Task 1: Frequency Table (C3 to C5)

| Note | Frequency (Hz) |
| ---- | -------------- |
| C3   | 130.81         |
| D3   | 146.83         |
| E3   | 164.81         |
| F3   | 174.61         |
| G3   | 196.00         |
| A3   | 220.00         |
| B3   | 246.94         |
| C4   | 261.63         |
| D4   | 293.66         |
| E4   | 329.63         |
| F4   | 349.23         |
| G4   | 392.00         |
| A4   | 440.00         |
| B4   | 493.88         |
| C5   | 523.25         |

✅ Task 2: Why Output Load = 33Ω?

Answer:

The waveform generator is designed to work with a matched load impedance.
Setting 33Ω ensures correct voltage output.
If not matched:
Voltage amplitude will be incorrect
Signal reflections may occur
Measurement errors increase

👉 In short:
It ensures accurate signal amplitude and proper power transfer.

✅ Task 3: Python Script to Identify Device
import pyvisa

rm = pyvisa.ResourceManager()
device = rm.open_resource("YOUR_RESOURCE_ADDRESS")

device.write("*IDN?")
print(device.read())

👉 Replace "YOUR_RESOURCE_ADDRESS" using Keysight Connection Expert.


✅ Task 5: Waveform Differences

| Waveform | Sound              | Reason                  |
| -------- | ------------------ | ----------------------- |
| Sine     | Pure tone          | Only one frequency      |
| Square   | Harsh/buzzy        | Contains odd harmonics  |
| Triangle | Softer than square | Fewer harmonics         |
| Ramp     | Sharp/bright       | Strong harmonic content |

👉 Why difference?
Because each waveform has different harmonic content (Fourier components).