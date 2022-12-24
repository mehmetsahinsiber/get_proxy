from bs4 import BeautifulSoup
import requests
import time
import os
def proxy():
	url = "https://free-proxy-list.net/#"
	os.system("clear")
	r = requests.get(url)
	soup = BeautifulSoup(r.content,"html.parser")
	proxyList = soup.find("textarea", attrs={"class":"form-control"})
	for i in proxyList:
		os.system("clear")
		delete_letters = i[73:]
		delete_space = delete_letters.strip()
		with open("proxies.txt","w",encoding="utf-8") as prx:
			prx.writelines(delete_space)
			
	def second():
		how_much = int(input("after how many seconds to update the proxy: "))
		number = 1
		
		if how_much > 0:
			while number <= how_much:
				time.sleep(1)
				os.system("clear")
				print(number)
				number+= 1
			sayi_gir = how_much

			
			if sayi_gir == how_much:
				proxy()
					
			else:
				print("exiting..")
				time.sleep(0.5)
				os.system("clear")
				exit()
	return second()

if __name__ == "__main__":
	proxy()