''' python runner for ftp   '''

import ftplibdd
FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser@dlptest.com"
FTP_PASS = "SzMf7rTE4pCrf9dV286GuNe4N"

class FtpParser:
  def __init__(self):
    self._host = "host"
    self.user = "name"
    self.pw = "imp" 

  def connect_to_ftp_server(self):
      # connect to the FTP server
      ftp_base = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
      # force UTF-8 encoding
      ftp_base.encoding = "utf-8"
      return ftp_base

  def upload_file(self):
      # local file name you want to upload
      ftp = self.connect_to_ftp_server()
      filename = "some_file.txt"
      #reading the local file in binary mode
      with open(filename, "rb") as file:
         # use FTP's STOR command to upload the file
         ftp.storbinary(f"STOR {filename}", file)
      ftp.dir()
      self.close_conn()

  def close_conn(self):
     # quit and close the connection
     ftp = self.connect_to_ftp_server()
     ftp.quit()

  def download_files(self):
     # the name of file you want to download from the FTP server
     ftp = self.connect_to_ftp_server()
     filename = "some_file.txt"
     with open(filename, "wb") as file:
       # use FTP's RETR command to download the file
       ftp.retrbinary(f"RETR {filename}", file.write)

if __name__ == '__main__':
  print('dude')
