import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que a menor cidade do Brasil tem menos moradores do que um único prédio residencial em São Paulo?"),
    ("scene2", "Segundo o Censo do IBGE, Serra da Saudade em Minas Gerais tem apenas 833 habitantes. E só existem três cidades em todo o país com menos de mil pessoas."),
    ("scene3", "Enquanto isso, a capital de São Paulo tem mais de 11 milhões de moradores. Inscreva-se no Gráfico Aberto para mais curiosidades com dados oficiais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-019/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-019/audio/{sc_id}.wav"
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
