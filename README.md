# SPfileup

The Python script to backup important files in SharePoint.

# Situation

SharePoint is a reliable storage for documentation. One can need to store Python or text files in SharePoint to make them accessible for the business teams. 

# Approach

I spend some little time to see how we can manage SharePoint access and file management. So here is the Python script I created and worked out for me. 

# Arguments
**folder**: The path of the destination folder e.g., "sites/KOD"

**Username**: Please enter your corporate Microsoft email address

**Password**: Please enter your App password

**Sharepoint_folder**: Please enter the Sharepoint folder to store the files e.g., "Shared Documents/General/Backup {Your Name}"

**dir_ext**: Please address your important files using path and extension info e.g., "C:/Users/YoztyurkA/Projects/*.ppt"

# Attention!
#1 Please make sure that you have create your App password in "https://account.activedirectory.windowsazure.com/AppPasswords.aspx"

#2 Please ensure that you adjusted the custom variables in the script for your personal needs before running the job.

# Author:
Adnan Yoztyurk
