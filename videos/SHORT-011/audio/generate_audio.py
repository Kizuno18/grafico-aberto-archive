import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que a taxa de juros básica do Brasil já chegou a impressionantes 45% ao ano?"),
    ("scene2", "Segundo o Banco Central, a Selic bateu 45% em 1999, despencou para a mínima histórica de 2% em 2020, e hoje voltou para os dois dígitos."),
    ("scene3", "Mesmo oscilando tanto, o Brasil continua pagando um dos juros reais mais altos do planeta. Inscreva-se no Gráfico Aberto para entender os dados!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-011/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-011/audio/{sc_id}.wav"
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
