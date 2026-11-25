# 🖥️ Monitor de Saúde de Hardware e Rede (Data Center)

Projeto desenvolvido em **Python** com foco no monitoramento básico de infraestrutura de servidores, simulando rotinas de operação e suporte (NOC) em ambientes de Data Center.

## 🚀 Funcionalidades
- **Monitoramento de Hardware:** Coleta em tempo real do uso de CPU, Memória RAM e Disco utilizando a biblioteca `psutil`.
- **Verificação de Conectividade:** Testes contínuos de resposta (`ping`) em servidores e DNS externos.
- **Sistema de Alertas e Logs:** Disparo de avisos visuais no terminal quando o consumo ultrapassa limites críticos e registro automático de eventos com data e hora em arquivo `.txt`.

## 🛠️ Tecnologias Utilizadas
- Python 3
- Biblioteca `psutil`
- Módulos nativos (`subprocess`, `datetime`, `platform`, `time`)

## ▶️ Como executar
1. Instale a dependência necessária:
   ```bash
   pip install psutil
   ```
2. Execute o script:
   ```bash
   python monitor_datacenter.py
   ```
