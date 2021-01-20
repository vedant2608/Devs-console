import os
from datetime import *
import sys
import subprocess
import pyttsx3
import pyfiglet
import screen_brightness_control as sbc
engine = pyttsx3.init()
engine.setProperty('rate', 190)


def run(cmd):
    completed = subprocess.run(["powershell", "-Command", f"{cmd} 2>$logs.exe"], capture_output=True)
    return completed


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


class command_list():
    def __init__(self, command):
        self.command = command

    def execution(self):
        # Sleep commands
        sleep_commands = list()
        with open("commands\\sleep_commands.exe", "r") as command:
            tmp_lst = [i.split("\n")[0] for i in command.readlines()]
            for i in tmp_lst:
                sleep_commands.append(i)
        # Self introduction
        introduction_commands = list()
        with open("commands\\introduction_commands.exe", "r") as command:
            tmp_lst = [i.split("\n")[0] for i in command.readlines()]
            for i in tmp_lst:
                introduction_commands.append(i)
        # greeting command
        greeting_commands = list()
        with open("commands\\greeting_commands.exe", "r") as command:
            tmp_lst = [i.split("\n")[0] for i in command.readlines()]
            for i in tmp_lst:
                greeting_commands.append(i)
        # Date-asking command
        date_commands = []
        with open("commands\\date_commands.exe", "r") as command:
            tmp_lst = [i.split("\n")[0] for i in command.readlines()]
            for i in tmp_lst:
                date_commands.append(i)
        # Open for camera
        camera_commands = []
        with open("commands\\camera_commands.exe", "r") as command:
            tmp_lst = [i.split("\n")[0] for i in command.readlines()]
            for i in tmp_lst:
                camera_commands.append(i)
        # Open the browsers
        browsers_command = []
        with open("commands\\browsers_command.exe", "r") as command:
            tmp_lst = [i.split("\n")[0] for i in command.readlines()]
            for i in tmp_lst:
                browsers_command.append(i)
        # Opening notepad
        open_file_commands = []
        with open("commands\\file_opening_commands.exe", "r") as command:
            tmp_lst = [i.split("\n")[0] for i in command.readlines()]
            for i in tmp_lst:
                open_file_commands.append(i)
        # To show list of connected wifi devices
        connected_wifi_commands = []
        with open("commands\\connected_wifi_commands.exe", "r") as command:
            tmp_lst = [i.split("\n")[0] for i in command.readlines()]
            for i in tmp_lst:
                connected_wifi_commands.append(i)
        # To show the password of connected and selected wifi
        password_of_connected = []
        with open("commands\\connected_wifi_passwords_command.exe", "r") as command:
            tmp_lst = [i.split("\n")[0] for i in command.readlines()]
            for i in tmp_lst:
                password_of_connected.append(i)
        # To generate battery report
        battery_report = []
        with open("commands\\battery_report_commands.exe", "r") as command:
            tmp_lst = [i.split("\n")[0] for i in command.readlines()]
            for i in tmp_lst:
                battery_report.append(i)
        #For changing brightness
        brightness=[]
        with open("commands\\brightness_commands.exe","r") as command:
            tmp_lst=[i.split("\n")[0] for i in command.readlines()]
            for i in tmp_lst:
                brightness.append(i)
        # Checking user interfaces or command execution
        # sleep command
        if self.command in sleep_commands:
            return 'exit'
        # introduction command
        if self.command in introduction_commands:
            return 'introduction'
        # greeting command
        if self.command in greeting_commands:
            return 'greeted'
        # date command
        if self.command in date_commands:
            return 'todays_date'
        # open camera
        if self.command in camera_commands:
            return 'opened camera'
        # browsers command
        if self.command in browsers_command:
            return "opening browser"
        # notepad command
        if self.command in open_file_commands:
            return 'opening file'
        # connected_wifi_commands
        if self.command in connected_wifi_commands:
            return 'listof_connected_wifi'
        # Password_connected_wifi_command
        if self.command in password_of_connected:
            return 'connected_wifi_passwords'
        # Battery report
        if self.command in battery_report:
            return 'generated_battery_report'
        # Help command
        if self.command == 'help-dev':
            return 'helping'
        #brightness command
        if self.command in brightness:
            return 'bright'
        # LAST SCRIPT
        else:
            system_command_code = run(self.command)
            if system_command_code.returncode == 0:
                subprocess.call(f"powershell -command {self.command} 2>$logs.exe", shell=True)
                return "sys_command_executed"
            else:
                while True:
                    choice = input("Is this a new keyword you want to add for specific task[y/n]:")
                    if choice == 'y':
                        print('''
Please Enter category number from for commands. 
The categories are-:
1.To exit the console
2.To introduce dev to yourself
3.To greet dev
4.To ask for today's date
5.To open the camera
6.To open specific website in browser
7.To open notepad
8.To show list of previsiously connected network
9.To show password of previsiously connected network
10.To generate battery report
11.To alter brightness''')
                        category = input("Enter choice number:")
                        if category == '1':
                            sleep_coordinator = open("commands\\sleep_commands.exe", "a+")
                            sleep_coordinator.write(self.command + "\n")
                            sleep_coordinator.close()
                            speak(
                                f"OK I will remember this and You can now use {self.command} command for terminating dev")
                            engine.runAndWait()
                            return 'exit'
                        elif category == '2':
                            introduction_coordinator = open("commands\\introduction_commands.exe", "a+")
                            introduction_coordinator.write(self.command + "\n")
                            introduction_coordinator.close()
                            speak(
                                f"Ok I will remember this and You can now use {self.command} command for introducing dev to yourself")

                            return 'introduction'
                        elif category == '3':
                            greet_coordinator = open("commands\\greeting_commands.exe", "a+")
                            greet_coordinator.write(self.command + "\n")
                            greet_coordinator.close()
                            speak(f"Ok I will remember this ,You can now use {self.command} command for greeting dev")
                            return 'greeted'
                        elif category == '4':
                            date_coordinator = open("commands\\date_commands.exe", "a+")
                            date_coordinator.write(self.command + "\n")
                            date_coordinator.close()
                            speak(
                                f"Ok I will remember this ,You can now use {self.command} command for greeting time from dev")
                            return 'todays_date'
                        elif category == '5':
                            camera_coordinator = open("commands\\camera_commands.exe", "a+")
                            camera_coordinator.write(self.command + "\n")
                            camera_coordinator.close()
                            speak(
                                f"Ok I will remember this ,You can now use {self.command} command to open your camera")
                            return 'opened camera'
                        elif category == '6':
                            broswer_coordinator = open("commands\\browsers_command.exe", "a+")
                            broswer_coordinator.write(self.command + "\n")
                            broswer_coordinator.close()
                            speak(
                                f"Ok I will remember this ,You can now use {self.command} command to open your broswer")
                            return 'opening browser'
                        elif category == '7':
                            notepad_coordinator = open("commands/file_opening_commands.exe", "a+")
                            notepad_coordinator.write(self.command + "\n")
                            notepad_coordinator.close()
                            speak(
                                f"Ok I will remember this ,You can now use {self.command} command to open files")
                            return 'opening file'
                        elif category == '8':
                            network_coordinator = open("commands\\connected_wifi_commands.exe", "a+")
                            network_coordinator.write(self.command + "\n")
                            network_coordinator.close()
                            speak(
                                f"Ok I will remember this ,You can now use {self.command} command to Show the list of connected wifi networks")
                            return 'listof_connected_wifi'
                        elif category == '9':
                            password_coordinator = open("commands\\connected_wifi_passwords_command.exe", "a+")
                            password_coordinator.write(self.command + "\n")
                            password_coordinator.close()
                            speak(
                                f"Ok I will remember this ,You can now use {self.command} command to Show the password of selected wifi networks")
                            return "connected_wifi_passwords"
                        elif category == '10':
                            report_coordinator = open("commands\\battery_report_commands.exe", "a+")
                            report_coordinator.write(self.command + "\n")
                            report_coordinator.close()
                            speak(f"Ok I will remember this, You can now use {self.command} to generate battery report")
                            return "generated_battery_report"
                        elif category=='11':
                            battery_coordinator=open("commands\\brightness_commands.exe","a+")
                            battery_coordinator.write(self.command+"\n")
                            battery_coordinator.close()
                            speak(f"Ok I will remember this, You can now use {self.command} to alter brightness")
                            return 'bright'
                    elif choice == 'n':
                        return "sys_command_not_executed"
                    else:
                        continue


