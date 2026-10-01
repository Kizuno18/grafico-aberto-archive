import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Você sabia que o papel que o mundo usa para caixas, cadernos e embalagens depende totalmente das florestas plantadas do Brasil?"),
    ("scene2", "Segundo a Indústria Brasileira de Árvores, o eucalipto no Brasil cresce em apenas sete anos, contra trinta anos na Europa e no Canadá, gerando mais de vinte e cinco milhões de toneladas."),
    ("scene3", "Cem por cento vem de florestas cultivadas, gerando dez bilhões de dólares em exportações. Inscreva-se no Gráfico Aberto para ver os dados reais!")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/SHORT-047/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/SHORT-047/audio/{sc_id}.wav"
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
