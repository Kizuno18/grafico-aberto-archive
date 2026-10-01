import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que o Brasil deu um salto de trinta vezes na energia eólica em pouco mais de dez anos?"),
    ("scene2", "Mais de oitenta e cinco por cento de todos os parques eólicos do país estão no Nordeste, liderados pelo Rio Grande do Norte e pela Bahia."),
    ("scene3", "Graças aos ventos constantes, nossas turbinas produzem quase o dobro da média mundial. Inscreva-se no Gráfico Aberto!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-051/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-051/audio/{sc_id}.wav"
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
