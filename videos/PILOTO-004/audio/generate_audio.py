import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Todo brasileiro sabe que paga muito imposto: a carga tributária total do país gira em torno de 33% de tudo o que a economia produz em um ano. Mas a grande pergunta que quase ninguém faz é: de onde exatamente o governo arrecada esse dinheiro? Quando olhamos os relatórios oficiais da Receita Federal, descobrimos uma estrutura tributária completamente diferente da maioria dos países desenvolvidos do mundo."),
    ("scene2", "Diferente do que muita gente imagina, a maior fonte de arrecadação do país não é o Imposto de Renda. Quase metade de todos os tributos nacionais, cerca de 44%, incide diretamente sobre o consumo de produtos e serviços, embutida nos preços através de impostos como ICMS, PIS, Cofins e ISS. A tributação sobre a renda e os lucros responde por apenas 23%, e o patrimônio, como imóveis e carros, por menos de 5%."),
    ("scene3", "Essa dependência excessiva de impostos sobre o consumo cria o que os economistas chamam de sistema regressivo. Segundo a Pesquisa de Orçamentos Familiares do IBGE e estudos do IPEA, famílias que ganham até dois salários mínimos gastam quase tudo o que recebem no mês para comer e viver, comprometendo mais de 26% de sua renda total pagando tributos embutidos. Já para os 10% mais ricos, esse peso cai para cerca de 10% da renda."),
    ("scene4", "Na média dos países da OCDE, os tributos sobre renda e lucro representam mais de 34% da receita, aliviando o peso nos preços dos alimentos e do consumo básico. Compreender como os impostos são cobrados é o primeiro passo para debater qualquer reforma real no país. Para mais explicações baseadas em dados oficiais e gráficos descomplicados, inscreva-se no Gráfico Aberto.")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/PILOTO-004/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/PILOTO-004/audio/{sc_id}.wav"
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
