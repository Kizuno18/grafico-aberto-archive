import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Em 1960, a mulher brasileira tinha em média mais de seis filhos. Hoje, tem menos de um vírgula seis."),
    ("scene2", "Os dados do Censo do IBGE mostram uma queda contínua de 75% na fecundidade, ficando bem abaixo da taxa de reposição populacional."),
    ("scene3", "O número de nascimentos por ano no Brasil é o menor em mais de 40 anos. Inscreva-se no Gráfico Aberto para entender a realidade através dos dados!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-004/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-004/audio/{sc_id}.wav"
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
