from pypresence import Presence
import time, json, os, sys, psutil, win32gui, win32process, re

# Load in config
me = os.path.dirname(os.path.abspath(__file__))     
try:
    config = json.load(open(me + "/config.json", "r"))
    print("Successfully loaded config.json")
    print("\n\nConfig file reads:\n" + str(config))
except Exception as e:
    print("config.json does not exist.")
    print("Error\n" + str(e))

# Check if a process is running or not, parameter is the name of the process, will be used to check in CDisplayEx is running
def isProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

# Get the window handles based on PID
def getWindowHandle(pid):
  def callback (hwnd, hwnds):
    if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
      _, found_pid = win32process.GetWindowThreadProcessId (hwnd)
      if found_pid == pid:
        hwnds.append (hwnd)
    return True  
  hwnds = []
  win32gui.EnumWindows (callback, hwnds)
  return hwnds

# Get CDisplayEx PID
def findProcessIdByName(processName):
    listOfProcessObjects = []
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=["pid", "name", "create_time"])
           if processName.lower() in pinfo["name"].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return listOfProcessObjects
def getCdisplayID():
    cdisplayPidInfo = findProcessIdByName("CDisplayEX")
    for cdisplayPID in cdisplayPidInfo:
        return cdisplayPID["pid"]

# Get window tile of CDisplayEX from PID using get_hwnds_for_pid()
def getManga():
    if isProcessRunning("Cdisplayex"):
        for hwnd in getWindowHandle(getCdisplayID()):
            title = str(win32gui.GetWindowText(hwnd))
            if title.lower() == "cdisplayex" or title == None:
                return "Idling"
            if "+" in title.lower(): # When reading in double page mode, only show first page to make it look neater
                title = title.split("+", 1)[0]
                title = title.replace("[", " ", 1)
            title = re.sub(r'\.(jpg|jpeg|png|webp)', "", title, flags=re.IGNORECASE) # Remove image file extensions
            title = title[:125] + (title[125:] and "...") # Discord RPC can"t have more then 128 characters so we cut off at 50 and add three dots
            return title
    else:
        print("No CDisplayEx process is running")
        return "CDisplayEX is not running"

# Discord Rich Presence
clientID = config["clientID"]
RPC = Presence(clientID)
RPC.connect()

startTime = time.time()

def main():
    while True:
        while isProcessRunning("Cdisplayex"):
            try:
                RPC.update(
                        large_image=config["images"]["largeImage"], 
                        large_text=config["hoverText"]["largeImageText"], 
                        small_image=config["images"]["smallImage"], 
                        small_text=config["hoverText"]["smallImageText"], 
                        state=getManga(), 
                        details="Reading a manga", 
                        buttons=config["buttons"], 
                        start=startTime
                        )
                time.sleep(15)
            except Exception as e:
                print(e)
                break
        else:
            if not findProcessIdByName("cdisplayex"):
                print("Cannot find CDisplayEx...")
                time.sleep(int(config["time"]["closeTime"]))
                while not isProcessRunning("Cdisplayex"):
                    print("No connection...\nCDisplayExx will close")
                    RPC.close()
                    sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)