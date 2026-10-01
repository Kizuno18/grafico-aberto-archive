import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que mais de mil e trezentas cidades brasileiras já têm oficialmente mais idosos do que crianças?"),
    ("scene2", "Segundo o Censo do IBGE, a cidade de Coqueiro Baixo, no Rio Grande do Sul, lidera o país com quase três idosos para cada criança."),
    ("scene3", "Entre as capitais, Porto Alegre e Rio de Janeiro são as mais velhas. Inscreva-se no Gráfico Aberto para acompanhar os dados reais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-026/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-026/audio/{sc_id}.wav"
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
