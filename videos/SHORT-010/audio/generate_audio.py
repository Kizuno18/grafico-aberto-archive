import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que em centenas de cidades brasileiras já existem mais motos registradas do que carros de passeio?"),
    ("scene2", "Segundo dados oficiais da Senatran, o país tem mais de 33 milhões de motos. E em estados como Maranhão e Piauí, mais de metade de todos os veículos já são de duas rodas."),
    ("scene3", "A moto virou o verdadeiro transporte público e ferramenta de trabalho do interior do país. Inscreva-se no Gráfico Aberto para ver mais dados!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-010/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-010/audio/{sc_id}.wav"
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
