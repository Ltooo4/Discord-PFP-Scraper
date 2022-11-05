import requests, json, time, os
from tools import *


class Scraper:

    def __init__(self):
        os.system("cls || clear")
        print(logo)
        print("\r\n\r\n\r\n\r\n")
        self.title = "Scraper 1.0 | Made by lto#0207"
        self.token = json.load(open('config.json','r',encoding='utf-8'))['token']
        self.channelId = input(f"{Colors.blue}Channel ID {Colors.purple}>{Colors.white} ")
        self.xsup = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1MTYzOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
        if not self.token:
            log(f"Token Not Found. {Colors.red}|{Colors.white} Put it in {Colors.blue}config{Colors.white}.{Colors.blue}json{Colors.white}")
            time.sleep(2)
            quit()
        else:
            r = requests.get("https://discordapp.com/api/v6/users/@me", headers={'Authorization': self.token})
            if int(str(r.status_code)[:1]) == 2:
                log(f"Logged Into Token. ")
            else:
                log(f"Token Not Valid. {Colors.red}|{Colors.white} Put it in {Colors.blue}config{Colors.white}.{Colors.blue}json{Colors.white}")
                time.sleep(2)
                quit()
        self.proxies = open('proxies.txt','r').readlines()
        if self.proxies:
            log(f"[{len(self.proxies)}] Proxies Found. ")
            self.title += " | Proxies: " + str(len(self.proxies))
            title(self.title)
        else:
            log(f"No Proxies. {Colors.red}|{Colors.white} Put some in {Colors.blue}proxies{Colors.white}.{Colors.blue}txt{Colors.white}")
            time.sleep(2)
            quit()
        
        while True:
            try:
                self.scrape()
            except Exception as e:
                log(str(e).capitalize() + ".")

    def scrape(self):
        headers = {
            'accept': '*/*',
            'authorization': self.token,
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-super-properties': self.xsup,
        }
        r = requests.get(f'https://discord.com/api/v9/channels/{self.channelId}/messages', headers=headers, params={"limit": 100})
        for message in r.json():
            uname = message['author']['username']
            uid = message['author']['id']
            upfp = message['author']['avatar']
            r = requests.get(url=f'https://cdn.discordapp.com/avatars/{uid}/{upfp}.jpg?size=512',stream=True)
            if not os.path.exists("avatars\\%s.png" % uid) and r.content:
                f = open("avatars\\%s.png" % uid, "wb").write(r.content)
                log(f"[{Colors.green}+{Colors.white}] Saved the pfp of {Colors.purple}{uname}{Colors.white} ({Colors.green}{uid}{Colors.white})")
                title(self.title + " | Saved PFPs: " + str(len(os.listdir("avatars\\"))))

if __name__ == "__main__":
    Scraper()