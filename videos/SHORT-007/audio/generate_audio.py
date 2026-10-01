import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Se o salário mínimo tivesse apenas acompanhado a inflação do Real, ele seria de menos de 600 reais hoje!"),
    ("scene2", "Em 1994, o mínimo era de 64 reais. Com a inflação acumulada de quase 800%, ele valeria 577 reais. Mas como hoje o piso passa de 1.600 reais, o trabalhador teve quase 180% de ganho real."),
    ("scene3", "O poder de compra do salário mínimo quase triplicou em 30 anos. Para mais fatos baseados em dados oficiais, inscreva-se no Gráfico Aberto!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-007/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-007/audio/{sc_id}.wav"
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
