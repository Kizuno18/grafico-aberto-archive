import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "No mundo, a queima de petróleo e carvão gera quase toda a poluição. Mas você sabe qual é o verdadeiro vilão no Brasil?"),
    ("scene2", "Segundo o relatório oficial do SEEG, o desmatamento lidera isolado com 48% das emissões do país, seguido pela agropecuária com 27%."),
    ("scene3", "Já a energia e os transportes geram menos de 20%, graças à nossa matriz renovável. Inscreva-se no Gráfico Aberto para ver os dados reais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-029/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-029/audio/{sc_id}.wav"
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
