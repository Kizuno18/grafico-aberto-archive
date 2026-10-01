import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você lembra quando o desemprego no Brasil bateu quase 15% na pandemia? Veja o que aconteceu com a taxa de lá pra cá."),
    ("scene2", "Segundo a PNAD Contínua do IBGE, a desocupação despencou para 6,8% em 2024, o menor nível em uma década, superando 100 milhões de trabalhadores ocupados."),
    ("scene3", "O emprego cresceu, mas o desafio ainda é a qualidade das vagas e a renda. Inscreva-se no Gráfico Aberto para ver os dados reais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-025/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-025/audio/{sc_id}.wav"
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
