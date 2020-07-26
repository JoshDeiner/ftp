""" python runner for ftp   """
"""
error handling needs to be added
unit testing could be very useful(pytest)
if cant move files directly from servers without downloading in between, need optimization if large scale
can include partition based on block size
"""

import ftplib, pysftp, os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


class FtpMiddleware:
    
    def __str__(self):
        return ("need to validate whether the transfer suceeded")

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def set_access(self):
        # hard coded credentials for webpage ftp
        self.user = "dlpuser@dlptest.com"
        self.password = "SzMf7rTE4pCrf9dV286GuNe4N"
        self.host = "ftp.dlptest.com"

    def set_ftp(self):
        self.set_access()
        # connect to the FTP server
        ftp = ftplib.FTP(self.host, self.user, self.password)
        # force UTF-8 encoding
        ftp.encoding = "utf-8"
        return ftp

    def upload_file(self, filename="some_file.txt"):
        ftp = self.set_ftp()
        # local file name you want to upload
        with open(filename, "rb") as file:
            # use FTP's STOR command to upload the file
            ftp.storbinary(f"STOR {filename}", file)
        ftp.dir()

    def upload_folder(self, directory="testdirectory"):
        ftp = self.set_ftp()
        ftp.mkd(directory)

    def connect_azure(self, file_name):
        '''connect to azure storage account and blob container  '''
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        # may want to hardcode container name or use some form data structure to hold container options
        container_name = "quickstart" + str(uuid.uuid4()) 
        container_client = blob_service_client.create_container(container_name)
        # Write text to the file
        local_path = "./"
        local_file_name = file_name
        upload_file_path = os.path.join(local_path, local_file_name)
        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
        # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)

    def close_conn(self):
        # quit and close the connection
        ftp = self.set_ftp()
        ftp.quit()

    def download_files(self, filename="some_file.txt"):
        ftp = self.set_ftp()
        # local file name you want to download
        with open(filename, "wb") as file:
            ftp.retrbinary(f"RETR {filename}", file.write)

    def init_transfer(self):
        ftp = self.set_ftp()
        # local file name you want to upload
        print(ftp)
        file_names = ['some_file.txt']
        for i, file_name in enumerate(file_names):
             self.download_files(file_name)
             self.connect_azure(file_name)
             print("if succeeds to delete")
             # if you find deleting a file interferes with your work process locally and you are using git
             # you can use git restore
             os.remove(file_name)
             # need to return a status code
             # if succeeds delete file locally in path
        ftp.dir()


if __name__ == "__main__":
    tc = FtpMiddleware()
    print(tc)
    tc.secure_conn()
    #tc.upload_file()
    #tc.download_files()
    #tc.upload_folder()
    #tc.set_access()
    #tc.connect_azure()
    #tc.init_transfer()
    tc.close_conn()
