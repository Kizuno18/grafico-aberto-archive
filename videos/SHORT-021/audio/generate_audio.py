import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que o brasileiro está casando quase oito anos mais tarde e se divorciando cada vez mais rápido?"),
    ("scene2", "Segundo o IBGE, a idade média ao casar saltou para 31 anos entre mulheres e 33 entre homens. E a duração do casamento caiu de 17 para menos de 14 anos."),
    ("scene3", "Hoje já acontece praticamente um divórcio para cada dois casamentos no país. Inscreva-se no Gráfico Aberto para ver a realidade dos dados!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-021/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-021/audio/{sc_id}.wav"
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
