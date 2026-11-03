# 🏥 UTI Vital Signs Monitor

**Monitoramento de sinais vitais em UTI com NumPy**

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-00995D?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/NumPy-00995D?style=flat-square&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Origem-Faculdade-00995D?style=flat-square" alt="Origem">
  <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-00995D?style=flat-square" alt="Status">
</p>

Mini projeto prático desenvolvido para aplicar os fundamentos da biblioteca **NumPy** em um cenário real de saúde: a análise estatística e a triagem automática da frequência cardíaca (BPM) de pacientes internados em UTI.

---

## 🩺 Contexto

Em uma UTI, os sinais vitais de vários pacientes são medidos ao longo do dia. Revisar esses números um a um é lento e sujeito a erro. A pergunta que guiou o projeto foi:

> *Como identificar rapidamente, em um conjunto de medições, quais pacientes apresentaram sinais de taquicardia?*

---

## 🎯 Objetivo

Demonstrar o uso de **computação vetorizada** para calcular médias, identificar picos de BPM e sinalizar casos de taquicardia **sem laços manuais**, deixando o NumPy fazer o trabalho pesado sobre a matriz inteira de uma só vez.

---

## 🧪 Conceitos aplicados

| Conceito | Para que foi usado |
| :--- | :--- |
| **Arrays 2D (`ndarray`)** | Estruturar os dados: cada linha é um paciente e cada coluna, uma medição horária. |
| **Operações por eixo (`axis=1`)** | Calcular a média e o valor máximo de BPM de cada paciente, linha por linha. |
| **Máscaras booleanas** | Filtrar de uma vez todas as medições acima de 100 BPM. |
| **`np.where`** | Localizar os índices exatos dos pacientes em estado crítico. |

---

## ⚙️ Lógica da triagem

```text
Matriz de BPM  →  média e máximo por paciente  →  máscara (BPM > 100)  →  np.where  →  pacientes sinalizados
 (pacientes ×        (axis=1)                      (booleana)             (índices)       (relatório)
  horários)
```

### Ideia central (exemplo ilustrativo)

```python
import numpy as np

# Linhas = pacientes | Colunas = medições horárias de BPM
bpm = np.array([
    [72, 75, 78, 74],
    [88, 95, 104, 110],
    [65, 68, 70, 66],
])

media = bpm.mean(axis=1)             # média por paciente
maximo = bpm.max(axis=1)             # pico por paciente
taquicardia = bpm > 100              # máscara booleana
criticos = np.where(taquicardia.any(axis=1))[0]   # índices dos pacientes sinalizados
```

---

## 📁 Arquivos do projeto

| Arquivo | O que faz |
| :--- | :--- |
| `versao1_matriz_bruta.py` | Foco no motor matemático e na manipulação direta de matrizes numéricas. |
| `versao2_interativo_ux.py` | Versão completa, com cadastro dinâmico de pacientes pelo terminal, integração com NumPy e relatório de triagem amigável. |

> **Evolução:** a versão 1 resolve o problema matemático e a versão 2 o transforma em uma ferramenta utilizável, aplicando também os ensinamentos de experiência de usuário vistos em aula.

---

## ▶️ Como rodar

```bash
pip install numpy
python versao1_matriz_bruta.py
python versao2_interativo_ux.py
```

---

## 📚 Aprendizados

- Vetorizar elimina laços e deixa o código mais curto e legível.
- Máscaras booleanas e `np.where` transformam uma regra clínica em uma única linha de código.
- Separar o "motor" matemático da interface (versão 1 e versão 2) facilita testar e evoluir cada parte.

---


> ⚠️ **Aviso:** projeto estritamente educacional. Os limites e a lógica usados aqui são simplificados.

<p align="center">
  <a href="../README.md">← Voltar para Faculdade</a>
</p>
