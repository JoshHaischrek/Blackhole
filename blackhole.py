#I, Joshua Haischrek 000365474, certify that this material is my original work. No other person's work has been used without due acknowledgement.
import os

def blackhole():
    if os.name == 'nt': #this is Windows
        hostfile = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
    else:               #This is Linux or Mac
        hostfile = '/etc/hosts'

    #user input section
    fqdn = input("Enter the fully qualified domain name: ")
    with open(hostfile) as file:
        current_hosts = file.readlines()
        for current_host in current_hosts:
            if fqdn in current_host:
                print("The domain is already in the host file.")
        else file.write("0.0.0.0 {fqdn}\n")
except FileNotFoundError:
    print ("The host file could not be found.")

    