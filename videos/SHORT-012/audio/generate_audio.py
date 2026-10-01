import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "A desigualdade de renda no Brasil aumentou ou diminuiu nos últimos trinta anos? Os números oficiais surpreendem."),
    ("scene2", "Segundo o IBGE e o IPEA, o Índice de Gini caiu de 0,60 em 1995 para cerca de 0,52 hoje, uma redução de quase 14% na desigualdade."),
    ("scene3", "Apesar da melhora, o país ainda segue entre os mais desiguais do mundo. Inscreva-se no Gráfico Aberto para entender a realidade através dos dados!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-012/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-012/audio/{sc_id}.wav"
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
