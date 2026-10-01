import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que na década de 1940 a expectativa de vida média do brasileiro era de apenas 45 anos?"),
    ("scene2", "Segundo dados oficiais do IBGE, a expectativa de vida saltou de 45 anos para mais de 76 anos hoje, um ganho impressionante de mais de três décadas de vida!"),
    ("scene3", "A vacinação em massa, o saneamento e o SUS transformaram o país. Inscreva-se no Gráfico Aberto para entender a realidade através dos dados!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-014/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-014/audio/{sc_id}.wav"
    audio_bytes = bytearray()
    for chunk in voice.synthesize(text):
        audio_bytes.extend(chunk.audio_int16_bytes)
        
    with wave.open(out_wav, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_bytes)
        
    dur = len(audio_bytes) / (2 * sample_rate)
    print(f"{sc_id}: dur={dur:.2f}s")
