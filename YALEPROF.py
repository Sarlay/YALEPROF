import subprocess, sys  
from subprocess import check_output
from subprocess import Popen, PIPE
from time import sleep
import subprocess

directory = "C:\\Users\\ELVE~1\\AppData\\Local\\Temp"

def write_temp_files():
    with open(f'{directory}\\YALEPROF.ps1', 'w+') as f:
        f.write('Get-NetTCPConnection -LocalPort 11100 | Select-Object -Property LocalAddress, LocalPort, RemoteAddress, RemotePort, State | Sort-Object LocalPort |ft')
        f.close()

    with open('C:\\Users\\ELVE~1\\AppData\\Local\\Temp\\popup.vbs', 'w+') as f:
        f.write('''

        Sample = msgBox("YA LA PROF qui t'espionne" & vbCrLf & vbCrLf & "VOULEZ VOUS FUIR ????",16+32+4, "YA LE PROF !!!")
        Select Case Sample
            Case 6
                Dim objShell
                Set objShell = CreateObject("WScript.Shell")
                objShell.Run("""C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"" ""https://taozhiyu.gitee.io/fake/win10ue/win10ue.html""")
                Wscript.Sleep 100
                objShell.SendKeys "{F11}"
                WScript.Quit
            Case 7
                wScript.Echo "Ok mais le prof te surveille toujours"
        End Select''')
        f.close()
    with open('C:\\Users\\ELVE~1\\AppData\\Local\\Temp\\pasla.vbs', 'w+') as f:
        f.write('''Sample = msgBox("LA PROF EST PARTI" & vbCrLf & vbCrLf & "Vous n'etes plus surveillé",0+64, "LE PROF EST PARTI !!!")''')
        f.close()


write_temp_files()


monitored = False
while True:
    p = subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "C:\\Users\\ELVE~1\\AppData\\Local\\Temp\\YALEPROF.ps1"', stdout=PIPE)
    text = p.communicate()[0]
    if b"Established" in text and monitored is False: # teacher started to monitor you
        subprocess.call(['cscript.exe', f'{directory}\\popup.vbs'])
        sleep(10)
        monitored = True # update state to monitored
    elif b"Established" in text and monitored is True:
        print("toujours surveillé, prochaine update dans 10s")
        sleep(10)
    elif b"Established" not in text and monitored is True:
        subprocess.call(['cscript.exe', f'{directory}\\pasla.vbs']) # popup teacher left
        monitored = False # update, teacher left
    elif b"Established" not in text and monitored is False:
        print("Ya pas le prof trkl, update dans 5 secondes")
        sleep(5)

#'powershell.exe -ExecutionPolicy RemoteSigned -file "C:\Users\Elève\Documents\site\YALEPROF.ps1"', stdout=sys.stdout)
