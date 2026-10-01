import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "A dívida pública do Brasil já passa de 8 trilhões e meio de reais. Mas para quem exatamente o governo deve esse dinheiro?"),
    ("scene2", "Segundo o Tesouro Nacional, mais de 90% da dívida é interna. E os maiores donos desses títulos são fundos de investimento, bancos e previdências do próprio país."),
    ("scene3", "Na prática, o governo deve para a poupança e aposentadoria dos próprios brasileiros. Inscreva-se no Gráfico Aberto para entender a economia!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-016/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-016/audio/{sc_id}.wav"
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
