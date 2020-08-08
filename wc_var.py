#-*- coding: utf-8 -*-
from os import getenv

class wcii():
    def __init__(self):
        self.windowswall = getenv('appdata') + "/Microsoft/Windows/Themes/"
        self.windowswall = self.windowswall.replace("\\", "/").replace("\\", "/").replace("\\", "/").replace("\\", "/")

        appfolder = getenv('localappdata') + "/whatclockisit/"
        appfolder = appfolder.replace("\\", "/").replace("\\", "/").replace("\\", "/").replace("\\", "/")

        self.pver = "beta0.7" #베타 버전 체크!
        self.appdata = appfolder

        #date
        self.data = appfolder + "data/"
        self.appclive = self.data + "clive.wcii" #코어 라이브
        self.ckill = self.data + "ckill.wcii" #킬스위치
        self.appcini = self.data + "cini.ini" #코어 설정
        self.appuini = self.data + "uini.ini" #설정 설정
        self.apptt = self.data + "tt.wcii" #다음 텍스트 저장
        self.update = self.data + "update.wcii" #새로운 업데이트 저장

        #temp
        self.temp = appfolder + "temp/"
        self.showtemp = self.temp + "showtemp.png"
        self.preview = self.temp + "preview.png"

        #resource
        self.rs = appfolder + "resource/"
        self.appctt = self.rs + "ctt.ini"  # 커스텀 텍스트 저장
        self.rsimage = self.rs + "rsimage.png"
        self.oriimage = self.rs + "oriimage.png"
        self.rsfontotf = self.rs + "font.otf"
        self.rsfontttf = self.rs + "font.ttf"
        self.refontlicense = self.rs + "font_license.txt"

        #log
        self.log = appfolder + "log/"
        self.errorlog = self.log + "wciierror.log"
        self.wciilog = self.log + "wcii.log"

        #defalt
        self.dsource = "wc_source/"

        #css
        self.pb_f = "QPushButton{font-size: 15px; background-color: rgb(120,120,120); color: rgb(0,0,0)}\nQPushButton:hover{background-color: rgb(255,255,255); color: rgb(0,0,0)}"
        self.pb_t = "QPushButton{font-size: 15px; background-color: rgb(255,255,255); color: rgb(0,0,0)}\nQPushButton:hover{background-color: rgb(255,255,255); color: rgb(0,0,0)}"

