import src.utils.settingsStorageUtil as settingsStorageUtil

def settingsSceneFunc():
     storageUtil = settingsStorageUtil.StorageUtil()
     with open("settings.txt", 'r') as f:
            print (f'''
\033[1;35mSettings page activated\033[0m
\033[1;4mSet connection data:\033[0m
IP address: \033[34m{storageUtil.getIp()}\033[0m
Port: \033[34m{storageUtil.getPort()}\033[0m
Mode: \033[34m{storageUtil.getMode()}\033[0m

\033[1;4mSet applciation data:\033[0m
Click screen bottom to activate: \033[34m{storageUtil.getActivate()}\033[0m
Bottom screen activation area height: \033[34m{storageUtil.getHeight()}\033[0m

\033[1;4mSelect option (number) to change:\033[0m
1. IP address
2. Port
3. Mode
4. Click screen bottom to activate/deactivate typing mode
5. Bottom screen activation area height
6. Exit
''')
            
            option = input()
            if option == '1':
                print('\n\033[1;4mEnter new IP address:\033[0m')
                ip = input()
                storageUtil.setIp(ip)
                print('\n\033[1;32mIP address changed!\033[0m')
    
            elif option == '2':
                print('\n\033[1;4mEnter new port:\033[0m')
                port = input()
                storageUtil.setPort(port)
                print('\n\033[1;32mPort changed!\033[0m')
                
            elif option == '3':
                print('\n\033[1;4mEnter new mode:\033[0m')
                mode = input()
                storageUtil.setMode(mode)
                print('\n\033[1;32mMode changed!\033[0m')
              
            elif option == '4':
                print('\n\033[1;4mClick screen bottom to activate/deactivate typing mode:\033[0m')
                activate = input()
                storageUtil.setActivate(activate)
                print('\n\033[1;32mClick screen bottom to activate/deactivate typing mode changed!\033[0m')
               
            elif option == '5':
                print('\n\033[1;4mBottom screen activation area height:\033[0m')
                height = input()
                storageUtil.setHeight(height)
                print('\n\033[1;32mBottom screen activation area height changed!\033[0m')
            
            elif option == '6':
                return
                
            settingsSceneFunc()
                