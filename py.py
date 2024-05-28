import paramiko
import requests

# SSH параметры
ssh_host = '192.168.0.1'
ssh_port = 22
ssh_username = 'pi'
ssh_password = 'raspberry'

# URL для получения данных
url = "http://192.168.0.1:8080/v1/devices/battery"

def get_battery_data():
    try:
        # Установка SSH-соединения
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)
        
        # Выполнение HTTP-запроса на удаленной машине через SSH-туннель
        transport = ssh.get_transport()
        local_addr = ('localhost', 8080)
        remote_addr = ('192.168.0.1', 8080)
        channel = transport.open_channel("direct-tcpip", remote_addr, local_addr)
        
        response = requests.get(url, proxies={'http': 'http://localhost:8080'}, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print("Battery data:", data)
        else:
            print("Failed to retrieve data:", response.status_code)
        
        # Закрытие канала и соединения
        channel.close()
        ssh.close()
    except Exception as e:
        print(f"An error occurred: {e}")

# Вызов функции для получения данных
get_battery_data()
