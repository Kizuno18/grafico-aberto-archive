import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Por que um país gigante como o Brasil tem praticamente a mesma extensão de trilhos que tinha nos anos 50?"),
    ("scene2", "Segundo a ANTT, o Brasil tem só 30 mil quilômetros de ferrovias, contra 250 mil nos Estados Unidos. E mais de 75% de tudo o que viaja nos trilhos é apenas minério de ferro."),
    ("scene3", "Sem trens, mais de 65% das cargas dependem de caminhões e asfalto. Inscreva-se no Gráfico Aberto para mais dados da nossa infraestrutura!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-020/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-020/audio/{sc_id}.wav"
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
