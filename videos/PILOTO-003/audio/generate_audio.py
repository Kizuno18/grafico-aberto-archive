import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Quando se fala em transição energética e energia limpa no noticiário internacional, a impressão que dá é que o mundo inteiro está muito atrasado. Mas quando olhamos para os números oficiais da geração de eletricidade, o Brasil está em uma posição completamente diferente do resto do planeta. Segundo os dados da Empresa de Pesquisa Energética e da Agência Internacional de Energia, quase 88% de toda a eletricidade consumida no Brasil vem de fontes renováveis, contra uma média mundial de apenas 30%."),
    ("scene2", "A base do nosso sistema elétrico continua sendo a água: as usinas hidrelétricas respondem por cerca de 58% de toda a geração. Mas nos últimos anos, uma verdadeira revolução aconteceu no Nordeste e no Sul do país. A energia eólica cresceu em ritmo acelerado e já responde por quase 15% do total. Somando a biomassa da cana-de-açúcar e a explosão recente dos painéis solares, as três novas fontes renováveis já geram quase um terço de toda a nossa luz."),
    ("scene3", "Para entender o tamanho da nossa vantagem na eletricidade, basta ver o que o resto do mundo ainda queima para ligar computadores e indústrias. A maior fonte de eletricidade do planeta Terra continua sendo o carvão mineral, responsável por mais de 35% de toda a energia global, seguido pelo gás fóssil com mais de 22%. No Brasil, o carvão mineral não chega sequer a 2% da nossa matriz elétrica."),
    ("scene4", "Isso não significa que o Brasil não tenha desafios: dependemos do regime de chuvas, precisamos de milhares de quilômetros de linhas de transmissão e o setor de transportes ainda queima muito petróleo. Mas na tomada de casa, a nossa matriz é uma das mais limpas do planeta. Para mais análises visuais baseadas em dados e fatos reais, inscreva-se no Gráfico Aberto.")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/PILOTO-003/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/PILOTO-003/audio/{sc_id}.wav"
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
