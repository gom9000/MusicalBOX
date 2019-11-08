# ---------------------------------
# GET THE AUDIO DEVICE ID FROM NAME
# ---------------------------------
ii=0
for device in sounddevice.query_devices():
    if AUDIO_DEVICE_NAME in device['name']:
        AUDIO_DEVICE_ID = ii
        break
    ii += 1
# ---------------------------------


