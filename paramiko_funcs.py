import paramiko, os
import functools
paramiko.util.log_to_file('/tmp/paramiko.log')
from stat import S_ISDIR
host = ""
port = 22
transport = paramiko.Transport((host, port))
password = ""
username = ""
transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)
print(sftp)



def bulk_upload(local_path:str='~/testitpy/data/', target_path:str=''):
    '''  upload all files from local directory '''
    prinit=os.walk(local_path)
    for root, dirs, files in os.walk(local_path, topdown=False):
        for name in files:
            full_path=(os.path.join(root, name))
            try:
                print(full_path)
                sftp.put(full_path, f'/sftpuser_11/test/{name}')
            except Exception as e:
                print(f"{full_path}, error: {e}")
            else:
                print("finished successfully")

def sftp_walk(remotepath):
    path=remotepath
    files=[]
    folders=[]
    for f in sftp.listdir_attr(remotepath):
        if S_ISDIR(f.st_mode):
            folders.append(f.filename)
        else:
            files.append(f.filename)
    if files:
        yield path, files
    for folder in folders:
        new_path=os.path.join(remotepath,folder)
        for x in sftp_walk(new_path):
            yield x

pathr = '/sftpuser_11/test'
local = '~/testitpy/data'
#bulk_upload(local, pathr)
sftp.chdir('path')
data = []


def get_remote_d_docs(local_dir:str='~/testitpy/data/'):
    for filename in sftp.listdir_attr():
        print(filename.filename)
        #    sftp.get(str(filename), str(filename))
        sftp.get(filename.filename, f"{local_dir}{filename.filename}")
