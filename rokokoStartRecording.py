from pip._vendor import requests
#import main

IP_ADDRESS = '192.168.50.55' # Replace with actual ip address
PORT = '14053' # Replace with actual port
API_KEY = '1234' # Replace with actual api key
CLIP_NAME = 'MyNewClip' # Clip Name, Optional
TIME_CODE = '00:01:05:00'
FRAME_RATE = '60'
BACK_TO_LIVE = False # should we enter isolation mode after recording or continue in live mode
SMARTSUIT_NAME = '' # Optional
COUNTDOWN_DELAY = 5 # Optional



responce = None

def start_Recording(IP_ADDRESS):
    try:
        responce = requests.post(f"http://{IP_ADDRESS}:{PORT}/v1/{API_KEY}/recording/start",
            json = {
            'filename': CLIP_NAME,
            'time' : TIME_CODE,
            'frame_rate' : FRAME_RATE,
            'back_to_live' : BACK_TO_LIVE
            }
        )
    except Exception as e:
        print (e)

    if responce is not None:
        print(responce.json())

def stop_Recording(IP_ADDRESS):
    try:
        responce = requests.post(f"http://{IP_ADDRESS}:{PORT}/v1/{API_KEY}/recording/stop",
            json = {
            'filename': CLIP_NAME,
            'time' : TIME_CODE,
            'frame_rate' : FRAME_RATE,
            'back_to_live' : BACK_TO_LIVE
            }
        )
    except Exception as e:
        print (e)

    if responce is not None:
        print(responce.json())

def calibrate_Suit(IP_ADDRESS):
    try:
        responce = requests.post(f"http://{IP_ADDRESS}:{PORT}/v1/{API_KEY}/calibrate",
            json = {
            'device_id': SMARTSUIT_NAME,
            'countdown_delay': COUNTDOWN_DELAY,
            'skip_suit' : False,
            'skip_gloves' : False,
            'use_custom_pose' : False,
            'pose' : 'straight-arms-down' # tpose, straight-arms-down, straight-arms-forward
            }
        )
    except Exception as e:
        print (e)

    if responce is not None:
        print(responce.json())