import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que o Brasil tem quase dez milhões de estudantes universitários, quase quatro vezes mais do que no ano 2000?"),
    ("scene2", "Segundo o Inep, as faculdades privadas concentram quase 80% das vagas. E mais de 65% de todos os novos calouros do país entram estudando à distância."),
    ("scene3", "A proporção de adultos com diploma triplicou, passando de 7% para mais de 20%. Inscreva-se no Gráfico Aberto para mais dados da nossa sociedade!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-023/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-023/audio/{sc_id}.wav"
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
