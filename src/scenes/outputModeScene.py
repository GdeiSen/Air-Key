import socket, time, pynput, pyautogui
import threading
import cowsay
import socket
def outputModeSceneFunc(ip, port):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        cowsay.cow(f'''Your ip adresses: {s.getsockname()[0]}''')
    except:
        cowsay.cow(f'''I can't get your local ip! Do it by yourself now''')

    if ip is None:
        print('''
\033[1;35mOutput device mode activated\033[0m
\033[4mPlease enter the IP address of the device that will receive the keystrokes:\033[0m
        ''')
        ip = input()
    if port is None:
        print('''
\033[4mPlease enter the port of the device that will receive the keystrokes:\033[0m
        ''')
        port = input()
    print('''
\033[1;35mStarting AIR KEY...\033[0m''')
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    attempt = 0
    while attempt < 4:
        try:
            conn.connect((ip, int(port)))
            attempt = 5
        except:
            if attempt > 2:
                print('''
\033[1;31mError while connecting to the device!\033[0m
\033[1;4mThis may be because of:\033[0m
\033[1m1. Wrong IP address \033[0m
    Check current device local IP address and try again
\033[1m2. Wrong port\033[0m
    Check is the port is open and not used by another program
\033[1m3. Wrong mode\033[0m
    Check if the device is in the right mode
\033[1m4. Firewall or antivirus\033[0m
    Check if the firewall or antivirus is blocking the connection or program     
\033[1m5. Input device host is offline\033[0m
    Device air key host that you are trying to connect to is not online.
            ''')
                conn.close()
                return()
            else :
                print(f'''
\033[1;31mCannot establish connection!\033[0m
Next attempt in 5 seconds...\033[0m
                    ''')
                time.sleep(5)
                attempt += 1

    print ('''
\033[1;32mConnected to the device! \033[0m
        ''')

    print (f'''
Connected to {ip}:{port} successfully!
Now you can start typing on this computer and the keystrokes will be sent to the other device!''')
    global activate
    activate = False
    def mouse_listener():
        def on_click(x, y, button, pressed):
            if pressed:
                activation_area = 100
                global activate
                with open("settings.txt", 'r') as f:
                    data = f.read()
                    data = data.split('\n')
                    activation_area = data[4]
                    activation_area = int(activation_area)
                    if data[3] != True and data[3] != 'True' and data[3] != 'true' and data[3] != '1':
                        activation_area = 0
                        activate = True
                if y > pyautogui.size().height - activation_area and button == pynput.mouse.Button.left:
                    activate = not activate
                    print (f"Typing mode {'activated' if activate else 'deactivated'}")
                    
        listener = pynput.mouse.Listener(on_click=on_click)
        listener.start()

    def keyboard_listener():
        def on_press(key):
            if not activate:
                return
            data = str(key)
            if len (data) > 3 :
                data = data[4:]
            else:
                data = data[1:-1] 
            conn.send(data.encode('utf-8'))
        listener = pynput.keyboard.Listener(on_press=on_press)
        listener.start()

    thread2 = threading.Thread(target=(mouse_listener()))
    thread1 = threading.Thread(target=(keyboard_listener()))
    thread2.start()
    thread1.start()
    time.sleep(200000)
    cowsay.cow('''I am tired of waiting, I am going to sleep now!''')
    conn.close()
