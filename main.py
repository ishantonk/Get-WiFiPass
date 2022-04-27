import subprocess # subprocess module is used to run cmd command.

# store devices profiles data in data.
data =  subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Converting into list and store in variable "profile".
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# itrate every wifi names and passwords.
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')

    results = [b.split(":")[1:-1] for b in results if "Key Content" in b]

    try:
        print (f'{str(i):30}{str(results[0]):}')
        
    except IndexError:
        print(f'{str(i):30}{str(""):}')