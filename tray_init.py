import subprocess as sb
commands=['export QT_DEVICE_PIXEL_RATIO=0','export QT_AUTO_SCREEN_SCALE_FACTOR=1','export QT_SCREEN_SCALE_FACTORS=1','export QT_SCALE_FACTOR=1','python3 tray.py']
for i in commands:
	k=sb.run([i],shell=True)