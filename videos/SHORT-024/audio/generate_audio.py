import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "O Brasil bateu recorde de 340 bilhões de dólares em exportações. Mas você sabe quais são os três produtos que dominam tudo?"),
    ("scene2", "Segundo o Ministério da Indústria e Comércio, a soja lidera com 53 bilhões de dólares, seguida pelo petróleo com 42 bilhões e o minério de ferro com 31 bilhões."),
    ("scene3", "E o maior cliente do país é a China, que compra sozinha quase um terço de tudo. Inscreva-se no Gráfico Aberto para ver os dados reais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-024/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-024/audio/{sc_id}.wav"
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
