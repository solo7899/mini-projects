from time import sleep
import subprocess
import shlex
import asyncio
import sys

try:
    from desktop_notifier import DesktopNotifier, DEFAULT_SOUND
except ImportError:
     print("install desktop-notifier\n\rpip install desktop-notifier")
     sys.exit()

async def main():
    notifier =DesktopNotifier()
    while True:
        ping = ""
        try:
            ping = subprocess.check_output(shlex.split("ping 8.8.8.8 -n 1 ")).decode()
            print(ping)
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)
        except Exception as e:
                print(f"Error pinging: {e}")
                pass

        if "TTL" in ping:
            await notifier.send("Internet Check", "Internet is working", sound=DEFAULT_SOUND)
            break
        sleep(1)


if __name__ == "__main__":
    asyncio.run(main())