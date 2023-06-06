import time

def cronometro():
    tempo_inicial = time.time()
    
    while True:
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - tempo_inicial
        
        minutos = int(tempo_decorrido / 60)
        segundos = int(tempo_decorrido % 60)
        milissegundos = int((tempo_decorrido % 1) * 1000)
        
        print(f"{minutos:02d}:{segundos:02d}:{milissegundos:03d}", end="\r")
        time.sleep(0.001)

# Executa o cronômetro
cronometro()
