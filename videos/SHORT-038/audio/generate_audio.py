import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você lembra como a gente comprava antes de 2020? Veja como a internet engoliu o comércio no Brasil."),
    ("scene2", "Segundo dados da ABComm e Ebit Nielsen, o faturamento online saltou de setenta e cinco bilhões em 2019 para mais de duzentos bilhões em 2024."),
    ("scene3", "São quase noventa milhões de brasileiros comprando online. Inscreva-se no Gráfico Aberto para ver os dados reais da economia!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-038/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-038/audio/{sc_id}.wav"
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
