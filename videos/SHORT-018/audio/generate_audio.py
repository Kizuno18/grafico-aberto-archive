import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que o Banco Central do Brasil tem guardado mais de 350 bilhões de dólares em reservas?"),
    ("scene2", "Nas décadas de 80 e 90, o país não tinha nem 20 bilhões e vivia pedindo socorro ao FMI. Hoje, temos um dos maiores colchões cambiais do mundo em ouro e títulos."),
    ("scene3", "Esse dinheiro funciona como um escudo contra crises mundiais e ataques ao Real. Inscreva-se no Gráfico Aberto para entender a economia!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-018/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-018/audio/{sc_id}.wav"
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
