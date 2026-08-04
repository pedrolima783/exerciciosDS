logs_brutos = [
    "2024-07-15 08:42:17 | ERROR | auth-service | ip=192.168.4.21 | Login failed: invalid credentials",
    "2024-07-15 08:43:02 | INFO  | api-gateway  | ip=10.0.0.5     | Request completed: 200 OK",
    "2024-07-15 08:43:45 | WARN  | db-connector | ip=10.0.1.12    | Connection pool at 87% capacity",
    "2024-07-15 08:44:10 | ERROR | auth-service | ip=192.168.4.21 | Login failed: invalid credentials",
    "2024-07-15 08:46:30 | CRITICAL | firewall  | ip=192.168.4.21 | Port scan detected: 1024 ports/5s"
]
print("=== Iniciando Triagem de Logs do SOC ===\n")
for log in logs_brutos:
    campos = [campo.strip() for campo in log.split("|")]
    
    nivel = campos[1]
    origem_raw = campos[3]
    mensagem = campos[4]
    ip = origem_raw.replace("ip=", "")
    if nivel in ["ERROR", "CRITICAL"]:
        print(f"⚠️ ALERTA DE SEGURANÇA! Nível: {nivel} | Origem: {ip} | Mensagem: {mensagem}")
