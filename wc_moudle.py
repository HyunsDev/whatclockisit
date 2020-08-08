#-*- coding: utf-8 -*-
import requests, os, wc_var, datetime, ctypes, json, socket, urllib, sys, shutil, psutil, configparser
from platform import *
from urllib.request import urlopen
from os import getenv, path, makedirs
from ctypes import windll
from time import sleep
from win32api import *
from PIL import Image, ImageDraw, ImageFont, ImageFile

#변수 불러오기
wc = wc_var.wcii()

#로그 전송
def goerror(wc_name, email, wc_text, reply):
    #try:
    if True:
        #data = json.loads(urlopen("http://ip.jsontest.com/").read())
        #data = urlopen('http://automation.whatismyip.com/n09230945.asp').read()
        URL = "http://jsgetip.appspot.com/"
        try:
            data = str(urlopen(URL).read())
        except Exception as e:
            errorlog(str(e), appcheck=False)
            return "error"
        data = data.replace("b'function ip(){return\"", "")
        data = data.replace("\"};'", "")
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
        ip = data
        log_dir = wc.appdata + "log/"
        log_list = os.listdir(log_dir)
        log_list.sort()
        ver = wc.pver
        now = datetime.datetime.now()

        errorlogtext = f"==========[ 에러 리포트 ]==========\n" \
                   f"작성 시각 : {now}\n" \
                   f"==========[ 사용자 정보 ]==========\n" \
                   f"아이피 : {ip}\n" \
                   f"이름 : {wc_name}\n" \
                   f"프로그램 버전 : {ver}\n" \
                   f"==========[ 모니터 정보 ]==========\n" \
                   f"모든 모니터 크기 : {sc_allsize()}\n" \
                   f"주 모니터 크기 : {sc_size()}\n" \
                   f"모니터 수 : {sc_num()}\n" \
                   f"==========[ 시스템 정보 ]==========\n" \
                   f"{uname()}\n" \
                   f"==========[ 사용자 작성 ]==========\n" \
                   f"{wc_text}\n" \
                   f"==========[ 답변할 방법 ]==========\n" \
                   f"이름 : {wc_name}\n" \
                   f"답변 방법 : {reply}\n" \
                   f"이메일 : {email}\n" \
                   f"==========[ 로그 ]===========\n"


        for item in log_list:
            with open(log_dir + item) as f:
                error = f.read()
                errorlogtext = errorlogtext + f"[ 로그 이름 : {item}]\n" \
                                      f"{error}\n"

        print(errorlogtext)

        code = "wcii_" + now.strftime("%y%m%d_%H") + now.strftime("%f")[0:2]

        URL = 'http://wcii.dothome.co.kr/goerror/index.php'
        #URL = "http://asdf.asdf"
        try:
            req = requests.post(URL, {'error':errorlogtext, "ver": ver, "code": code})
            print("[ Goerror 응답 ]\n"+str(req))
            return req
        except Exception as e:
            errorlog(str(e), appcheck=False)
            return "error"

#버전 체크
def vercheck(view=True):
    try:
        opener = urllib.request.build_opener()
        # opener.addheaders = [('User-Agent',
        #                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        url = urlopen(f"http://wcii.dothome.co.kr/pver/index.php", timeout=2)
        textdata = url.read()
        t = json.loads(textdata)
        pver = t['ver']

        if pver != wc.pver:
            if view is True:
                with open(wc.update, "w") as f:
                    f.write(pver)
                windll.user32.MessageBoxW(None, f"지금몇시계 업데이트가 있어요\n\n현재 지금몇시계 버전 : {wc.pver}\n지금몇시계 최신버전 : {pver}\n\nhttps://whatclockisit.xyz 에서 업데이트 해주세요!", "지금몇시계 업데이트가 있어요!", 0)
            return pver
        else:
            with open(wc.update, "w") as f:
                f.write("nowest")
            return None

    except Exception as e:
        errorlog("업데이트 체크" + e)
        return False

