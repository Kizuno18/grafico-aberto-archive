import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que mais de trinta milhões de brasileiros ainda não têm água encanada da rede pública dentro de casa?"),
    ("scene2", "Segundo o Censo do IBGE, enquanto no Sudeste mais de noventa e um por cento das pessoas têm água da rede, no Norte esse número despenca para cinquenta e oito por cento."),
    ("scene3", "O Norte tem a maior bacia hidrográfica do planeta, mas o menor acesso à água tratada. Inscreva-se no Gráfico Aberto para ver os dados reais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-041/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-041/audio/{sc_id}.wav"
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
