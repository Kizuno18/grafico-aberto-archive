import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que quase 85% dos brasileiros ainda moram em casas? Mas os apartamentos estão avançando rápido!"),
    ("scene2", "Segundo o Censo do IBGE, a proporção de moradores de apartamentos saltou de 8% para mais de 12%, somando mais de 25 milhões de pessoas."),
    ("scene3", "A cidade mais vertical do país é Santos, onde mais de 63% da população vive em prédios. Inscreva-se no Gráfico Aberto para ver a realidade dos dados!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-008/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-008/audio/{sc_id}.wav"
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
