import ftplib
import os


class ftpclient():

    def __init__(self):
        self.ftp = 0
        self.data = []
        self.curdir = ""

    def loginToServer (self, server, username, password):
        """Logins into server"""
        self.ftp= ftplib.FTP(server)
        return self.ftp.login(username, password)

    def getDir(self):
        """gets current directory and displays it"""
        self.data = []
        self.ftp.dir(self.data.append)
        return self.data

    def showDir(self):
        """Print curDir"""
        for line in self.data:
            print "-", line

    def changeDir (self, dir):
        """changes dir """
        self.curdir = self.ftp.pwd() + dir
        self.ftp.cwd(self.curdir)

    def getFile(self, filename):
        try:
            self.ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
        except:
            print "Error"

    def upFile(self,filename):
        ext = os.path.splitext(filename)[1]
        if ext in (".txt", ".htm", ".html"):
            self.ftp.storlines("STOR " + filename, open(filename))
        else:
            self.ftp.storbinary("STOR " + filename, open(filename,"rb"), 1024)

    def quit(self):
        """exit ftp connection"""
        self.ftp.quit()

if __name__ == '__main__':
    client = ftpclient()
    client.loginToServer("ftp.nluug.nl", "anonymous", "ftplib-example-1")
    client.getDir()
    client.showDir()
    print '\n'
    client.changeDir("pub/")
    client.getDir()
    client.showDir()
