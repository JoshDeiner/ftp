import pysftp, os

#  file to connect to sftp

# documentation includes many other useful features if need to be added
# https://pysftp.readthedocs.io/en/release_0.2.9/cookbook.html#pysftp-connection-put-r


def validate_data_avail(sftp, data_obj='some_file.txt', directory='mydirectory'):
    ''' check if data can be operated upon  '''
    if sftp.isfile(data_obj) or os.path.isfile(data_obj):
        return 0
    elif sftp.isdir(directory):
        return 1
    else:
        return 2


def post_actions(sftp):
    print("ending transaction ||| local dir below")
    print(sftp.listdir())

def render_sftp_action(sftp, action, file_name="some_file.txt", directory="myfolder", remote_dir="thisdir"):
        sftp_swtch_commands = {
            "download_f": sftp.get,  # download to local from remote
            "upload_f": sftp.put,  # upload to remote from local
            "ls": sftp.listdir,  # inspect surroundings like ls in unix
            "remove_f": sftp.remove,  # delete file in remote
            "upload_dir": sftp.put_r,  # recursive put dir, logic will need to be amended to change for file vs dir
        }
        # switch statement to return sftp action
        func = sftp_swtch_commands.get(action, "no sftp actions available")
        #validation check and switch statement to return correct action for data type: file vs folder
        validation_result = validate_data_avail(sftp, file_name, directory)
        validation_switch = {0: (file_name), 1: (directory, remote_dir)}
        # initialize sftp action
        func(validation_switch.get(validation_result, "no data provided"))


def sftp_conn(action):
    """ 
connect to sftp server and render correct sftp action depedent on switch statement
directory have been added as defaulted just to show functionality.
they should probably be moved when logic becomes more mature
"""
    with pysftp.Connection(
        os.getenv("MYHOST"),
        username=os.getenv("THISUSER"),
        password=os.getenv("SPASSWORD"),
    ) as sftp:
        sftp.chdir("sftpuser/sftp-test")
        render_sftp_action(sftp, action)
        # list directory upon completion
        post_actions(sftp)


def init_safe_transfer(action):
    try:
        sftp_conn(action)
        print("**** finish transaction ****")
    except:
        print("failed to finish")


if __name__ == "__main__":
    action = "upload_f"
    #action = "download_f"
    init_safe_transfer(action)
