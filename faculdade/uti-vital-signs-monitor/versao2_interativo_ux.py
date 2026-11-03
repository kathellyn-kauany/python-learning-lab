"""
Projeto: Monitoramento de UTI com NumPy — Versão 2 (Interativa & UX)
Descrição: Evolução do motor matemático para uma aplicação interativa completa. 
           Permite o cadastro dinâmico de pacientes via terminal, construção automática 
           da matriz multidimensional e geração de relatórios de triagem amigáveis ao usuário.
Tecnologias: Python 3, NumPy, Tratamento de Strings e Loops Dinâmicos.
"""

import numpy as np

# 1. CADASTRO DE PACIENTES E MEDIÇÕES
lista_nomes = []
lista_bpm = []

print("=== CADASTRO DE PACIENTES - MONITORAMENTO UTI ===")

while True:
    idx = len(lista_nomes) + 1
    nome = input(f"\nNome do paciente #{idx}: ").strip()
    entrada = input(f"Digite as medições de BPM de {nome} (separadas por vírgula): ")
    
    medicoes = [int(val.strip()) for val in entrada.split(',')]
    lista_nomes.append(nome)
    lista_bpm.append(medicoes)
    
    opcao = input("Deseja cadastrar outro paciente? [1] Sim | [2] Não: ").strip()
    if opcao == '2':
        break

# 2. PROCESSAMENTO COM NUMPY
bpm_dados = np.array(lista_bpm)

media_pacientes = np.mean(bpm_dados, axis=1)
pico_bpm = np.max(bpm_dados, axis=1)
media_uti = np.mean(bpm_dados)

pacientes_criticos = pico_bpm > 100
ids_alerta = np.where(pacientes_criticos)[0]

# 3. EXIBIÇÃO DO RELATÓRIO
print("\n" + "="*40)
print("=== RELATÓRIO DO TURNO ===")
print("="*40)

for i in range(len(lista_nomes)):
    print(f"Paciente: {lista_nomes[i]} | Média = {media_pacientes[i]:.1f} BPM | Pico = {pico_bpm[i]} BPM")

print(f"\nMédia Geral da UTI: {media_uti:.1f} BPM")

print("\n=== TRIAGEM AUTOMÁTICA (RISCO DE TAQUICARDIA) ===")
if len(ids_alerta) > 0:
    nomes_alerta = [lista_nomes[idx] for idx in ids_alerta]
    print(f"🚨 ALERTA: Os seguintes pacientes registraram picos acima de 100 BPM: {', '.join(nomes_alerta)}")
else:
    print("✅ Nenhum paciente registrou episódios de taquicardia.")
