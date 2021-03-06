from .settings import *

# Update SITE infos to use the common port 80 to publish the webapp
SITE_FIXED = {
    'name': "Gamestation Manager",
    'ip': None, # If 'None' find the ip automatically. Use a string to define another ip/hostname
    'port': None, # If 'None' no port is added to hostname, so the server have to be reachable from port 80
}

# Production path to the Gamestation logs file
GAMESTATION_LOGFILE_PATH = "/root/gamestation.log"

# Use packaged assets
ASSETS_PACKAGED = True
