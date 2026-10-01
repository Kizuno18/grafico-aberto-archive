import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "O Brasil envelheceu seis anos em apenas doze anos. E quem prova isso são os dados oficiais do Censo do IBGE."),
    ("scene2", "Em 1980, crianças e jovens de zero a 14 anos eram quase 40% da população. Hoje, caíram para menos de 20%."),
    ("scene3", "Já o número de idosos explodiu. Hoje já são 55 idosos para cada 100 crianças no país."),
    ("scene4", "O bônus demográfico brasileiro está acabando. Inscreva-se no Gráfico Aberto para entender a realidade através dos dados.")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-001/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-001/audio/{sc_id}.wav"
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
