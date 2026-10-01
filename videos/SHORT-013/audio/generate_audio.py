import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que quase 20% de todas as casas do Brasil hoje têm apenas uma única pessoa morando?"),
    ("scene2", "Segundo o Censo do IBGE, o número de lares com só um morador quase dobrou em 12 anos, saltando para quase 14 milhões de pessoas."),
    ("scene3", "Pela primeira vez na história, a média por casa caiu para menos de 3 pessoas. Inscreva-se no Gráfico Aberto para entender a realidade do país!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-013/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-013/audio/{sc_id}.wav"
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
