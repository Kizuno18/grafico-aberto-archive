import wave
from piper import PiperVoice

voice = PiperVoice.load("tools/voices/pt_BR-faber-medium.onnx")

scenes = [
    ("scene1", "Quando o Real começou a circular em julho de 1994, uma nota de cem reais era uma quantia impressionante. Mais de três décadas depois, essa mesma cédula de cem continua existindo no nosso bolso, mas o valor real dela mudou completamente. Segundo os dados oficiais do Banco Central e do IBGE, a inflação acumulada no período ultrapassou 790%, o que significa que cem reais de 1994 equivalem a quase 900 reais nos dias de hoje."),
    ("scene2", "Se fizermos a conta inversa, o resultado é ainda mais impressionante: uma cédula de cem reais hoje compra o equivalente a apenas onze reais e vinte e três centavos da época do lançamento. Ou seja, a nota perdeu quase 89% de todo o seu poder de compra. Isso não significa que o Plano Real falhou, mas sim que mesmo com inflação moderada e controlada, o tempo corrói o valor nominal de qualquer moeda fiduciária."),
    ("scene3", "Para entender o tamanho dessa diferença na prática, basta olhar para o salário mínimo e a comida na mesa. Em julho de 1994, o salário mínimo era de 64 reais e 79 centavos. Uma única nota de cem pagava mais de um salário e meio. Hoje, o salário mínimo passa de 1.500 reais, e cem reais representam menos de 7% dele. No supermercado, a mesma nota que comprava uma cesta básica e meia do DIEESE em 1994, hoje não paga sequer 15% dos mesmos alimentos."),
    ("scene4", "Esse histórico mostra por que deixar dinheiro parado perdendo para a inflação custa tão caro no longo prazo, e por que a estabilidade de preços é a base de qualquer economia saudável. Para mais explicações diretas baseadas em dados oficiais e gráficos descomplicados, inscreva-se no Gráfico Aberto.")
]

sample_rate = voice.config.sample_rate

for sc_id, text in scenes:
    with open(f"videos/PILOTO-002/audio/{sc_id}.txt", "w", encoding="utf-8") as f:
        f.write(text)
        
    out_wav = f"videos/PILOTO-002/audio/{sc_id}.wav"
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
