import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabe quantas horas de trabalho quem ganha salário mínimo precisa dedicar no mês só para pagar a comida básica?"),
    ("scene2", "Segundo o DIEESE, em São Paulo a cesta básica passa de oitocentos reais, consumindo quase sessenta por cento do salário mínimo líquido e mais de cento e dez horas de jornada."),
    ("scene3", "Para sustentar uma família de quatro pessoas, o DIEESE calcula que o mínimo ideal deveria ser de quase sete mil reais. Inscreva-se no Gráfico Aberto para ver os dados reais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-034/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-034/audio/{sc_id}.wav"
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
