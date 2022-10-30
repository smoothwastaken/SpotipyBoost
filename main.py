import sys
import time
import spotipy
import spotipy.util as util


def exit():
    print("[x] Shutting down the client")
    sys.exit()


def main():
    if len(sys.argv) > 2:
        username = sys.argv[1]
        waiting_time = int(sys.argv[2])
    else:
        print("[-] Whoops, need your username!")
        print("usage: python user_playlists.py <username> <waiting time>")
        exit()

    token = util.prompt_for_user_token(
        username, scope=["app-remote-control", "streaming", "user-read-currently-playing", "user-modify-playback-state", "user-read-playback-state"])

    if token:
        sp = spotipy.Spotify(auth=token)
        timing = 0
        while True:
            current_song = sp.current_playback()
            timing += 1
            if current_song == None:
                if timing < waiting_time:
                    print(
                        f"[!] Waiting {waiting_time - timing} second(s) before starting... (waiting time set to {waiting_time} seconds)")
                else:
                    print("[*] Fetching connected devices...")
                    devices_obj = sp.devices()
                    devices = devices_obj["devices"]
                    if len(devices) == 0:
                        print("[-] There is no available device.")
                    else:
                        print(f"[+] {len(devices)} available device(s):")
                        for device in devices:
                            device_name = device["name"]
                            print(f"  - {device_name}")

                        last_device = devices[-1]
                        last_device_name = last_device["name"]
                        print(f"\n[+] Starting playing on {last_device_name}.")
                        sp.transfer_playback(last_device["id"], True)
            else:
                current_playing_device_name = current_song["device"]["name"]
                current_song_name = current_song["item"]["name"]
                current_song_author = current_song["item"]["artists"][0]["name"]
                print(
                    f"[*] Already listening on {current_playing_device_name}: ", end=" ")
                print(f"{current_song_name} • {current_song_author}")
                timing = 0

            time.sleep(1)

    else:
        print("[-] Can't get token for", username)



if __name__ == "__main__":
    main()
