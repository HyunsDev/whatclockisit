#-*- coding: utf-8 -*-
from wc_moudle import *
from time import sleep  # sleep
import datetime  # 현재 시간 모듈
import sys, wc_var


def wcii_core():
    try:
        try:
            appdata_check()
            wc = wc_var.wcii()
            last_e = ""
            #라이트 테스트
            if alreadylive():
                writelog("코어 중복 실행이 감지됬습니다. 코어를 종료합니다.")
                sys.exit(1)
            with open(wc.ckill, "w") as f:
                f.write("")
        except Exception as e:
            errorlog("<c_00> " + str(e))

        # 메인 코드
        try:
            errorcount = 0 #에러 누적
            updatetext()
            writelog("코어 실행")
            wcii_wallpaper()
            while True:  # 반복
                try:
                    # 메인 코드 시작
                    try:
                        with open(wc.ckill, "r") as f:
                            killdata = f.readline()
                    except:
                        with open(wc.ckill, "w") as f:
                            f.write("")

                    now = datetime.datetime.now()
                    if killdata == "kill":
                        stop_wallpaper()
                        with open(wc.ckill, "w") as f:
                            f.write("dead")
                        writelog("코어가 정상적으로 종료됨")
                        break

                    else:
                        try:
                            nowmin = now.strftime('%M')  # 30분마다 문구 불러오기
                            if nowmin == '59':
                                if now.strftime('%S') == "05":
                                    updatetext(1)
                                elif now.strftime('%S') == "35":
                                    updatetext(1)

                            elif nowmin == '29':
                                if now.strftime('%S') == "05":
                                    updatetext()
                                elif now.strftime('%S') == "35":
                                    updatetext()

                            if now.strftime('%S') == "00":  # 실행
                                if alreadylive():
                                    writelog("코어가 이미 실행된 상태이므로 종료합니다.")
                                    sys.exit(1)
                                wcii_wallpaper()
                                sleep(0.35)

                        except Exception as e:
                            errorlog("<c_01> " + str(e))
                    sleep(0.4)

                # 메인 코드 끝

                #오류 제어 1단 : 실행 가능
                except Exception as e:
                    if e == last_e:
                        errorcount = errorcount + 1
                    else:
                        last_e = e
                    if errorcount <= 10:
                        errorlog("c_02 : " + str(e))
                        errorcount = errorcount + 1
                        if errorcount == 5:
                            appdata_check()
                        pass

                    else: #오류 제어 2단 : 1단이 10회 이상 반복
                        errorwindow(e)
                        errorlog("c_03" + str(e))
                        appdata_check(hell=True)
                        pass

        #오류 제어 3단 : 더 큰 범위에서 에러 발생
        except Exception as e:
            errorwindow(e)
            errorlog("<c_04> " + str(e))
            appdata_check(hell=True)

    #오류 제어 4단 : 1,2,3단에서 제어하지 못한 에러
    except Exception as e:
        errorlog("<c_05> " + str(e))
        errorwindow(e)
        appdata_check(hell=True)

if __name__ == '__main__':
    wcii_core()
