#!/usr/env/python3
# Author: KenjiDoom
import pexpect



def main():
    print (""" 

            Password list file.
            Enter the BaseDIR & MountDIR
            """)

    passfile = input("> ")
    fileopen = open(passfile,  'r') # rb for bytes inlcuded

    for password in fileopen: # This will give it the loop
        passwords = password.strip() # Now we need a destination for the passwords
        command1 = pexpect.spawn('cryfs /home/%USER/.local/share/plasma-vault/test_today.enc/ /home/%USER/Vaults/test_today')
        command1.expect('Password:')
        command1.sendline(password)
        result = command1.expect(['Error 11: Could not load config file. Did you enter the correct password?', 'Mounting filesystem. To unmount, call:'])
        if result == 0:
            print ("Still bruteforcing using " + password)
        elif result == 1:
            print ("Bruteforce Complete, The password was " + password)
            break







main()
