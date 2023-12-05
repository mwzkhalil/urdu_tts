# urdu_tts
This Python library provides a simple interface for Urdu Text-to-Speech (TTS) using the Facebook MMS TTS Urdu Script model.

## Installation

You can install the library using pip:

```bash
pip install git+https://github.com/mwzkhalil/urdu-tts.git
```

### Usage
```bash
from urdu_tts.tts import UrduTTS
from IPython.display import Audio

# Initialize the UrduTTS class
urdu_tts = UrduTTS()

# Generate audio for Urdu text
text = "مجھے پاکستان کے شہر کراچی کے بارے میں بتائیں"
audio_waveform = urdu_tts.generate_audio(text)

# Display the audio
Audio(audio_waveform, rate=16000)
```