#앱데이터 체크
def appdata_check(hell=False, window=False):
    try:
        #백업용
        appdata_error = False
        if hell == True:
           if path.isdir(wc.appdata):
                shutil.rmtree(wc.appdata)
                sleep(2)

        if not path.isdir(str(wc.appdata)):
            makedirs(path.join(wc.appdata))
            print("whatclockisit 디렉터리 발견못함, 전체 디렉터리 생성")
            appdata_error = True

        app_folder = ["data", "temp", "resource", "log"]
        for i in app_folder:
            if not path.isdir(str(wc.appdata + i)):
                print(i + "  디렉터리 발견 실패, 디렉터리 생성")
                makedirs(path.join(wc.appdata + i))
                appdata_error = True

        data_file = ["cini.ini", "uini.ini"]
        for i in data_file:
            if not path.isfile(wc.appdata + "data/" + i):
                try:
                    makedirs(path.join(wc.appdata + "data/"))
                except:
                    pass
                shutil.copyfile(wc.dsource + i, wc.appdata + "data/" + i)
                print(i + " 발견실패, 기본으로 대체")
                appdata_error = True

        resource_file = ["ctt.ini", "font.otf", "font_license.txt"]
        for i in resource_file:
            if not path.isfile(wc.appdata + "resource/" + i):
                try:
                    makedirs(path.join(wc.appdata + "resource/"))
                except:
                    pass
                shutil.copyfile(wc.dsource + i, wc.appdata + "resource/" + i)
                print(i + " 발견실패, 기본으로 대체")
                appdata_error = True
        if window:
            windll.user32.MessageBoxW(None, "프로그램 오류로 설정이 초기화 되었어요...\n너무너무 미안해요..\n프로그램을 다시 시작해주세요..", "지금몇시계", 0)
            return True
        elif appdata_error == True:
            return True
        elif appdata_error == False:
            return False
    except PermissionError:
        return "error"

#에러 로그 작성
def errorlog(e, pos="알 수 없음", appcheck=True):
    if appcheck:
        appdata_check()

    if pos == "알 수 없음":
        if __name__ == "wc_core":
            pos = "코어"
        elif __name__ == "wc_setting":
            pos = "설정"
        elif __name__ == "wcii_wallpaper":
            pos = "배경화면 생성 과정"
        else:
            pos = __name__
    now = datetime.datetime.now()
    msg = f"[{pos}] {now.year}/{now.month}/{now.day} {now.hour}:{now.minute}:{now.second} 문제 : {e}\n"
    try:
        with open(wc.errorlog, "a") as f:
            f.write(msg)
    except FileNotFoundError:
        with open(wc.errorlog, "w") as f:
            f.write(msg)

#로그작성
def writelog(log):
    now = datetime.datetime.now()
    msg = f"{now.year}/{now.month}/{now.day} {now.hour}:{now.minute}:{now.second} 내용 : {log}\n"
    try:
        with open(wc.wciilog, "a") as f:
            f.write(msg)
    except FileNotFoundError:
        with open(wc.wciilog, "w") as f:
            f.write(msg)

#오류 창
def errorwindow(e, exit=False):
    errorlog(e)
    mes = f"이런..프로그램에 나쁜 버그가 나타났어요.\n혹시 다시 실행해도 이 화면이 반복된다면\n오류보내기를 하거나\n로그파일들과 함께 디스코드에 올려주세요!\n버그 내용 : {e}\n\n로그위치 : {wc.appdata}log/"
    windll.user32.MessageBoxW(None, mes, "앗..이런..버그나 나타났어요", 0)
    if exit:
        sys.exit(0)

#코어 라이브 테스트
def alreadylive():
    mypid = int(os.getpid())

    if not path.isfile(wc.appclive): #라이브 파일 탐색
        try:
            makedirs(path.join(wc.appdata + "data"))
        except:
            pass
        with open(wc.appclive, "w") as f:
            f.write(mypid)
            return False
    else:
        try:
            with open(wc.appclive, "r") as f:
                pid = f.readline()
                pid = int(pid)
        except Exception as e:
            print(e)
            with open(wc.appclive, "w") as f:
                f.write(str(mypid))
            return False

        if pid != mypid:
            try:
                p = psutil.Process(pid)
                p = p.name()
                if p == "wc_core.exe":
                    return True
                else:
                    print(3)
                    with open(wc.appclive, "w") as f:
                        f.write(str(mypid))
                    return False
            except psutil.NoSuchProcess:
                print(4)
                with open(wc.appclive, "w") as f:
                    f.write(str(mypid))
                return False
        else:
            with open(wc.appclive, "w") as f:
                f.write(str(mypid))
