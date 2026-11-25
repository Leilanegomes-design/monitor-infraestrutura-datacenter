import datetime
import platform
import subprocess
import time
import psutil

# Configurações de limite (simulando regras de alerta de um Data Center)
LIMITE_CPU = 80.0
LIMITE_RAM = 85.0
SERVIDORES = ["8.8.8.8", "1.1.1.1", "://google.com"]


def registrar_log(mensagem):
    """Salva eventos e alertas em um arquivo de texto com data e hora."""
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{agora}] {mensagem}\n"
    with open("logs_datacenter.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(linha)


def verificar_ping(host):
    """Testa se um servidor responde ao ping (funciona em Windows e Linux)."""
    parametro = "-n" if platform.system().lower() == "windows" else "-c"
    comando = ["ping", parametro, "1", host]
    resposta = subprocess.run(
        comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    return resposta.returncode == 0


def monitorar():
    print("=== INICIANDO MONITORAMENTO DE INFRAESTRUTURA ===")
    print("Pressione Ctrl + C no terminal para encerrar.\n")
    registrar_log("Sistema de monitoramento iniciado.")

    try:
        while True:
            # 1. Coleta dados de Hardware
            uso_cpu = psutil.cpu_percent(interval=1)
            uso_ram = psutil.virtual_memory().percent
            uso_disco = psutil.disk_usage("/").percent

            agora = datetime.datetime.now().strftime("%H:%M:%S")
            print(
                f"[{agora}] HARDWARE -> CPU: {uso_cpu}% | RAM: {uso_ram}% | Disco: {uso_disco}%"
            )

            # 2. Checa alertas de Hardware
            if uso_cpu > LIMITE_CPU:
                alerta = f"ALERTA CRÍTICO: Uso de CPU alto ({uso_cpu}%)"
                print(f"   ⚠️ {alerta}")
                registrar_log(alerta)

            if uso_ram > LIMITE_RAM:
                alerta = f"ALERTA CRÍTICO: Uso de RAM alto ({uso_ram}%)"
                print(f"   ⚠️ {alerta}")
                registrar_log(alerta)

            # 3. Testa conectividade de Rede
            for servidor in SERVIDORES:
                online = verificar_ping(servidor)
                status = "ONLINE" if online else "OFFLINE"
                print(f"   🌐 Servidor {servidor}: {status}")

                if not online:
                    alerta_rede = f"FALHA DE REDE: Servidor {servidor} não responde ao ping."
                    print(f"   🚨 {alerta_rede}")
                    registrar_log(alerta_rede)

            print("-" * 55)
            time.sleep(5)  # Aguarda 5 segundos para a próxima verificação

    except KeyboardInterrupt:
        print("\nMonitoramento encerrado pelo operador.")
        registrar_log("Sistema de monitoramento encerrado.")


if __name__ == "__main__":
    monitorar()