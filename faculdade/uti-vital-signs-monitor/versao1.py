import numpy as np

lista_nomes = []
lista_bpm = []

print("=== MATRIZ DE BATIMENTOS CARDÍACOS (BPM) ===")

while True:
    # 1. Pega o número atual do paciente usando o len + 1
    numero_paciente = len(lista_nomes) + 1
    
    # 2. Seus inputs normais com f-string
    nome = input(f"\nQual o nome do(a) paciente {numero_paciente}? ")
    entrada_bpm = input(f"Insira as medições de BPM de {nome} (separadas por vírgula): ")
    
    # 3. Tratamento do split e guarda nas listas
    medicoes = [int(valor.strip()) for valor in entrada_bpm.split(',')]
    lista_nomes.append(nome)
    lista_bpm.append(medicoes)
    
    # 4. A PERGUNTA DE UX: Quer continuar?
    print("\nDeseja cadastrar mais um paciente?")
    resposta = input("Digite [1] para SIM ou [2] para NÃO: ").strip()
    
    if resposta == '2':
        print("\nCadastro finalizado!")
        break # Encerra o loop while e segue para o NumPy

# Guarda os dados nas nossas listas principais
lista_nomes.append(nome)
lista_bpm.append(medicoes)

# Segundo Passo: Calcular a média de cada paciente.
medias = np.mean(lista_bpm, axis=1) #usamos axis=1 para que o numpy leia as linhas de forma horizontal, em caso de uso do axis=0 a leitura seria de forma vertical. 

# Terceiro Passo: Encontrar o Pico (Maior Valor) de cada paciente
#picos = np.max(BPM, axis=1)
#print(picos) 

# Quarto Passo: Triagem Automática (Filtro de Taquicardia)
#Na saúde, um batimento acima de 100 BPM em repouso pode indicar taquicardia. 
#Queremos que o sistema identifique automaticamente quais pacientes ultrapassaram esse limite, sem precisarmos de um if ou for.
#alerta = picos > 100
#print(alerta)

# Quinto Passo: Descobrir o ID do Paciente Crítico
#pacientes_criticos = np.where(alerta)
#print(pacientes_criticos)

print(lista_nomes)
print(lista_bpm)
print(medias)
