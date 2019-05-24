import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("base",BASE_DIR)

MEDIA_ROOT = os.path.join(BASE_DIR,'media\TEXT.mp3')
print("media",MEDIA_ROOT)
print(MEDIA_ROOT,"/text.mp3")