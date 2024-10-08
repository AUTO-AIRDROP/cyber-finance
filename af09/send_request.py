import requests, json
from fake_useragent import UserAgent

class Api : 
    def __init__(self):
        self.referer='https://g.cyberfin.xyz/'
    
    def header(
            self,
            token,
            Referer=None
        ):
        ua=UserAgent()
        headers = {
            "accept"            : "application/json",
            "accept-language"   : "en-US,en;q=0.9",
            "authorization"     : f"Bearer {token}",
            "content-type"      : "application/json",
            "priority"          : "u=1, i",
            "sec-ch-ua"         : ua.random,          # Use a random fake user-agent
            "sec-ch-ua-mobile"  : "?1",
            "sec-ch-ua-platform": '"android"',        # Optional: Customize the platform as needed
            "sec-fetch-dest"    : "empty",
            "sec-fetch-mode"    : "cors",
            "sec-fetch-site"    : "same-site",
            "Referer"           : f"{Referer or self.referer}",
            "Referrer-Policy"   : "origin"
        }
 
        return headers
    
    def get(self,url,token,data):
        header=self.header(token,Referer=None)
        return requests.get(url, headers=header, json=data)
    
    def post(self,url,token,data):
        header=self.header(token,Referer=None)
        return requests.post(url, headers=header, json=data) 
    
    def put(self,url,token,data):
        header=self.header(token,Referer=None)
      
        return requests.put(url, headers=header, json=data) 
    
    def patch(self,url,token,data):
        header=self.header(token,Referer=None)
        return requests.patch(url, headers=header, json=data) 






        