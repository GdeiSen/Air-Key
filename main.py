from pynput.keyboard import Listener
import src.scenes.inputModeScene as inputModeScene
import src.scenes.outputModeScene as outputModeScene
import src.scenes.settingsScene as settingsScene
import src.utils.settingsStorageUtil as settingsStorageUtil

while True:

    print('''\033[1;34m
      /^       /^^/^^^^^^^         /^^   /^^  /^^^^^^^^/^^      /^^
     /^ ^^     /^^/^^    /^^       /^^  /^^   /^^       /^^    /^^ 
    /^  /^^    /^^/^^    /^^       /^^ /^^    /^^        /^^ /^^   
   /^^   /^^   /^^/^ /^^           /^ /^      /^^^^^^      /^^     
  /^^^^^^ /^^  /^^/^^  /^^         /^^  /^^   /^^          /^^     
 /^^       /^^ /^^/^^    /^^       /^^   /^^  /^^          /^^     
/^^         /^^/^^/^^      /^^     /^^     /^^/^^^^^^^^    /^^ \033[0m  
                                                        BETA   v1.0.0  
        
\033[1;35mWelcome to AIR KEY!\033[0m
This is a keylogger that sends the keystrokes to another device throw your LAN network!

\033[4mSelect mode (number) of type of current device:\033[0m
1. Set current device as output 
2. Set current device as input
3. Load saved configuration
4. Settings and configuration
5. Exit
    ''')
    storageUtil = settingsStorageUtil.StorageUtil()
    storageUtil.check()
    mode = input()
    if mode == '1': outputModeScene.outputModeSceneFunc(None, None)
    elif mode == '2': inputModeScene.inputModeSceneFunc(None, None)
    elif mode == '3':
        try:
            mode = storageUtil.getMode()
            ip = storageUtil.getIp()
            port = storageUtil.getPort()
            if mode == '1': outputModeScene.outputModeSceneFunc(ip, port)
            elif mode == '2': inputModeScene.inputModeSceneFunc(ip, port)
        except(Exception) as err:
            print (err)
            print('''
\033[1;31mError while loading settings!\033[0m
\033[1;4mThis may be because of:\033[0m
\033[1m1. Wrong settings file\033[0m
    Check if the settings file is in the same directory as the program
\033[1m2. Wrong mode\033[0m
    Check if the mode is correct
\033[1m3. Wrong IP address \033[0m
    Check current device local IP address and try again
\033[1m4. Wrong port\033[0m
    Check is the port is open and not used by another program
\033[1m5. Firewall or antivirus\033[0m
    Check if the firewall or antivirus is blocking the connection or program
\033[1m6. Input device host is offline\033[0m
    Device air key host that you are trying to connect to is not online.
            ''')
            exit()
    elif mode == '4': settingsScene.settingsSceneFunc()
    elif mode == '5': exit()
        