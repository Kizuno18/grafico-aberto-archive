import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que uma pessoa que ganha salário mínimo paga proporcionalmente muito mais imposto do que um milionário no Brasil?"),
    ("scene2", "Segundo dados da Receita Federal, quase metade de todos os impostos do país estão embutidos nos preços do que a gente compra no supermercado e na farmácia."),
    ("scene3", "Quem ganha menos gasta quase tudo para sobreviver e entrega mais de 26% da renda em tributos. Inscreva-se no Gráfico Aberto!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-006/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-006/audio/{sc_id}.wav"
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
