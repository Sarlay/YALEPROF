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
                objShell.Run("""C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"" ""https://fakeupdate.net/win10ue/""")
                Wscript.Sleep 100
                objShell.SendKeys "{F11}"
                WScript.Quit
            Case 7
                wScript.Echo "Ok mais le prof te surveille toujours"
        End Select''')
        f.close()


write_temp_files()


while True:
    p = subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "C:\\Users\\ELVE~1\\AppData\\Local\\Temp\\YALEPROF.ps1"', stdout=PIPE)
    text = p.communicate()[0]
    if b"Established" in text:
        subprocess.call(['cscript.exe', f'{directory}\\popup.vbs'])
        sleep(10)
    else:
        sleep(10)

#'powershell.exe -ExecutionPolicy RemoteSigned -file "C:\Users\Elève\Documents\site\YALEPROF.ps1"', stdout=sys.stdout)