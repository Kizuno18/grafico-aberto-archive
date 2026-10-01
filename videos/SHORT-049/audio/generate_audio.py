import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você já comparou quanto imposto o Brasil cobra em relação ao resto da América Latina e aos países ricos?"),
    ("scene2", "Segundo a Receita Federal e a OCDE, o Brasil arrecada trinta e três por cento do PIB, muito acima da média latina de vinte e um por cento e superando até os Estados Unidos."),
    ("scene3", "O problema não é só o tamanho da conta, mas o retorno nos serviços públicos. Inscreva-se no Gráfico Aberto para ver os dados reais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-049/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-049/audio/{sc_id}.wav"
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
