import pysftp
import os

#  file to connect to sftp

# documentation includes many other useful features if need to be added
# https://pysftp.readthedocs.io/en/release_0.2.9/cookbook.html#pysftp-connection-put-r


def validate_input(sftp, action_func, input_data, env):
    """ function to validate if folder/file exists within remote file system  """
    if sftp.isfile(input_data) or sftp.isdir(input_data):
        return 0

def download_file(sftp, file_name="some_file.txt"):
    sftp.get(file_name)

def upload_file(sftp, file_name="some_file.txt"):
    # probably need to check local path
    check_path = os.path.isfile(file_name)
    sftp.put(file_name) if check_path is True else print(
        f"status of file check {check_path== True}"
    )

def upload_directory(sftp, directory="some_folder"):
    # recursively copy files and directories from local static, to remote static,
    # preserving modification times on the files
    # match folder needs to already exist even if empty
    remote_folder = "myfolder"
    sftp.put_r(directory, remote_folder, preserve_mtime=True)


def sftp_conn(func):
    with pysftp.Connection(
        os.getenv("MYHOST"), username=os.getenv("THISUSER"), password=os.getenv("IDEA")
    ) as sftp:
        sftp.chdir("sftpuser/sftp-test")
        # set up base context manager if you will have multiple directories that need to be iterated through
        # with sftp.cd(base_dir):
        logic = validate_input(sftp, func, "some_file.txt", "remote")
        func(sftp) if logic == 0 else print("failure")


def init_safe_transfer(action):
    switch_st = {
        "upload_f": upload_file,
        "download_f": download_file,
        "upload_d": upload_directory,
    }
    func = switch_st[action]
    try:
        sftp_conn(func)
    except:
        print("failed to connect")


if __name__ == "__main__":
    # action = "upload_f"
    action = "download_f"
    init_safe_transfer(action)
