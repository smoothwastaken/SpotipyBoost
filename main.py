import os
import sys
import time
import spotipy
import spotipy.util as util
from dotenv import load_dotenv
from termcolor import colored, cprint


def exit(exit_message="") -> None:
    if exit_message:
        cprint("[!]", 'yellow', attrs=['bold'], end=" ")
        print(f'{exit_message}')
    cprint("[x]", 'red', attrs=['bold'], end=" ")
    print("Shutting down the client")
    sys.exit()


def main():
    # Defining variables
    username = ""
    waiting_time = -1

    # Loading environment variables (spotify app credentials)
    load_dotenv()

    if not username or waiting_time == -1:
        # Verifying if the user provided arguments directly with the command
        if len(sys.argv) > 2:
            username = sys.argv[1]
            waiting_time = int(sys.argv[2])

        # Asking the settings values
        else:
            os.system("clear")
            cprint("[?]", 'green', attrs=['bold'], end=" ")
            username = str(input("Your Spotify username: "))
            try:
                cprint("[?]", 'green', attrs=['bold'], end=" ")
                waiting_time = int(
                    input("Enter the waiting time before start playing: "))
            except:
                exit(f"Invalid waiting time entered. Try again with a correct value.")

    # If no username or waiting time provided aborting...
    if not username or waiting_time == -1:
        exit(exit_message="You didn't provide correct infos.")

    # Generate the token for the user
    token = util.prompt_for_user_token(
        username, scope=["app-remote-control", "streaming", "user-read-currently-playing", "user-modify-playback-state", "user-read-playback-state"])

    # If the token is fetch, launching the listening
    if token:
        sp = spotipy.Spotify(auth=token)
        timing = 0
        while True:
            current_song = sp.current_playback()
            timing += 1
            if current_song == None or current_song["item"] == None:
                if timing < waiting_time:
                    cprint("[!]", 'yellow', attrs=['bold'], end=" ")
                    print(
                        f"Waiting {waiting_time - timing} second(s) before starting... (waiting time set to {waiting_time} seconds)")
                else:
                    cprint("[*]", 'blue', attrs=['bold'], end=" ")
                    print("Fetching connected devices...")
                    devices_obj = sp.devices()
                    devices = devices_obj["devices"]
                    if len(devices) == 0:
                        cprint("[-]", 'red', attrs=['bold'], end=" ")
                        print("There is no available device.")
                    else:
                        cprint("[+]", 'green', attrs=['bold'], end=" ")
                        print(f"{len(devices)} available device(s):")
                        for device in devices:
                            device_name = device["name"]
                            print(f"  - {device_name}")

                        last_device = devices[-1]
                        last_device_name = last_device["name"]
                        cprint("\n[+]", 'green', attrs=['bold'], end=" ")
                        print(f"Starting playing on {last_device_name}.")
                        if current_song != None and current_song['item'] == None:
                            sp.start_playback(
                                device_id=last_device['id'], context_uri='https://open.spotify.com/album/0JMZmkRaNLaGUWayBrHOMa?si=5ZBiuYAHRSeLbbZCFB4ZDQ')
                            sp.shuffle(state=True, device_id=last_device['id'])
                            sp.next_track(device_id=last_device['id'])
                        else:
                            sp.transfer_playback(last_device["id"], True)
            else:
                os.system('clear')
                current_playing_device_name = current_song["device"]["name"]
                current_song_name = current_song["item"]["name"]
                current_song_author = current_song["item"]["artists"][0]["name"]
                cprint("[*]", 'blue', attrs=['bold'], end=" ")
                print(
                    f"Already listening on {current_playing_device_name}: ", end=" ")
                print(f"{current_song_name} • {current_song_author}")
                timing = 0

            time.sleep(1)

    else:
        cprint("[-]", 'red', attrs=['bold'], end=" ")
        print("Can't get token for", username)


if __name__ == "__main__":
    main()
