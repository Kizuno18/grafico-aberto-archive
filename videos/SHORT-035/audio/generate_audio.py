import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que o número de assassinatos no Brasil caiu mais de trinta por cento nos últimos anos?"),
    ("scene2", "Segundo o Atlas da Violência, o país bateu um pico trágico de sessenta e cinco mil mortes em 2017. De lá pra cá, a taxa recuou de trinta e um para vinte e um por cem mil habitantes."),
    ("scene3", "Porém, enquanto São Paulo tem taxa abaixo de sete, estados do Norte e Nordeste ainda passam de trinta e cinco. Inscreva-se no Gráfico Aberto para ver os dados reais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-035/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-035/audio/{sc_id}.wav"
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
