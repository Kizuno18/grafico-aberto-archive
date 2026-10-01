import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você já percebeu como os telhados do Brasil se encheram de painéis solares nos últimos anos?"),
    ("scene2", "Segundo a Absolar, a energia solar saltou de menos de um gigawatt em 2017 para mais de quarenta e cinco gigawatts em 2024, virando a segunda maior fonte do país."),
    ("scene3", "E mais de dois terços dessa energia vêm de casas e comércios. Inscreva-se no Gráfico Aberto para ver os dados reais da nossa infraestrutura!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-036/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-036/audio/{sc_id}.wav"
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
