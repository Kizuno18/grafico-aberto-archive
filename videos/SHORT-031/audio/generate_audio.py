import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você lembra quando tinha que pagar taxa de quinze reais para fazer uma TED ou esperar o dinheiro cair no dia seguinte?"),
    ("scene2", "Lançado pelo Banco Central em 2020, o Pix já ultrapassou quarenta e dois bilhões de transações em um único ano, superando de longe boleto, TED e cartão de débito."),
    ("scene3", "Hoje já são mais de cento e sessenta milhões de brasileiros cadastrados. Inscreva-se no Gráfico Aberto para ver os dados reais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-031/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-031/audio/{sc_id}.wav"
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
