import sys, wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

for scene in ["scene1", "scene2", "scene3", "scene4"]:
    with open(f"videos/PILOTO-001/audio/{scene}.txt", "r", encoding="utf-8") as f:
        text = f.read().strip()
    
    out_wav = f"videos/PILOTO-001/audio/{scene}.wav"
    audio_bytes = bytearray()
    sample_rate = voice.config.sample_rate
    
    for chunk in voice.synthesize(text):
        audio_bytes.extend(chunk.audio_int16_bytes)
        
    with wave.open(out_wav, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2) # 16-bit PCM
        wf.setframerate(sample_rate)
        wf.writeframes(audio_bytes)
        
    dur = len(audio_bytes) / (2 * sample_rate)
    print(f"{scene}: rate={sample_rate}, dur={dur:.2f}s, bytes={len(audio_bytes)}")
