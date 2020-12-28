import socket
import ssl
import pickle
import subprocess
import platform
import os

from datetime import datetime
from send_email import send_email

class Server():
    def __init__(self, address, port, connection, priority, organization, service,mail_recipients):
        self.address = address
        self.port = port
        self.connection = connection.lower()
        self.priority = priority.lower()
        self.organization = organization.lower()
        self.service = service.lower()
        self.mail_recipients = mail_recipients.lower()
        self.alert = False
        self.message = ""
        self.subject = f"{self.organization} :: {self.address} --- {self.service} service interruption."

    def check_connection(self):
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        try:            
            if self.connection == "plain":
                socket.create_connection((self.address, self.port), timeout=10)
                self.message = f"{self.organization} :: {now} {self.address} --- {self.service} is up."
                
            elif self.connection == "ssl":
                ssl.wrap_socket(socket.create_connection((self.address, self.port), timeout=10))
                self.message = f"{self.organization} :: {now} {self.address} --- {self.service} is up."

            else:
                if self.ping():
                    self.message = f"{self.organization} :: {now} {self.address} --- {self.service} is up."
                else:
                    self.message = f"{self.organization} :: {now} {self.address} --- {self.service} is down."
                    self.alert = True

        except Exception as e:
            self.message = f"{self.organization} :: {now} {self.address} --- {self.service} is down. ({e})"
            self.alert = True

        
        if self.alert == True:
            #Send Alert email
            send_email(self.subject,self.message,self.mail_recipients)

        # self.create_history(msg,success,now)

    # def create_history(self, msg, success, now):
    #     self.mail_body.append((msg,success,now))

    def ping(self):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
            ) == "windows" else 'c', self.address ), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False


if __name__ == "__main__":
    # try:
    #     servers = pickle.load(open("servers_info.pickle", "rb"))
    # except:
    # servers = [ 
    #     Server("test.com", 80, "plain", "high","test","Test domain"),
    #     Server("reddit.com", 80, "plain", "high","reddit","reddit domain"),
    #     Server("msn.com", 80, "plain", "high","msn","msn domain"),
    #     Server("smtp.gmail.com", 465, "ssl", "high","gmail","Gmail email"),
    #     Server("hossaintest.com", 80, "ping", "high","hossaintest","hossaintest domain"),
    #     Server("192.168.0.5", 80, "ping", "high","local","local pc"),
    #     Server("yahoo.com", 80, "plain", "high","yahoo","yahoo domain")
    # ]
    mail_recipients_system_team = "suvo@atilimited.net,showmik@atilimited.net,yousha@atilimited.net,tahmid@atilimited.net"
    servers = [ 
        Server("203.130.133.165", 80, "ping", "high","Thailand","CPanel Server",mail_recipients_system_team),
        Server("203.130.133.166", 80, "ping", "high","Thailand","Server",mail_recipients_system_team),
        Server("203.130.133.166", 8088, "plain", "high","Thailand","Tomacat-7 JAVA",mail_recipients_system_team),
        Server("203.130.133.166", 80, "plain", "high","Thailand","Apache PHP-5.6",mail_recipients_system_team),
        Server("203.130.133.167", 80, "ping", "high","Thailand","Server",mail_recipients_system_team),
        Server("203.130.133.167", 8080, "plain", "high","Thailand","Tomacat-8 JAVA",mail_recipients_system_team),
        Server("203.130.133.168", 80, "ping", "high","Thailand","Server",mail_recipients_system_team),
        Server("203.130.133.168", 8082, "plain", "high","Thailand","Apache PHP-7",mail_recipients_system_team),
        Server("203.130.133.168", 80, "plain", "high","Thailand","Tomacat-8 JAVA",mail_recipients_system_team),
        Server("gpst.billingdil.com", 80, "ping", "high","MMU","Domain",mail_recipients_system_team),
        Server("gpst.billingdil.com", 80, "plain", "high","MMU","Apache PHP-5.6",mail_recipients_system_team),
        Server("gpst.billingdil.com", 8088, "plain", "high","MMU","Tomacat-8 JAVA",mail_recipients_system_team),
    ]
    file_name = datetime.now().strftime("%d-%m-%Y")+".txt"
    path = "server_monitoring_logs/"+datetime.now().strftime("%B-%Y")+"/"
    # if not os.path.exists(path): os.makedirs(path)
    logFile = open(path + file_name,"a")
    # logFile = open("server_monitoring_logs.txt", "a")
    start = f"\n\n-------------------- Start --------------------\n\n"
    end = f"\n\n-------------------- End --------------------\n\n"
    logFile.write(start) 
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    logFile.write(f"-------------------- {now} --------------------\n\n") 
    
    for server in servers:
        server.check_connection()
        print(server.message)
        logFile.write(server.message + "\n")

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    logFile.write(f"\n-------------------- {now} --------------------") 
    logFile.write(end)