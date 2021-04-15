# BrokenVaults
Understanding how bruteforcing works by creating a script that will bruteforce KDE-Vaults.
As of now the script will only work with cryfs encryption program. Later updates will inlcude Encfs and gocryptfs

### Requirements
```
pip install pexpect 
```

### Manual
```
$ python main.py
usage: main.py [-h] -w -b -m

BrokenVaults is a tool used for bruteforcing KDE-Vaults using the cryfs method.

positional arguments:
  -w          Wordlist file, password file location, must be a txt file.
  -b          The base directory, ENC file location.
  -m          Mount directory for the ENC file.

optional arguments:
  -h, --help  show this help message and exit
```
Running the progam on a vault
```
$ python main.py rockyou.txt /home/$USER/.local/share/plasma-vault/test.enc /home/$USER/Vaults/test
Attacking [/home/$USER/.local/share/plasma-vault/test.enc] with: iloveyou

Attacking [/home/$USER/.local/share/plasma-vault/test.enc] with: password

Done [/home/$USER/.local/share/plasma-vault/test.enc] [/home/$USER/Vaults/test] Password:123

```
![](https://github.com/KenjiDoom/BrokenVaults/blob/main/terminal_video.gif)

### Release History
* 0.0.1
    * Uploaded orginal piece of code & fixed issues
    * Updated the README.md 
* 0.0.2
    *  Made the output look more hackerish
    *  better user input with argparse 
* 0.0.3
    * 