'''
def corelive():
    try:
        with open(wc.appcorelive, "w") as f:
            f.write("r u already live?")
        sleep(0.5)
        with open(wc.appcorelive, "r") as f:
            livedata = f.readline()

        if livedata == "already":
            return True
        else:
            sleep(0.5)
            with open(wc.appcorelive, "r") as f:
                livedata = f.readline()
                if livedata != "already":
                    return False
    except:
        with open(wc.appcorelive, "w") as f:
            f.write("r u already live?")
        sleep(0.5)
        with open(wc.appcorelive, "r") as f:
            livedata = f.readline()

        if livedata == "already":
            return True
        else:
            sleep(0.5)
            with open(wc.appcorelive, "r") as f:
                livedata = f.readline()
                if livedata != "already":
                    return False
''' #구버전 코어라이브

#시간대 문구
def wciitime(time=None):
    if time == None:
        now = datetime.datetime.now()
        nowtime = now.strftime('%H%M')
        nowtime = str(nowtime)
    else:
        nowtime = str(time)

    if nowtime == '0000':
        showtime = "지금은 자정이야"
        return showtime
    elif nowtime == '1200':
        showtime = "지금은 정오야"
        return showtime
    else:
        hour = int(nowtime[0:2])
        if hour == 00:
            hour = 24
        minu = int(nowtime[2:4])
        time_map_hour = {0: "", 1: "한", 2: "두", 3: "세", 4: "네", 5: "다섯", 6: "여섯", 7: "일곱", 8: "여덟", 9: "아홉"}
        time_map_minu = {0: "", 1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}

        # 시간
        if hour >= 21: showhour = "밤 "
        elif hour >= 17: showhour = "저녁 "
        elif hour >= 15: showhour = "오후 "
        elif hour >= 11: showhour = "점심 "
        elif hour >= 7: showhour = "아침 "
        elif hour >= 5: showhour = "이른 아침 "
        elif hour >= 3: showhour = "새벽 "
        elif hour >= 1: showhour = "늦은 밤 "
        elif hour >= 0: showhour = "밤 "

        if hour > 12: hour = hour - 12

        if hour >= 10:
            hour = hour - 10
            showhour = showhour + "열" + time_map_hour[hour] + " 시 "
        else:
            showhour = showhour + time_map_hour[hour] + " 시 "

        # 분 구문
        showminu = ""
        if minu >= 10:
            if minu >= 20:
                minu_ten = int(str(minu)[0])
                showminu = time_map_minu[minu_ten] + "십"
            else:
                showminu = "십"
            minu_one = int(str(minu)[1])
            showminu = showminu + time_map_minu[minu_one] + " 분"
        elif minu > 0:
            minu_one = int(str(minu)[0])
            showminu = showminu + time_map_minu[minu_one] + " 분"
        else:
            showminu = showminu + "정각"

        # 최종 출력 구문
        showtime = showhour + showminu + "이야."
        return showtime

