import urllib.request as req
import bs4 #pip install beautifulsoup4
import re
import time
def getData(t_url):
    log = open("ppt_log.txt","w",encoding="utf-8")     #開啟一個檔案，沒有就新建一個#a
    # if __name__=='__main__':
    #     fw = open("/exercise1/data/query_deal.txt", 'w') #將要輸出保存的文件地址
    # for line in open("/exercise1/data/query.txt"): #讀取的文件
    #     fw.write("\"poiName\":\"" + line.rstrip("\n") + "\"") # 將字符串寫入文件中
    # # line.rstrip("\n")為去除行尾換行符
    # fw.write("\n") # 換行

    #建立一個Requsest 物件，附加Request Headers 的資訊
    request=req.Request(t_url, headers={
        "cookie":"nwtc=61343e9f262b47.39849336; AB_18=A; AB_28=A; AB_29=B; AB_34=A; AB_full=18-A_28-A_29-B_34-A; cdb_nc_open_datetime=2021-09-05 11:50:55; px1fq=1; adulturl=/viewthread.php?tid=30121483&extra=page%3D1&tr_h=197697717661343a73dcf785_85346503; __auc=9390862317bb41496f7b5567f34; __asc=9390862317bb41496f7b5567f34; adultagreed152=1630813857; viewthread_history=30121483|30121483; dfp_seg_ids=[]; cdb_oldtopics=D30121483D; cdb_fid93=1630813831; cdb_sid=OJfDfT; cdb_fb_referer=/viewthread.php?tid=30121483&extra=page%3D1&tr_h=197697717661343a73dcf785_85346503; curr_hostname=www.discuss.com.hk; up_c=1630813856; _cc_id=f28b685a92049571f6d7b62c95b05d37; panoramaId=1e076d8cac99fa08c3be66e9fb2e4945a7026eb6cf1fb8090cd1079c76e7d6dc; _ga=GA1.3.1782067158.1630813856; _gid=GA1.3.675066675.1630813856; _dc_gtm_UA-4077994-2=1; cdb_cookietime=63072000; cdb_auth=yz1sEN7ksfjoDGKbI0xz6JXwT4o1LDm8CWbsNIptZy2nkiJwdGIwJAncC9yW5x4LGCSh9TwWt1KheeTx+2B65+epA28iwD50tuNR29tZG/d2Ig; cdb_logmode=x; cdb_backurl=x; lotame_domain_check=discuss.com.hk; cdb_lastrequest=W6AHOIveqvrnlQJbqe0/dslI; nwu=810700; ui_uid_up=1jzq+nm7gc9fiBEDQkgaag==; panoramaId_expiry=1631418674313",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")#儲存到data
        
    #print(data)
    #解析HTML,取得每篇文卓的標題

    root=bs4.BeautifulSoup(data,"html.parser")#BeautifulSoup解析HTML格式文件
    #print(root.title)
    # print(root.title.string)
    # print("拍拍手!")
    titles=root.find_all("span",class_="tsubject" , id=True)
    last=root.find_all("em")
    cite=root.select("tbody>tr>td.author>cite>a")
    #print(type(cite))
    #cite = root.select('.main')
    #titles = root.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
    #print(last)
    # realtitle=titles.find_all()
    #titles=root.find("tbody")
    #print(titles)
    #print(root.titles.a.string)
    titles_list = []
    last_list = []
    last_list_str = []
    last_re_name = []
    cite_list = []

    for cite2 in cite:
        #if titles.id != None :#如果標題包含A標籤(沒有被刪除)印出來
            cite_list.append(cite2.text)
    #print(cite_list)
    cite_list2=cite_list[3:]
    for titles2 in titles:
    #   if last.span != None :#如果標題包含A標籤(沒有被刪除)印出來
            #if titles2.a != None :#如果標題包含A標籤(沒有被刪除)印出來
                #print(titles2.a.string)
                titles_list.append(titles2.a.string)
                
    for last2 in last:
        if last2.span != None :#如果標題包含A標籤(沒有被刪除)印出來
            #if last2.a != None :#如果標題包含A標籤(沒有被刪除)印出來
                #print(last2.a.string)
                last_list_str.append(last2.a.string)
                last_list.append(last2.a)
                
                
    h_list = []
    for t2 in last_list:
        t3 = t2.get('href')
        h_list.append(t3)

    last_list_str = [w.replace("\xa0", "") for w in last_list_str]#字串替代
    #print(len(h_list))
    #print(len(titles_list))
    #new = zip(titles_list,h_list)
    #print(list(new))
    #stu = zip(titles_list,last_list_str)
    #print(last_list_str)
    #print(list(stu))
    #origin = zip(*new)
    #print(list(origin))
    #print(titles)
    #print(titles)
    # nextlink=root.find("a", string="››")
    # print(nextlink["href"])
    # print(len(titles_list))
    # print(len(last_list))
    # print((titles_list))
    # print("---------------------")
    def getData(url):
        #建立一個Requsest 物件，附加Request Headers 的資訊
        request=req.Request(url, headers={
            "cookie":"nwtc=61343e9f262b47.39849336; AB_18=A; AB_28=A; AB_29=B; AB_34=A; AB_full=18-A_28-A_29-B_34-A; cdb_nc_open_datetime=2021-09-05 11:50:55; px1fq=1; adulturl=/viewthread.php?tid=30121483&extra=page%3D1&tr_h=197697717661343a73dcf785_85346503; __auc=9390862317bb41496f7b5567f34; __asc=9390862317bb41496f7b5567f34; adultagreed152=1630813857; viewthread_history=30121483|30121483; dfp_seg_ids=[]; cdb_oldtopics=D30121483D; cdb_fid93=1630813831; cdb_sid=OJfDfT; cdb_fb_referer=/viewthread.php?tid=30121483&extra=page%3D1&tr_h=197697717661343a73dcf785_85346503; curr_hostname=www.discuss.com.hk; up_c=1630813856; _cc_id=f28b685a92049571f6d7b62c95b05d37; panoramaId=1e076d8cac99fa08c3be66e9fb2e4945a7026eb6cf1fb8090cd1079c76e7d6dc; _ga=GA1.3.1782067158.1630813856; _gid=GA1.3.675066675.1630813856; _dc_gtm_UA-4077994-2=1; cdb_cookietime=63072000; cdb_auth=yz1sEN7ksfjoDGKbI0xz6JXwT4o1LDm8CWbsNIptZy2nkiJwdGIwJAncC9yW5x4LGCSh9TwWt1KheeTx+2B65+epA28iwD50tuNR29tZG/d2Ig; cdb_logmode=x; cdb_backurl=x; lotame_domain_check=discuss.com.hk; cdb_lastrequest=W6AHOIveqvrnlQJbqe0/dslI; nwu=810700; ui_uid_up=1jzq+nm7gc9fiBEDQkgaag==; panoramaId_expiry=1631418674313",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        })
        with req.urlopen(request) as response:
            data=response.read().decode("utf-8")#儲存到data
            
        #print(data)
        # fileOb = open('data2.html','w',encoding='utf-8')     #開啟一個檔案，沒有就新建一個
        # fileOb.write(data)
        # fileOb.close()
        #解析HTML,取得每篇文卓的標題
        root=bs4.BeautifulSoup(data,"html.parser")#BeautifulSoup解析HTML格式文件
        #print(root.title)
        # print(root.title.string)
        #titles = root.find(class_="^postorig")
        titles=root.find_all("span", id=re.compile(r"postorig"))#_all會返回一個列表
        names =root.find_all("a", target="_blank", class_="name")
        boss = root.find_all("div", {"class":"post-date"})
        au_titles = root.find_all("p",class_="authortitle")
        #titles2 = titles.find_parents("span")
        #titles=root.find(id = "postorig")
        #titles = root.select("span", id = True)
        #titles = root.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
        boss_list = []
        au_titles_list = []
        last_re = []
        for boss in boss:
            boss_list.append(boss.text)
        
        for au_titles2 in au_titles:
            #   if last.span != None :#如果標題包含A標籤(沒有被刪除)印出來
            #if titles2.a != None :#如果標題包含A標籤(沒有被刪除)印出來
                #print(titles2.a.string)
                au_titles_list.append(au_titles2.text)
        #print(au_titles_list)
        #print(last_re)
        boss_list = [r.replace(" ", "") for r in boss_list]
        boss_list = [r.replace("\n", " ") for r in boss_list]
        boss_list = [r.replace("\xa0", " ") for r in boss_list]
        boss_list = [r.replace("樓主", "⚡️⚡️樓主⚡️⚡️") for r in boss_list]
        boss_list = [r.replace("#1 ", "#1 ⚡️⚡️樓主⚡️⚡️") for r in boss_list]
        au_titles_list = [r.replace("\n", "") for r in au_titles_list]
        au_titles_list = [r.replace("\r", "") for r in au_titles_list]
        #print(au_titles_list)
        #print(last_re)
        #last_list_str = [w.replace("\xa0", "") for w in last_list_str]#字串替代
        #print(boss_list)
        # realtitle=titles.find_all()
        #titles=root.find("tbody")
        #print(titles)
        #print(root.titles.a.string)
        for titles in titles:
            #print(titles.text)
            last_re.append(titles.text)
        last_re = [r.replace("\r\n", "") for r in last_re]
        last_re = [r.replace("\r", "") for r in last_re]
        last_re = [r.replace("\n", "") for r in last_re]
        last_re = [r.replace("引用:原帖由 ", "[") for r in last_re]
        last_re = [r.replace("於", "") for r in last_re]
        last_re = [r.replace("發表", "]") for r in last_re]
        #print(last_re)
        # #     if titles.id != None :#如果標題包含A標籤(沒有被刪除)印出來
        for names in names:
            #if titles.a != None:
                #print(names.text)
                last_re_name.append(names.text)

        for x, y, z, j in zip(last_re_name, last_re, boss_list, au_titles_list):
            print("")
            print("-",x,z)
            print(y)
            #log.write("--------------------------------------------------------------------------------------------------------------------------------")
            log.write("🆔"+str(x)+"💨"+str(j))
            log.write("\n")
            log.write(str(z)+"💬"+str(y))
            log.write("\n")
            log.write("--------------------------------------------------------------------------------------------------------------------------------")
            log.write("\n")

        last_re_name.clear()
        last_re.clear()
        #     print(names.text)
        # for names in names:
        # #     # #     if titles.id != None :#如果標題包含A標籤(沒有被刪除)印出來
        #     print(names.text)
        #print(titles)
        #print(titles)
        # nextlink=root.find("a", string="››")
        # return nextlink["href"]
        #print("下一頁:",nextlink["href"])

    #抓取一個頁面的標題

    # count=0
    # while count<1:#抓取頁數
    #     print("-----第",count+1,"頁-----")
    #     Pageurl="https://www.discuss.com.hk/"+getData(Pageurl)
    #     count+=1
    #print(Pageurl)

    # print(last_list)
    #print(last_list2.get('href'))
    # for last_list in last_list.find_all('a', href=True):
    #     print "Found the URL:", a['href']
    titles_list = [r.replace(" ", "") for r in titles_list]
    for x, y, z,j  in zip(titles_list, last_list_str, h_list, cite_list2):
        print("----------------------------------------------------------------")
        print("------",x,y,"------")
        print("----------------------------------------------------------------")
        log.write("❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
        log.write("\n")
        log.write("✖️✖️✖️✖️✖️["+str(x)+"]✖️✖️✖️✖️✖️ 🆔["+str(j)+"] - 📡["+str(y)+"]")
        log.write("\n")
        log.write("❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
        log.write("\n")
        log.write("--------------------------------------------------------------------------------------------------------------------------------")
        log.write("\n")

        #print("時間:",y)
        getData("https://www.discuss.com.hk/"+z)
        #print("----------------------------------------------------------------")
        
    #print(last_re_name)
    log.close()
    nextlink=root.find("a", string="››")
    return nextlink["href"]


    # log.write("time cost"+str(time_c)+"s")
    # log.write("\n")
    # log.write("time cost"+str(time_c)+"s")
    # log.write("time cost"+str(time_c)+"s")

time_start = time.time()
Paget_url="https://www.discuss.com.hk/forumdisplay.php?fid=46"
count=0
while count<3:#抓取頁數
    print("-Page:",count+1)
    Paget_url="https://www.discuss.com.hk/"+getData(Paget_url)
    count+=1
#print(Paget_url)
time_end = time.time()
time_c= time_end - time_start   #運行所花時間
print("Time cost", time_c, "s")