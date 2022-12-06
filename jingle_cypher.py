# Jingle Cypher

from datetime import datetime
import time
import random
import getpass

aurora_strength = 70
naughty_list = 9001
magic_of_christmas = True
turboman_action_figures_left = 1

# This function returns the number of days remaining until midnight of christmas day

def get_days_until_xmas():
	print("[-] Calculating Days Until Xmas")
	xmas = datetime(2022, 12, 25, 0, 0, 0)
	today = datetime.now()
	print ('[-] Today is:', today )
	print ('[-] Christmas day is:', xmas )	
	xmas_countdown = xmas - today
	days_until_xmas = xmas_countdown.total_seconds() / 60 / 60 / 24
	print ('[-] There are', days_until_xmas, 'days until Christmas')
	return int(days_until_xmas)

# This function calculates the reindeer energy level
	
def get_reindeer_energy_level():
	print ('[-] Measuring Reindeer Energy Levels')
	rudolph_heart_rate = random.randint(140, 200)
	reindeer_energy_level = rudolph_heart_rate * random.randint(0, 1)
	return (reindeer_energy_level)
	
def get_xmas_tree_seed():
	print ('[-] Planting a random Xmas Tree Seed')
	time.sleep(3)
	tree_size = naughty_list // aurora_strength
	return (tree_size * turboman_action_figures_left)
	
def get_jingle_prime():
	reindeer_energy_level = get_reindeer_energy_level()
	xmas_tree_seed = get_xmas_tree_seed()
	days_until_xmas = get_days_until_xmas()
	jingle_prime = reindeer_energy_level + xmas_tree_seed + days_until_xmas
	return (jingle_prime)
	print (jingle_prime)


def encrypt_string(a, b):
	clear_text = a
	jingle_prime_key = b
	print ('[-] Encrypting Data')
	time.sleep(3)
	print ('[-] 50% Progress')
	time.sleep(3)
	print ('[-] Encyption Complete')
	encoded = [ord(c) * jingle_prime_key for c in clear_text]
	return (encoded)
	

	
print ('Jingle Cypher Encryption: Copyright Figgle Muffinbow')
print ('========================')
clear_data = getpass.getpass('Enter Text To Encrypt: ')
jingle_prime_key = get_jingle_prime()
encrypted_data = encrypt_string(clear_data, jingle_prime_key)

print ('Jingle Prime Encyption Results')
print ('==============================')
print (encrypted_data)
