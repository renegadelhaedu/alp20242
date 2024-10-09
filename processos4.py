import wmi

f = wmi.WMI()

print("pid   Nome do processo")

for process in f.Win32_Process():

    print(f"{process.ProcessId:<10} {process.Name}")