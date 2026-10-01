import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você já parou pra pensar por que quase tudo o que você consome no Brasil chega de caminhão?"),
    ("scene2", "Segundo a Confederação Nacional do Transporte, cerca de 65% da carga brasileira roda por rodovias, contra apenas 15% em ferrovias e 11% em hidrovias."),
    ("scene3", "Em longas distâncias, o asfalto consome até quatro vezes mais combustível por tonelada. Inscreva-se no Gráfico Aberto para ver os dados reais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-027/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-027/audio/{sc_id}.wav"
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
