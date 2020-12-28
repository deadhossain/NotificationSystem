from datetime import datetime
now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
file_name = datetime.now().strftime("%d-%m-%Y")
floder_name = datetime.now().strftime("%B_%Y")
print(file_name)
print(floder_name)