import unittest
import os
from ftpclient import ftpclient as ftp


class ftpclientTest(unittest.TestCase):

    def test_init(self):
        self.client = ftp.ftpclient()
        self.assertEquals(self.client.ftp, 0)

    def test_login(self):
        self.client = ftp.ftpclient()
        a = self.client.loginToServer("ftp.nluug.nl", "anonymous", "ftplib-example-1")
        self.assertNotEquals(a, 0)
        self.client.quit()

    def test_getDir(self):
        self.client = ftp.ftpclient()
        self.client.loginToServer("ftp.nluug.nl", "anonymous", "ftplib-example-1")
        data = self.client.getDir()
        self.assertTrue(data)
        self.client.quit()

    def test_changeDir(self):
        self.client = ftp.ftpclient()
        self.client.loginToServer("ftp.nluug.nl", "anonymous", "ftplib-example-1")
        data = self.client.getDir()
        self.assertTrue(data)
        self.client.changeDir('pub/')
        data2 = self.client.getDir()
        self.assertNotEqual(data, data2)
        self.client.quit()

    def test_getFile(self):
        self.client = ftp.ftpclient()
        self.client.loginToServer("ftp.nluug.nl", "anonymous", "ftplib-example-1")
        self.client.changeDir("pub/")
        self.client.getDir()
        self.client.getFile("robots.txt")
        self.assertTrue(os.path.isfile("robots.txt"))
        if os.path.isfile("robots.txt"):
            os.remove("robots.txt")

    def test_upFile(self):
        self.client = ftp.ftpclient()
        self.client.loginToServer("ftp.nluug.nl", "anonymous", "ftplib-example-1")
        self.client.changeDir("pub/")
        self.client.getDir()
        self.client.getFile("robots.txt")
        self.assertTrue(os.path.isfile("robots.txt"))
        self.client.quit()
        self.client.loginToServer("127.0.0.1", "thymaster", "fuck")
        self.client.getDir()
        self.client.upFile("robots.txt")
        if os.path.isfile("robots.txt"):
            os.remove("robots.txt")
        self.assertTrue(os.path.isfile("/home/thymaster/robots.txt"))
        if os.path.isfile("/home/thymaster/robots.txt"):
            os.remove("/home/thymaster/robots.txt")

if __name__ == '__main__':
    unittest.main()