#문구
def wciitext(plushour=0, online=True):
    now = datetime.datetime.now()
    nowdate = now.strftime('%H')
    time_now = int(nowdate) + int(plushour)
    if cinidown("where_text") == "online":
        try:
            if online is True:
                if time_now == 0:
                    time_now = 24
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-Agent', f'Mozilla/5.0 (Whatclockisit {wc.pver}; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.37')]
                urllib.request.install_opener(opener)
                url = urlopen(f"http://wcii.dothome.co.kr/v1/?hour={time_now}", timeout=3)
                textdata = url.read()
                t = json.loads(textdata)
                showtext = t['text']
                return showtext

            else:
                if time_now == 0:
                    time_now = 24
                with open(wc.apptext, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    custext = []
                    for line in lines:
                        try:
                            line = line.replace("\n", "")
                        except:
                            pass
                        custext.append(line)
                time_now == time_now - 1
                showtext = custext[time_now]

        except Exception as e: #오프라인 기본 문구
            print(f"서버연결 오류발생 : {e}")
            errorlog("neterror", e)
            time_now = int(nowdate) + int(plushour)
            if time_now == 0:
                showtext = "좋은 꿈 꿔"
            elif time_now == 1:
                showtext = "헉?! 아직도 안 잤어?"
            elif time_now == 2:
                showtext = "아직 안 자고 뭐해?"
            elif time_now == 3:
                showtext = "음.. 졸리지 않니?"
            elif time_now == 4:
                showtext = "하아암.. 졸립당"
            elif time_now == 5:
                showtext = "지금 쯤이면 해가 뜰려나..?"
            elif time_now == 6:
                showtext = "벌써 새벽이네"
            elif time_now == 7:
                showtext = "상쾌한 아침"
            elif time_now == 8:
                showtext = "오늘은 뭐해?"
            elif time_now == 9:
                showtext = "힘쌔고 강한 아침!"
            elif time_now == 10:
                showtext = "지금은 뭐하시나..?"
            elif time_now == 11:
                showtext = "조금 나른해지네..ㅎㅎ"
            elif time_now == 12:
                showtext = "쩝..배고프당"
            elif time_now == 13:
                showtext = "밥 맛있게 먹었어?"
            elif time_now == 14:
                showtext = "더 열심히!"
            elif time_now == 15:
                showtext = "나른하당..ㅎ"
            elif time_now == 16:
                showtext = "헉 벌써"
            elif time_now == 17:
                showtext = "지금 뭐해?"
            elif time_now == 18:
                showtext = "슬슬 배고파진다 ㅎㅎ"
            elif time_now == 19:
                showtext = "해가 슬슬 지고 있겠네.." #계절마다 달라져야 함
            elif time_now == 20:
                showtext = "저녁 맛있게 먹었어?"
            elif time_now == 21:
                showtext = "벌써"
            elif time_now == 22:
                showtext = "오늘은 별이 보일려나?"
            elif time_now == 23:
                showtext = "슬슬 졸립지 않아?"
            elif time_now == 24:
                showtext = "좋은 꿈 꿔"
        return showtext

    elif cinidown("where_text") == "custom":
        time_now = int(nowdate) + int(plushour)
        customtext = configparser.ConfigParser()
        customtext.read(wc.appctt, encoding="UTF-8")
        customtime = customtext['main']

        return customtime[str(time_now)]

    else:
        time_now = int(nowdate) + int(plushour)
        if time_now == 0:
            showtext = "좋은 꿈 꿔"
        elif time_now == 1:
            showtext = "헉?! 아직도 안 잤어?"
        elif time_now == 2:
            showtext = "아직 안 자고 뭐해?"
        elif time_now == 3:
            showtext = "음.. 졸리지 않니?"
        elif time_now == 4:
            showtext = "하아암.. 졸립당"
        elif time_now == 5:
            showtext = "지금 쯤이면 해가 뜰려나..?"
        elif time_now == 6:
            showtext = "벌써 새벽이네"
        elif time_now == 7:
            showtext = "상쾌한 아침"
        elif time_now == 8:
            showtext = "오늘은 뭐해?"
        elif time_now == 9:
            showtext = "힘쌔고 강한 아침!"
        elif time_now == 10:
            showtext = "지금은 뭐하시나..?"
        elif time_now == 11:
            showtext = "조금 나른해지네..ㅎㅎ"
        elif time_now == 12:
            showtext = "쩝..배고프당"
        elif time_now == 13:
            showtext = "밥 맛있게 먹었어?"
        elif time_now == 14:
            showtext = "더 열심히!"
        elif time_now == 15:
            showtext = "나른하당..ㅎ"
        elif time_now == 16:
            showtext = "헉 벌써"
        elif time_now == 17:
            showtext = "지금 뭐해?"
        elif time_now == 18:
            showtext = "슬슬 배고파진다 ㅎㅎ"
        elif time_now == 19:
            showtext = "해가 슬슬 지고 있겠네.."  # 계절마다 달라져야 함
        elif time_now == 20:
            showtext = "저녁 맛있게 먹었어?"
        elif time_now == 21:
            showtext = "벌써"
        elif time_now == 22:
            showtext = "오늘은 별이 보일려나?"
        elif time_now == 23:
            showtext = "슬슬 졸립지 않아?"
        elif time_now == 24:
            showtext = "좋은 꿈 꿔"
        return showtext

#프로그램 업데이트 확인
def vercheck(view=True):
    try:
        url = urlopen(f"http://wcii.dothome.co.kr/pver/index.php", timeout=2)
        textdata = url.read()
        t = json.loads(textdata)
        pver = t['ver']

        if pver != wc.pver:
            if view is True:
                with open(wc.update, "w") as f:
                    f.write(pver)
                windll.user32.MessageBoxW(None, f"지금몇시계 업데이트가 있어요\n\n현재 지금몇시계 버전 : {wc.pver}\n지금몇시계 최신버전 : {pver}\n\nhttps://whatclockisit.xyz 에서 업데이트 해주세요!", "지금몇시계 업데이트가 있어요!", 0)
            return pver
        else:
            with open(wc.update, "w") as f:
                f.write("nowest")
            print("프로그램 최신 버전")
            return None

    except Exception as e:
        errorlog("업데이트 체크" + str(e))
        return False

#모든 모니터 크기
def sc_allsize():
    wc_mon = EnumDisplayMonitors()
    wc_len = len(wc_mon)
    re = []
    for i in range(0, wc_len):
        a = wc_mon[i][2]
        re.append(a)
    return re

#주 모니터 크기
def sc_size():
    sc = (GetSystemMetrics(0), GetSystemMetrics(1))
    return sc

#모니터 숫자
def sc_num():
    wc_mon = EnumDisplayMonitors()
    wc_len = len(wc_mon)
    return wc_len

#배경 이미지 리사이즈
def resizeimage():
    wc_wall = Image.new("RGB", sc_size(), "white")
    oriimage = Image.open(wc.oriimage)

    wall_ratio_xy = oriimage.size[0] / oriimage.size[1]
    wall_ratio_yx = oriimage.size[1] / oriimage.size[0]
    min_x = oriimage.size[0] / sc_size()[0]
    min_y = oriimage.size[1] / sc_size()[1]

    if min_x > min_y:
        log_1 = "세로 기준 조정"
        resize_x = int(sc_size()[1] * wall_ratio_xy)
        resize_y = sc_size()[1]
        resized = oriimage.resize((resize_x, resize_y))
        pan = int(int(int(sc_size()[0]) - sc_size()[1] * wall_ratio_xy) / 2)
        wc_wall.paste(im=resized, box=(pan, 0))
    else:
        log_1 = "가로 기준 조정"
        resize_x = sc_size()[0]
        resize_y = int(sc_size()[0] * wall_ratio_yx)
        resized = oriimage.resize((resize_x, resize_y))
        pan = int(int(int(sc_size()[1]) - sc_size()[0] * wall_ratio_yx) / 2)
        wc_wall.paste(im=resized, box=(0, pan))
    #print(f"배경 이미지 제작, 기존 이미지 : {str(oriimage.size)}({str(wall_ratio_xy)}), 화면 크기 : {str(sc_size())}, {log_1}(여백 : {str(pan)}), 원본/화면 비 : ({str(min_x)},{str(min_y)})")
    writelog(f"배경 이미지 제작, 기존 이미지 : {str(oriimage.size)}({str(wall_ratio_xy)}), 화면 크기 : {str(sc_size())}, {log_1}(여백 : {str(pan)}), 원본/화면 비 : ({str(min_x)},{str(min_y)})")
    wc_wall.save(wc.rsimage)

#단색 이미지 제작
def solidimage(rgb=True):
    if rgb:
        rgb = eval(cinidown("wall_color"))
        print(rgb)
    wc_wall = Image.new("RGB", sc_size(), rgb)
    wc_wall.save(wc.rsimage)

#ini파일 동기화 (설정 -> 코어)
def updataini():
    shutil.copyfile(wc.appuini, wc.appcini)
    print("업데이트 완료")

#ini파일 초기화 (코어 -> 설정)
def undoini():
    shutil.copyfile(wc.appcini, wc.appuini)

#설정 ini 수정
def uiniup(ini_key, ini_value):
    configsetting = configparser.ConfigParser()
    configsetting.read(wc.appuini)
    datasetting = configsetting['main']

    datasetting[ini_key] = ini_value
    with open(wc.appuini, 'w') as main:
        configsetting.write(main)

#설정 ini 불러오기
def uinidown(ini_key):
    configsetting = configparser.ConfigParser()
    configsetting.read(wc.appuini)
    datasetting = configsetting['main']

    return datasetting[ini_key]

#코어 ini 수정
def ciniup(ini_key, ini_value):
    configcore = configparser.ConfigParser()
    configcore.read(wc.appcini)
    datacore = configcore['main']

    datacore[ini_key] = ini_value
    with open(wc.appcini, 'w') as main:
        configcore.write(main)

#코어 ini 불러오기
def cinidown(ini_key):
    configcore = configparser.ConfigParser()
    configcore.read(wc.appcini)
    datacore = configcore['main']
    return datacore[ini_key]

#텍스트 데이터 불러오기
def loadtext():
    try:
        with open(wc.apptt, "r") as f:
            textdata = f.readline()
    except:
        updatetext()
        with open(wc.apptt, "r") as f:
            textdata = f.readline()
    return textdata

#커스텀 데이터 불러오기:
def tinidown(ini_key):
    customtext = configparser.ConfigParser()
    customtext.read(wc.appctt, encoding="UTF-8")
    customtime = customtext['main']
    return customtime[str(ini_key)]

#커스텀 데이터 수정
def tiniup(ini_key, ini_value):
    ini_key = str(ini_key)
    customtext = configparser.ConfigParser()
    customtext.read(wc.appctt, encoding="UTF-8")
    customtime = customtext['main']

    customtime[ini_key] = ini_value
    with open(wc.appctt, 'w', encoding="UTF-8") as main:
        customtext.write(main)

#텍스트 데이터 업데이트
def updatetext(hour=0):
    wc_textdata = str(wciitext(hour))
    with open(wc.apptt, "w") as f:
        f.write(wc_textdata)
    return wc_textdata

#메인 화면 제작
def wcii_wallpaper(previewmode=False, wciitext=None):
    nowtime = wciitime()
    if previewmode == True:
        config = configparser.ConfigParser()
        config.read(wc.appuini)
        data = config['main']
        print(f"[ 프리뷰 로드 ] ({nowtime})")
    else:
        config = configparser.ConfigParser()
        config.read(wc.appcini)
        data = config['main']
        print(f"[ 새로고침 ] ({nowtime})")

    if wciitext == None:
        nowtext = loadtext()
    else:
        nowtext = wciitext


    fsize = int(data['font_size'])
    screen_w = sc_size()[0]
    screen_h = sc_size()[1]

    plus_x = 0
    plus_y = 0

    if data['clock_pos'] == "left":
        plus_x = (screen_w / 4) * -1
    elif data['clock_pos'] == "right":
        plus_x = screen_w / 4
    elif data['clock_pos'] == "self":
        plus_x = int(data['clock_x'])
        plus_y = int(data['clock_y'])

    textfill = eval(data['font_color'])

    textalign = data['font_align']
    try:
        try:
            imagepath = Image.open(wc.rsimage)
        except:
            solidimage()
            imagepath = Image.open(wc.rsimage)
        imagepath.LOAD_TRUNCATED_IMAGES = True
    except:
        appdata_check()
        try:
            imagepath = Image.open(wc.rsimage)
        except:
            resizeimage()
            imagepath = Image.open(wc.rsimage)
        imagepath.LOAD_TRUNCATED_IMAGES = True

    msg = str(nowtext) + "\n" + str(nowtime)
    try:
        font = ImageFont.truetype(path.join(wc.rs, "font.otf"), fsize)
    except:
        font = ImageFont.truetype(path.join(wc.rs, "font.ttf"), fsize)
    draw = ImageDraw.Draw(imagepath)
    w, h = draw.textsize(msg, font=font)
    draw.text(((screen_w - w) / 2 + plus_x, (screen_h - h) / 2 - 50 + plus_y), msg, fill=textfill, font=font, align=textalign)
    if previewmode == True:
        imagepath.save(wc.preview)
    else:
        imagepath.save(wc.showtemp)
        imagepath = path.normpath(wc.showtemp)
        windll.user32.SystemParametersInfoW(20, 0, imagepath, 0)

    sleep(0.2)

#정지 화면
def stop_wallpaper():
    windll.user32.SystemParametersInfoW(20, 0, wc.rsimage, 0)

def testing():
    custom_where = []
    for i in range(24):
        custom_where.append("time_" + str(i))

    print(custom_where)

if __name__ == '__main__':
    print("wc_moudle 테스트 모드")
    work = input("명령을 입력하세요 : ")
    print("=================[ 함수 출력 부분 ]==================")
    output = eval(work)
    print("===================[ 결과 부분 ]=====================")
    print(f"출력값 : {output}[{type(output)}]")



