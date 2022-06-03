import socket
import psutil
import shutil

def main():

    if psutil.cpu_percent() > 80:
        send_email("Error - CPU usage is over 80%")

    # works for linux.
    if psutil.disk_usage("/").percent < 20:
        send_email("Error - Available disk space is less than 20%")

    # 4th index stores the free memory in bytes.
    if (psutil.virtual_memory()[4] / 1024 / 1024) < 500:
        send_email("Error - Available memory is less than 500MB")

    if (socket.gethostbyname("localhost")) != "127.0.0.1":
        send_email("Error - localhost cannot be resolved to 127.0.0.1")
        

def send_email(error_title):
    from emails import 

    message = EmailMessage()
    sender = "automation@example.com"
    receiver = "username@example.com"

    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = error_title

    body = '''
    Please check your system and resolve the issue as soon as possible.
    '''

    message.set_content(body)






if __name__ == '__main__':
    main()