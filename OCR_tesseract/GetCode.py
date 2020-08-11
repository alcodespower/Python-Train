import  requests
def GetCode(count):
        url = 'http://jwxt.nytdc.edu.cn/CheckCode.aspx'
        headers = {
                "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Cookie": "ASP.NET_SessionId=31b0qmy2ivrsiy45mje0z4en",
                "Host": "jwxt.nytdc.edu.cn",
                "Pragma": "no-cache",
                "Referer": "http://jwxt.nytdc.edu.cn/",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
        }
        
        response =requests.get(url,headers=headers,verify=False,timeout=5)
        # print(response)
        with open(str(count)+'.jpg','wb') as fw:
                fw.write(response.content)
                print('[Success] You Got ' +str(count) +' CheckCode now! ')
          
        
def Download():
        for i in range(1,16):
                GetCode(i)
Download()

        
