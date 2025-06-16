from network import WLAN
import time
import machine
from machine import RTC
import pycom

import binascii

# Devices
devices_list=[{"gw_eui":"b'807d3afffe947cc4'", "tag":"PYGATE01", "no":1, "ap": "RIM-AP"},
              {"gw_eui":"b'840d8efffe1228b4'", "tag":"PYGATE02", "no":2, "ap": "RIM-AP"},
              {"gw_eui":"b'840d8efffe012343'", "tag":"PYGATE03", "no":3, "ap": "RIM-AP"},
              {"gw_eui":"b'840d8efffe1177d0'", "tag":"PYGATE04", "no":4, "ap": "RIM-AP"},
              {"gw_eui":"b'807d3afffe948df4'", "tag":"PYGATE05", "no":5, "ap": "RIM-AP"},
              {"gw_eui":"b'840d8efffeabcdef'", "tag":"PYGATE06", "no":6, "ap": "RIM-AP"},
              {"gw_eui":"b'840d8efffe012347'", "tag":"PYGATE07", "no":7, "ap": "RIM-AP"},
              {"gw_eui":"b'807d3afffe948778'", "tag":"PYGATE08", "no":8, "ap": "RIM-AP"}]
              #{"gw_eui":"b'840d8efffe1185c8'", "tag":"PYGATE06", "no":6, "ap": "RIM-AP"},

# LoRaWAN server. If the Pygate connects to the Wi-Fi network "RIM-AP" (the one
# from devices_list), the IP address of the server is calculated from the
# gateway number (192.168.100.no). Otherwise, FIXEDLORAWANSERVER is used.
#FIXEDLORAWANSERVER = "palas.ugr.es"
FIXEDLORAWANSERVER = "eu1.cloud.thethings.network"

# Ensure pybytes disabled
print('pybytes disabled')
pycom.pybytes_on_boot(False)

# Ensure LTE disabled
print('LTE disabled')
pycom.lte_modem_en_on_boot(False)

print('\nStarting LoRaWAN concentrator')
# Disable Hearbeat
pycom.heartbeat(False)

# Define callback function for Pygate events
def machine_cb (arg):
    evt = machine.events()
    if (evt & machine.PYGATE_START_EVT):
        # Green
        pycom.rgbled(0x103300)
    elif (evt & machine.PYGATE_ERROR_EVT):
        # Red
        pycom.rgbled(0x331000)
    elif (evt & machine.PYGATE_STOP_EVT):
        # RGB off
        pycom.rgbled(0x000000)

# register callback function
machine.callback(trigger = (machine.PYGATE_START_EVT | machine.PYGATE_STOP_EVT | machine.PYGATE_ERROR_EVT), handler=machine_cb)

# Connect to a Wifi Network
wlan = WLAN(mode=WLAN.STA)

GatewayEUI = str(binascii.hexlify(wlan.mac().sta_mac)[:6] + 'fffe' + "abcdef") #binascii.hexlify(wlan.mac().sta_mac)[6:])
#print('Gateway EUI: ' + GatewayEUI)
print('Gateway EUI: ' + GatewayEUI[2:-1])

# Check device tag
deviceTag = "unknown"
deviceNo = 0
deviceAP = "RIM-AP"
gw_eui_list = [device["gw_eui"] for device in devices_list]
if GatewayEUI in gw_eui_list:
    GatewayEUI_index = gw_eui_list.index(GatewayEUI)
    deviceTag = devices_list[GatewayEUI_index]["tag"]
    deviceNo = devices_list[GatewayEUI_index]["no"]
    deviceAP = devices_list[GatewayEUI_index]["ap"]
print('Device tag:  ' + deviceTag + '\n')

# Check for known networks
bFoundKnownNetwork=False
while not bFoundKnownNetwork:
    nets = wlan.scan()
    ssid_list = [net.ssid for net in nets]

    # 1st priority network
    #if 'RIM-AP' in ssid_list:
    selectedSSID=""
    if deviceAP in ssid_list:
        bFoundKnownNetwork=True
        selectedSSID=deviceAP
        print('Found ' + selectedSSID + ' network!')
#        wlan.ifconfig(config=('192.168.100.' + str(100 + deviceNo), '255.255.255.0', '192.168.100.100', '8.8.8.8')) # (ip, subnet_mask, gateway, DNS_server)
        wlan.ifconfig(config=('192.168.100.' + str(100 + deviceNo), '255.255.255.0', '192.168.100.100', '192.168.100.100')) # (ip, subnet_mask, gateway, DNS_server)
        wlan.connect(ssid=deviceAP, auth=(WLAN.WPA2, "wimunet!"))
    # 2nd priority network
    elif 'WIMUNET-LORAWAN' in ssid_list:
        bFoundKnownNetwork=True
        selectedSSID='WIMUNET-LORAWAN'
        print('Found ' + selectedSSID + ' network!')
        wlan.connect(ssid='WIMUNET-LORAWAN', auth=(WLAN.WPA2, "wimunet!"))
    # 3rd priority network
    elif 'HOMENETWORK' in ssid_list:
        selectedSSID='MOVISTAR_0B20'
        bFoundKnownNetwork=True
        print('Found ' + selectedSSID + ' network!')
        wlan.connect(ssid='HOMENETWORK', auth=(WLAN.WPA2, "HOMENETWORK_PASSWORD"))
    # No known network found
    else:
        print('No known network found! Waiting 5 seconds to retry...')
        time.sleep(5)

print('Connecting to WiFi...',  end='')
counter=0
while not wlan.isconnected() and bFoundKnownNetwork:
    counter=counter+1
    print('.', end='')
    time.sleep(1)
    # Trying to connect again after 5 seconds
    if counter%5 == 0:
        if selectedSSID == deviceAP:
            wlan.connect(ssid=deviceAP, auth=(WLAN.WPA2, "wimunet!"))
        elif selectedSSID == 'WIMUNET-LORAWAN':
            wlan.connect(ssid='WIMUNET-LORAWAN', auth=(WLAN.WPA2, "wimunet!"))
        elif selectedSSID == 'HOMENETWORK':
            wlan.connect(ssid='HOMENETWORK', auth=(WLAN.WPA2, "HOMENETWORK_PASSWORD"))

print(" OK")
print("Wi-Fi network configuration: " + str(wlan.ifconfig()) + '\n')

# Sync time via NTP server for GW timestamps on Events
print('Syncing RTC via ntp...', end='')
rtc = RTC()
#rtc.ntp_sync(server="pool.ntp.org")
rtc.ntp_sync(server="162.159.200.1")

while not rtc.synced():
    print('.', end='')
    time.sleep(.5)
print(" OK\n")

# Read the GW config file from Filesystem
with open('/flash/global_conf.json','r') as fp:
    buf = fp.read()

LORAWANSERVER = ''
if selectedSSID == deviceAP:
    LORAWANSERVER = '192.168.100.' + str(deviceNo)
else:
    LORAWANSERVER = FIXEDLORAWANSERVER

buf = buf.replace("LORAWANSERVER", LORAWANSERVER, 1)
buf = buf.replace("GATEWAYEUI", GatewayEUI[2:-1], 1)
print("buf: " + buf)

# Start the Pygate
machine.pygate_init(buf)
# disable degub messages
# machine.pygate_debug_level(1)