# Untill we get exit command or ctrl+c keyboard interript
try:
    while True:
        try:
            instruction = input("<<DEV>>")
            command = command_list(instruction)
            output = command.execution()
            # exit check
            if 'exit' == output:
                confirm = input("Terminate DEV's console[y/n]:")
                if confirm.lower() == 'y':
                    speak("Thank you for using DEV's console")
                    hour = datetime.now().hour
                    if hour >= 6 and hour < 12:
                        try:
                            speak("Have a good day Buddy")
                        except:
                            break
                    elif hour >= 12 and hour <= 18:
                        try:
                            speak("Have a good noon Buddy")
                        except:
                            break
                    elif hour > 18:
                        try:
                            speak("Good night Buddy")
                        except:
                            break
                    break
            elif output == 'introduction':  # introduction check
                print(pyfiglet.figlet_format("D E V"))
                print('I am DEV. A Console made with python for all windows user')
            elif output == "sys_command_not_executed":  # INVALID system commands check
                print("Sounds like entered system command in wrong way")
            elif output == 'greeted':  # greeting commands check
                print("Hi Buddy")
            elif output == 'todays_date':  # date command check
                tdy_date = date.today()
                print(f"Today's date in yyyy-mm-dd format is {tdy_date}")
            elif output == 'opened camera':  # Camera command check
                run("start microsoft.windows.camera:")
            elif output == "opening browser":  # Open browsers with choice
                print("With which browser you want to open your website")
                print("1.Microsoft Edge")
                print("2.Google Chrome")
                print("3.Firefox")
                print("4.Internet Explorer")
                browser_choice = int(input("Enter your choice number:"))
                url_choice = input("Enter your url with perfect link:")
                # Microsoft edge
                if browser_choice == 1:
                    if url_choice.startswith('https:\\') or url_choice.startswith('http:\\'):
                        completed = subprocess.run(["powershell", "-Command",
                                                    f'''[system.Diagnostics.Process]::Start('msedge','{url_choice}')'''],
                                                   capture_output=True)
                    else:
                        completed = subprocess.run(["powershell", "-Command",
                                                    f'''[system.Diagnostics.Process]::Start('msedge','https:\\{url_choice}')'''],
                                                   capture_output=True)

                # Google chrome
                if browser_choice == 2:
                    if url_choice.startswith('https:\\') or url_choice.startswith('http:\\'):
                        completed = subprocess.run(["powershell", "-Command",
                                                    f'''[system.Diagnostics.Process]::Start('chrome','{url_choice}')'''],
                                                   capture_output=True)
                    else:
                        completed = subprocess.run(["powershell", "-Command",
                                                    f'''[system.Diagnostics.Process]::Start('chrome','https:\\{url_choice}')'''],
                                                   capture_output=True)

                # Firefox
                if browser_choice == 3:
                    if url_choice.startswith('https:\\') or url_choice.startswith('http:\\'):
                        completed = subprocess.run(["powershell", "-Command",
                                                    f'''[system.Diagnostics.Process]::Start('firefox','{url_choice}')'''],
                                                   capture_output=True)
                    else:
                        completed = subprocess.run(["powershell", "-Command",
                                                    f'''[system.Diagnostics.Process]::Start('firefox','https:\\{url_choice}')'''],
                                                   capture_output=True)
                # Internet Explorer
                if browser_choice == 4:
                    if url_choice.startswith('https:\\') or url_choice.startswith('http:\\'):
                        completed = subprocess.run(["powershell", "-Command",
                                                    f'''[system.Diagnostics.Process]::Start('iexplore','{url_choice}')'''],
                                                   capture_output=True)
                    else:
                        completed = subprocess.run(["powershell", "-Command",
                                                    f'''[system.Diagnostics.Process]::Start('iexplore','https:\\{url_choice}')'''],
                                                   capture_output=True)
            elif output == 'opening file':  # open files with notepad
                choice = input("Do you want to open a note with specific file_name[y/n]:")
                if choice == 'y':
                    path = input("Enter the path[Leave blank if file is in Dev's console location]:")
                    file_name = input("Enter the file name with extension also [e.g=> myfile.txt]:")
                    if len(path) == 0:
                        path = "..\\"
                    complete_path = path + "\\" + file_name
                    run(f'''notepad {complete_path}''')
                elif choice == 'n':
                    run('notepad')
            elif output == 'listof_connected_wifi':  # To show list of all connected wifi
                subprocess.run("netsh wlan show profiles", capture_output=False)
            elif output == 'connected_wifi_passwords':  # To show the password of selected conneced wifi

                print("Here is the list of connected wifi")
                subprocess.run("netsh wlan show profiles", capture_output=False)
                network_name = input('''
Enter the wifi name which is in user profiles [Enter any name which is infront of /"All users profile :/"].
Enter the name of your wifi: ''').strip()
                try:
                    print("Password is =>", subprocess.check_output(
                        ["netsh", "wlan", "show", "profiles", network_name, "key=clear"]).decode().replace('\r',
                                                                                                           " ").split(
                        "\n")[32].split(':')[1].strip())
                except subprocess.CalledProcessError as cpe:
                    print("Password is =>", subprocess.check_output(
                        ['netsh', 'wlan', 'show', 'profiles', f'"{network_name}"', 'key=clear']).decode().replace('\r',
                                                                                                                  " ").split(
                        "\n")[32].split(':')[1].strip())
                except Exception:
                    print("Password is =>", subprocess.check_output(
                        [f'netsh wlan show profiles {network_name} key=clear']).decode().replace('\r', " ").split(
                        "\n")[32].split(':')[1].strip())
            elif output == "generated_battery_report":  # To generate battery report

                flag = os.path.isfile("battery-report.html")
                if (flag == True):
                    speak("Opening the battery report file")
                    run("start battery-report.html")
                else:
                    speak("Generating Battery report")
                    run("powercfg /batteryreport")
                    run("start battery-report.html")

            elif output=='helping':
                print("Do read the readme file from the repository to get the help")
                speak("I am dev console , Which has the functionality to execute system commands in kind of human language. Currently I can execute only few tasks ,but with the help of contributors ,I will be able to execute more soon! Execute any system command or type hello here to get DEV in action!")
            elif output=='bright':
                current_brightness = sbc.get_brightness()
                if 40<current_brightness[0]<=60: speak("Curent brightness is okay! Want to alter it?")
                elif current_brightness[0]>=80: speak("Brightness is too much! Want to alter it?")
                elif current_brightness[0]<=30:speak("Brightness is too low! Want to alter it?")
                decision=input("Alter Brightness[y/n]:")
                if(decision=='y'):
                    battery_percentage=input("Enter the brightness percentage. It will increased or decreased according to percenatge:")
                    if battery_percentage.endswith("%"):
                        battery_percentage=battery_percentage.replace("%"," ")
                    sbc.set_brightness(int(battery_percentage))
                else:
                    pass
        except subprocess.CalledProcessError as e:
            speak("Dev can not work over this command!")
        except KeyboardInterrupt as e:
            confirm = input("Terminate DEV's console[y/n]:")
            if confirm.lower() == 'y':
                engine.say("Roger that!")
                hour = datetime.now().hour
                if hour >= 6 and hour < 12:
                    try:
                        speak("Have a good day buddy")
                        sys.exit(0)
                    except:
                        break
                elif hour >= 12 and hour < 18:
                    try:
                        speak("Have a good noon buddy")
                        sys.exit(0)
                    except:
                        break
                elif hour > 18:
                    try:
                        speak("Good night buddy! Sweet dreams")
                        sys.exit(0)
                    except:
                        break
except subprocess.CalledProcessError as e:
            speak("Dev can not work over this command!")
except KeyboardInterrupt as e:  # If pressed ctrl+c
    confirm = input("Terminate DEV's console[y/n]:")
    if confirm.lower() == 'y':
        engine.say("Roger that!")
        hour = datetime.now().hour
        if hour >= 6 and hour < 12:
            try:
                speak("Have a good day buddy")
                sys.exit(0)
            except:
                pass
        elif hour >= 12 and hour < 18:
            try:
                speak("Have a good noon buddy")
                sys.exit(0)
            except:
                pass
        elif hour > 18:
            try:
                speak("Good night buddy! Sweet dreams")
                sys.exit(0)
            except:
                pass
