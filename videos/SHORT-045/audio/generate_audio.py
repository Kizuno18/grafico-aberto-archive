import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabe para onde realmente vai o dinheiro dos dois trilhões de reais que o Governo Federal gasta por ano?"),
    ("scene2", "Segundo o Tesouro Nacional, a Previdência lidera isolada consumindo mais de novecentos bilhões de reais, seguida pelos servidores públicos com quase quatrocentos bilhões."),
    ("scene3", "Mais de noventa por cento de tudo já é obrigatório por lei. Inscreva-se no Gráfico Aberto para entender as contas do país!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-045/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-045/audio/{sc_id}.wav"
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
