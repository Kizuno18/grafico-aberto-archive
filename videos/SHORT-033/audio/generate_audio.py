import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você já percebeu a quantidade de carros elétricos e híbridos rodando nas ruas nos últimos meses?"),
    ("scene2", "Segundo a Associação Brasileira do Veículo Elétrico, as vendas saltaram de vinte mil em 2020 para mais de cento e cinquenta mil em 2024, multiplicando por quase oito vezes."),
    ("scene3", "A frota no país já passa de trezentos mil veículos. Inscreva-se no Gráfico Aberto para acompanhar as transformações da economia!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-033/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-033/audio/{sc_id}.wav"
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
