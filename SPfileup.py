"""SharePoint File Upload

The Python script to backup important files in SharePoint.

Arguments:
    folder: The path of the destination folder e.g., "sites/KOD"
    Username: Please enter your corporate Microsoft email address
    Password: Please enter your App password
    Sharepoint_folder: Please enter the Sharepoint folder to store the files e.g., "Shared Documents/General/Backup {Your Name}"
    dir_ext: Please address your important files using path and extension info e.g., "C:/Users/YoztyurkA/Projects/*.ppt"

Attention!: 
    Please make sure that you have create your App password in "https://account.activedirectory.windowsazure.com/AppPasswords.aspx"

Attention!
    Please ensure that you adjusted the custom variables in the script for your personal needs before running the job.

Note:
    This job is designed to run on your local machine, please make adjustments to run it on a virtual machine if necessary.

Author:
    Adnan Yoztyurk
"""

# Import modules
from shareplum import Office365
from shareplum import Site
from shareplum.site import Version
import os
import glob

# Function to read and copy the content of the files
def file_upload_to_sharepoint(file_name):
    with open(file_name, mode='rb') as file:
        file_content = file.read()
    folder.upload_file(file_content, os.path.basename(file_name))
    print(file_name + " is copied to SharePoint")


def SPfileup(folder, Username, Password, Sharepoint_folder, dir_ext):
    # Logging info
    server_url = "https://ktglbuc.sharepoint.com/"
    site_url = server_url + folder
    # SharePoint Authorization
    authcookie = Office365(server_url, username=Username, password=Password).GetCookies()
    site = Site(site_url, version=Version.v365, authcookie=authcookie)
    folder = site.Folder(Sharepoint_folder)
    # Address your important files using path and extension info
    source_dir = glob.glob(dir_ext, recursive=True)

    # Apply the function to all files
    for files in source_dir:
        file_upload_to_sharepoint(files)

print("The job completed successfully - All files are copied to SharePoint")
# End of the script
