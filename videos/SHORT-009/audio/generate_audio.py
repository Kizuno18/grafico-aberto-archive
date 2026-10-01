import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "O brasileiro trabalha duro mais de 40 horas por semana, mas por que o salário médio no país continua tão baixo?"),
    ("scene2", "Segundo dados internacionais do Conference Board e do IPEA, um trabalhador americano gera 87 dólares por hora trabalhada. No Brasil, são apenas 20 dólares."),
    ("scene3", "O problema não é esforço, é a falta de máquinas modernas, estradas ruins e burocracia. Inscreva-se no Gráfico Aberto para mais dados oficiais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-009/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-009/audio/{sc_id}.wav"
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
