import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que mais de 60% dos brasileiros que navegam na internet usam exclusivamente o telefone celular?"),
    ("scene2", "Segundo a PNAD do IBGE, a internet já chega a mais de 92% das casas. Mas enquanto 99% usam o celular, o computador caiu para apenas 35%."),
    ("scene3", "O celular virou o único banco, escola e trabalho de milhões de famílias. Inscreva-se no Gráfico Aberto para mais dados oficiais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-015/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-015/audio/{sc_id}.wav"
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
