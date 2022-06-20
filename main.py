import threading
import requests
import os
import time, json, datetime

print("\033[0;31m");
print('##############################################\n')
print('\033[0m');
print('[x] Author : SamCOMP')
print('[IG] @mistersm_0')
print('[FB] Syamsul Muarif')
print('[TT] @onlysyw')
print("\033[0;31m");
print('##############################################\n')
print('\033[0m');
print('Silakan pilih YGY input nomor nya :')
print('1. Trophy -MAINTENANCE-')
print('2. Crown')
ronde = input('Input: ')
time.sleep(1)
total_thread = os.cpu_count()
time.sleep(1)
loop = 1
def main():
	auth = open("auth.txt", "r")
	headers = {
	'authorization':auth.read()
	}
	while loop == 1:
		jam = datetime.datetime.now()
		if ronde == '1':
			juara = 2
		else:
			juara = 3
		req = requests.get('http://kitkabackend.eastus.cloudapp.azure.com:5010/round/finishv2/{}'.format(juara), headers=headers)
		response = json.loads(req.text)
		print('[{}-{}-{} {}:{}:{}] Sukses | Thropy: {} |Chrown: {}'.format(jam.year, jam.month, jam.day, jam.hour, jam.minute, jam.second, response['User']['SkillRating'], response['User']['Crowns']))
		time.sleep(0.05)


for i in range(1, total_thread + 1):
    t = threading.Thread(target=main)
    t.start()
