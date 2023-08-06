import socket, pynput, sys
import cowsay
def inputModeSceneFunc(ip, port):
    
    try:
        host = socket.getaddrinfo(socket.gethostname(), None)
        ipv4_addresses = [i[4][0] for i in host if i[0] == socket.AF_INET]
        cowsay.cow(f'''Your ip adresses: {ipv4_addresses}''')
    except:
        cowsay.cow(f'''Your ip adresses: {socket.gethostbyname(socket.gethostname())}''')


    if ip is None:
        print('''
\033[1;35mInput device mode activated\033[0m
\033[4mPlease enter the IP address of the device that will receive the keystrokes:\033[0m
        ''')
        ip = input()

    if port is None:
        print('''
\033[4mPlease enter the port that will receive the keystrokes: \033[0m
            ''')
        port = input()

    print('''
\033[1;35mStarting AIR KEY...\033[0m
        ''')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((ip, int(port)))
        s.listen(5)
    except:
            print('''
\033[1;31mError while working on host!\033[0m
\033[1;4mThis may be because of:\033[0m
\033[1m1. Wrong IP address \033[0m
    Check current device local IP address and try again
\033[1m2. Wrong port\033[0m
    Check is the port is open and not used by another program
\033[1m3. Wrong mode\033[0m
    Check if the device is in the right mode
\033[1m4. Firewall or antivirus\033[0m
    Check if the firewall or antivirus is blocking the connection or program     
            ''')
            s.close()
            return()
    print(f"""
\033[1;32mEverything is ready!\033[0m
Your IP address is: {ip}
Your port is: {port}
Now enter this IP address and port on the other device and start typing!""")
    while True:
        try:
            clientsocket, address = s.accept()
        except:
            print("""
\033[1;31mError while accepting connection!\033[0m
\033[1;4mThis may be because of:\033[0m
\033[1m1. Output device is already running \033[0m
    Check if the output device is already running and close it. Then try again
\033[1m2. Wrong mode\033[0m
    Check if the device is in the right mode
\033[1m3. Firewall or antivirus\033[0m
    Check if the firewall or antivirus is blocking the connection or program
\033[1m4. Something else could happen\033[0m
    Check if the output device is running and if the IP address and port are correct""")
            s.close()
            return()
        print(f'''
\033[1;35mConnection with {address} has been established!\033[0m
Now this device has control over the other device!''')
        while True:
            try:
                data = clientsocket.recv(1024)
                if not data:
                    break
                data = data.decode('utf-8')
                if len(data) > 1:
                    pynput.keyboard.Controller().press(getattr(pynput.keyboard.Key, data))
                else:
                    try:
                        pynput.keyboard.Controller().type(data)
                    except:
                        pass
            except:
                print(f"""
\033[1;31mConnection from {address} is closed!\033[0m
Now looking for new connections!""")
                