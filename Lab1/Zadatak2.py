import socket
import subprocess

# Set the path to the USB image file
image_path = 'C:\\Users\\Mario\\Downloads\\imageFESB'

# Call bitlocker2john to extract the recovery key
bitlocker2john_cmd = f'C:\\Users\\Mario\\Downloads\\john-1.9.0-jumbo-1-win64\\run\\bitlocker2john.exe -i {image_path}'
process = subprocess.Popen(bitlocker2john_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, error = process.communicate()

# Print the extracted recovery key
keys = output.decode().strip().split('\n')
recovery_key = [s for s in keys if "$bitlocker$1$" in s]
print(f'BitLocker recovery key: {recovery_key[0]}')

# Hash je uspjesno izvucen koristenjem bitlocler2john alata!

hashcat_cmd = f'C:\\Users\\Mario\\Downloads\\hashcat-6.2.6\\hashcat.exe -m 22100 -a 3 {recovery_key[0]} "218?d?d?d?d?d"'
process = subprocess.call(hashcat_cmd, shell=True)

cracked_password = subprocess.check_output([hashcat_cmd + " --show"], shell=True).decode()
cracked_password = cracked_password.split(':')[-1]
print(f"Password : {cracked_password}")

# Probijena BitLocker lozinka koristenjem Hashcat alata je: 21854671