import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que grandes capitais brasileiras estão encolhendo pela primeira vez na história?"),
    ("scene2", "Segundo o Censo do IBGE, Salvador perdeu quase 10% da sua população, e cidades como Porto Alegre e Rio de Janeiro também perderam dezenas de milhares de moradores."),
    ("scene3", "Enquanto isso, o Centro-Oeste foi a região que mais cresceu no país, atraindo população para cidades médias do interior. Inscreva-se no Gráfico Aberto para mais dados oficiais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-005/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-005/audio/{sc_id}.wav"
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
