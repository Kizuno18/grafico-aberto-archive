import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que mais de 75 milhões de brasileiros ainda não têm rede de esgoto na porta de casa?"),
    ("scene2", "Segundo o Censo do IBGE, enquanto no Sudeste mais de 86% da população tem esgoto adequado, na Região Norte menos de 15% têm esse serviço básico."),
    ("scene3", "E quase 34 milhões de pessoas ainda não têm água encanada regular. Inscreva-se no Gráfico Aberto para entender a realidade do país!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-022/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-022/audio/{sc_id}.wav"
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
