""" python runner for ftp   """

import ftplib

class FtpParser:
    def __init__(self):
        self._host = "ftp://ftp.dlptest.com/"
        self._user = "dlpuser@dlptest.com"
        self._pw = "SzMf7rTE4pCrf9dV286GuNe4N"

    @property
    def host(self):
        return self._host

    @property
    def user(self):
        return self._user

    def upload_file(self):
        FTP_HOST = "ftp.dlptest.com"
        FTP_USER = "dlpuser@dlptest.com"
        FTP_PASS = "SzMf7rTE4pCrf9dV286GuNe4N"
        # connect to the FTP server
        ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
        # force UTF-8 encoding
        ftp.encoding = "utf-8"
        # local file name you want to upload
        filename = "some_file.txt"
        with open(filename, "rb") as file:
            # use FTP's STOR command to upload the file
            ftp.storbinary(f"STOR {filename}", file)
        ftp.dir()


    @property
    def pw(self):
        return self._pw

    def connect_to_ftp_server(self):
        # connect to the FTP server
        ftp_base = FTP(self.host, self.user, self.pw, '')
        # force UTF-8 encoding
        ftp_base.encoding = "utf-8"
        return ftp_base

    def close_conn(self):
        # quit and close the connection
        ftp = self.connect_to_ftp_server()
        ftp.quit()

    def download_files(self):
        FTP_HOST = "ftp.dlptest.com"
        FTP_USER = "dlpuser@dlptest.com"
        FTP_PASS = "SzMf7rTE4pCrf9dV286GuNe4N"
        # connect to the FTP server
        ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
        # force UTF-8 encoding
        ftp.encoding = "utf-8"
        # local file name you want to upload
        filename = "some_file.txt"
        with open(filename, "wb") as file:
             ftp.retrbinary(f"RETR {filename}", file.write)

        # quit and close the connection
        ftp.quit()

if __name__ == "__main__":
    print("dude")
    test_class = FtpParser()
    #test_class.upload_file()
    test_class.download_files()
