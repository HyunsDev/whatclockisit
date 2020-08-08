# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import randint
from wc_moudle import *
import wc_var
from ctypes import windll
import sys, os
import shutil

appdata_check()
undoini()
wc = wc_var.wcii()

try:
    class Ui_Form(QWidget):
        def setupUi(self, Form):
            try:
                writelog("설정 실행")
                Form.setObjectName("Form")
                Form.setFixedSize(QSize(1050, 600))
                sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
                Form.setSizePolicy(sizePolicy)
                Form.setMinimumSize(QSize(1050, 600))

                self.how_reply_address = "discord"

                if alreadylive():
                    self.already = True
                else:
                    self.already = False

                icon = QIcon()
                icon.addPixmap(QPixmap("wc_source/ui/wcii_icon.png"), QIcon.Normal, QIcon.Off)
                Form.setWindowIcon(icon)
                Form.setStyleSheet("background-color: rgb(17, 17, 17);\n"             
                                   "font-size: 9pt;"
                                   "font-family: Noto Sans CJK KR Black;\n"
                                   "border: 0px; \n")

                Form.setWindowFilePath("")
                self.select_bar = QWidget(Form)
                self.select_bar.setGeometry(QRect(0, 0, 281, 601))
                self.select_bar.setAutoFillBackground(False)
                self.select_bar.setStyleSheet("background-color: rgb(27, 27, 27);\ncolor: rgb(255, 255, 255);\nQPushButton#pushButton:hover{\ncolor: rgb(255,255,255)\n};")
                self.select_bar.setObjectName("select_bar")

                self.main_icon = QLabel(self.select_bar)
                self.main_icon.setGeometry(QRect(20, 20, 61, 61))
                self.main_icon.setStyleSheet("image: url(wc_source/ui/wcii_icon.png);")
                self.main_icon.setText("")
                self.main_icon.setObjectName("main_icon")

                self.main_name = QLabel(self.select_bar)
                self.main_name.setGeometry(QRect(100, 30, 161, 41))
                self.main_name.setStyleSheet("font: 87 9pt Noto Sans CJK KR Black';")
                self.main_name.setObjectName("main_name")

                self.wcii_button = QPushButton(self.select_bar)
                self.wcii_button.setGeometry(QRect(70, 160, 91, 21))
                self.wcii_button.setCursor(QCursor(Qt.ArrowCursor))
                self.wcii_button.setStyleSheet("font-size: 17px;")
                self.wcii_button.setObjectName("wcii_button")
                self.wcii_button.clicked.connect(self.move_tab_wcii)

                self.gear1_icon = QLabel(self.select_bar)
                self.gear1_icon.setGeometry(QRect(20, 150, 51, 41))
                self.gear1_icon.setStyleSheet("image: url(wc_source/ui//Gear_1_icon.png);")
                self.gear1_icon.setText("")
                self.gear1_icon.setObjectName("gear1_icon")

                self.gear2_icon = QLabel(self.select_bar)
                self.gear2_icon.setGeometry(QRect(20, 220, 51, 41))
                self.gear2_icon.setStyleSheet("image: url(wc_source/ui//Gear_2_icon.png);")
                self.gear2_icon.setText("")
                self.gear2_icon.setObjectName("gear2_icon")

                self.clock_setting_button = QPushButton(self.select_bar)
                self.clock_setting_button.setGeometry(QRect(70, 230, 81, 21))
                self.clock_setting_button.setCursor(QCursor(Qt.ArrowCursor))
                self.clock_setting_button.setContextMenuPolicy(Qt.PreventContextMenu)
                self.clock_setting_button.setStyleSheet("QPushButton{font-size: 17px; color: rgb(120,120,120)}\nQPushButton:hover{color: rgb(255,255,255)}")
                self.clock_setting_button.setObjectName("clock_setting_button")
                self.clock_setting_button.clicked.connect(self.move_tab_clock)

                self.gear3_icon = QLabel(self.select_bar)
                self.gear3_icon.setGeometry(QRect(20, 290, 51, 41))
                self.gear3_icon.setStyleSheet("image: url(wc_source/ui/Gear_3_icon.png);")
                self.gear3_icon.setText("")
                self.gear3_icon.setObjectName("gear3_icon")

                self.text_setting_button = QPushButton(self.select_bar)
                self.text_setting_button.setGeometry(QRect(70, 300, 81, 21))
                self.text_setting_button.setCursor(QCursor(Qt.ArrowCursor))
                self.text_setting_button.setContextMenuPolicy(Qt.PreventContextMenu)
                self.text_setting_button.setStyleSheet("QPushButton{font-size: 17px; color: rgb(120,120,120)}\nQPushButton:hover{color: rgb(255,255,255)}")
                self.text_setting_button.setObjectName("text_setting_button")
                self.text_setting_button.clicked.connect(self.move_tab_text)

                self.clock_info_icon = QLabel(self.select_bar)
                self.clock_info_icon.setGeometry(QRect(20, 360, 51, 51))
                self.clock_info_icon.setStyleSheet("image: url(wc_source/ui/info_icon.png);")
                self.clock_info_icon.setText("")
                self.clock_info_icon.setObjectName("clock_info_icon")

                self.clock_info_button = QPushButton(self.select_bar)
                self.clock_info_button.setGeometry(QRect(70, 370, 81, 21))
                self.clock_info_button.setCursor(QCursor(Qt.ArrowCursor))
                self.clock_info_button.setContextMenuPolicy(Qt.PreventContextMenu)
                self.clock_info_button.setStyleSheet("QPushButton{font-size: 17px; color: rgb(120,120,120)}\nQPushButton:hover{color: rgb(255,255,255)}")
                self.clock_info_button.setObjectName("clock_info_button")
                self.clock_info_button.clicked.connect(self.move_tab_info)

                self.moon_icon = QLabel(self.select_bar)
                self.moon_icon.setGeometry(QRect(20, 530, 51, 41))
                self.moon_icon.setStyleSheet("image: url(wc_source/ui/exit_icon.png);")
                self.moon_icon.setText("")
                self.moon_icon.setObjectName("moon_icon")

                self.redbutton = QPushButton(self.select_bar)
                self.redbutton.setGeometry(QRect(60, 540, 141, 21))
                self.redbutton.setCursor(QCursor(Qt.ArrowCursor))
                self.redbutton.setContextMenuPolicy(Qt.PreventContextMenu)
                self.redbutton.setStyleSheet("QPushButton{font-size: 17px; color: rgb(120,120,120)}\nQPushButton:hover{color: rgb(255,255,255)}")
                self.redbutton.setObjectName("redbutton")

                if self.already:
                    self.redbutton.setText("지금몇시계 종료")
                    self.redbutton.clicked.connect(self.killwcii)
                else:
                    self.redbutton.setText("지금몇시계 실행")
                    self.redbutton.clicked.connect(self.core_wakeup)

                self.stacked_widget = QStackedWidget(Form)
                self.stacked_widget.setEnabled(True)
                self.stacked_widget.setGeometry(QRect(280, -30, 771, 621))
                self.stacked_widget.setAutoFillBackground(False)
                self.stacked_widget.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font-size: 15px;")
                self.stacked_widget.setFrameShape(QFrame.NoFrame)
                self.stacked_widget.setFrameShadow(QFrame.Plain)
                self.stacked_widget.setObjectName("stacked_widget")

                ############[ 지금몇시계 ] 페이지 ##############

                self.main_page = QWidget()
                self.main_page.setObjectName("main_page")

                self.main_wcii_title = QLabel(self.main_page)
                self.main_wcii_title.setGeometry(QRect(10, 180, 741, 151))
                self.main_wcii_title.setStyleSheet("")
                self.main_wcii_title.setFrameShape(QFrame.NoFrame)
                self.main_wcii_title.setAlignment(Qt.AlignCenter)
                self.main_wcii_title.setObjectName("main_wcii_title")
                if self.already:
                    self.main_wcii_title.setText("<span style=\" font-size:24pt;\">너는 지금 지금몇시계를 사용중이야</span>")
                else:
                    self.main_wcii_title.setText("<span style=\" font-size:24pt;\">너는 지금 지금몇시계를<br/>사용하지 않고 있어</span>")

                self.main_wcii_info = QPushButton(self.main_page)
                self.main_wcii_info.setGeometry(QRect(310, 450, 151, 41))
                self.main_wcii_info.setObjectName("main_wcii_info")
                self.main_wcii_info.setStyleSheet(wc.pb_f)

                if self.already:
                    self.main_wcii_info.setText("지금몇시계 잠재우기")
                    self.main_wcii_info.clicked.connect(self.killwcii)
                else:
                    self.main_wcii_info.setText("지금몇시계 잠 깨우기")
                    self.main_wcii_info.clicked.connect(self.core_wakeup)

                self.stacked_widget.addWidget(self.main_page)

                ############ [시계 설정] 페이지 ##############

                self.clock_setting_page = QWidget()
                self.clock_setting_page.setObjectName("clock_setting_page")

                #시계 위치
                self.c_pos_label = QLabel(self.clock_setting_page)
                self.c_pos_label.setGeometry(QRect(70, 80, 81, 21))
                self.c_pos_label.setObjectName("c_pos_label")

                self.c_pos_left = QPushButton(self.clock_setting_page)
                self.c_pos_left.setGeometry(QRect(220, 80, 111, 23))
                self.c_pos_left.setStyleSheet(wc.pb_f)
                self.c_pos_left.setObjectName("c_pos_left")
                self.c_pos_left.clicked.connect(self.c_p_set_left)

                self.c_pos_center = QPushButton(self.clock_setting_page)
                self.c_pos_center.setGeometry(QRect(340, 80, 111, 23))
                self.c_pos_center.setStyleSheet(wc.pb_f)
                self.c_pos_center.setObjectName("c_pos_center")
                self.c_pos_center.clicked.connect(self.c_p_set_center)

                self.c_pos_right = QPushButton(self.clock_setting_page)
                self.c_pos_right.setGeometry(QRect(460, 80, 111, 23))
                self.c_pos_right.setStyleSheet(wc.pb_f)
                self.c_pos_right.setObjectName("c_pos_right")
                self.c_pos_right.clicked.connect(self.c_p_set_right)

                self.c_pos_self = QPushButton(self.clock_setting_page)
                self.c_pos_self.setGeometry(QRect(580, 80, 111, 23))
                self.c_pos_self.setStyleSheet(wc.pb_f)
                self.c_pos_self.setObjectName("c_pos_self")
                self.c_pos_self.clicked.connect(self.c_p_self)

                if cinidown("clock_pos") == "left":
                    self.c_pos_left.setStyleSheet(wc.pb_t)
                elif cinidown("clock_pos") == "center":
                    self.c_pos_center.setStyleSheet(wc.pb_t)
                elif cinidown("clock_pos") == "right":
                    self.c_pos_right.setStyleSheet(wc.pb_t)
                else:
                    self.c_pos_self.setStyleSheet(wc.pb_t)

                #시계 위치 - self
                self.c_pos_self_label = QLabel(self.clock_setting_page)
                self.c_pos_self_label.setGeometry(QRect(110, 150, 81, 21))
                self.c_pos_self_label.setObjectName("c_pos_self_label")

                self.c_pos_x = QSpinBox(self.clock_setting_page)
                self.c_pos_x.setGeometry(QRect(220, 150, 231, 22))
                self.c_pos_x.setAutoFillBackground(False)
                self.c_pos_x.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
                self.c_pos_x.setFrame(False)
                self.c_pos_x.setMinimum(-10000)
                self.c_pos_x.setMaximum(10000)
                self.c_pos_x.setSingleStep(50)
                self.c_pos_x.setObjectName("c_pos_x")
                self.c_pos_x.setValue(int(cinidown("clock_x")))
                self.c_pos_x.valueChanged.connect(self.c_p_self)

                self.c_pos_y = QSpinBox(self.clock_setting_page)
                self.c_pos_y.setGeometry(QRect(460, 150, 231, 22))
                self.c_pos_y.setAutoFillBackground(False)
                self.c_pos_y.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
                self.c_pos_y.setFrame(False)
                self.c_pos_y.setMinimum(-10000)
                self.c_pos_y.setMaximum(10000)
                self.c_pos_y.setSingleStep(50)
                self.c_pos_y.setObjectName("c_pos_y")
                self.c_pos_y.valueChanged.connect(self.c_p_self)
                self.c_pos_y.setValue(int(cinidown("clock_y")))

                #글자크키
                self.c_fsize_label = QLabel(self.clock_setting_page)
                self.c_fsize_label.setGeometry(QRect(70, 220, 111, 21))
                self.c_fsize_label.setObjectName("c_fsize_label")

                self.c_fsize_spin = QSpinBox(self.clock_setting_page)
                self.c_fsize_spin.setGeometry(QRect(220, 220, 181, 22))
                self.c_fsize_spin.setAutoFillBackground(False)
                self.c_fsize_spin.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0, 0, 0);")
                self.c_fsize_spin.setFrame(False)
                self.c_fsize_spin.setObjectName("c_fsize_spin")
                self.c_fsize_spin.setValue(int(cinidown("font_size")))

                self.c_fsize_spin.valueChanged.connect(self.c_fs_set)

                #글자 색 <
                self.c_fcolor_label = QLabel(self.clock_setting_page)
                self.c_fcolor_label.setGeometry(QRect(420, 220, 71, 21))
                self.c_fcolor_label.setObjectName("c_fcolor_label")

                self.c_fcolor_pick = QPushButton(self.clock_setting_page)
                self.c_fcolor_pick.setGeometry(QRect(510, 220, 181, 23))
                self.c_fcolor_pick.setStyleSheet(wc.pb_f)
                self.c_fcolor_pick.setObjectName("c_fcolor_pick")
                self.c_fcolor_pick.clicked.connect(self.c_fcolor_set)

                #폰트설정 <
                self.c_fset_label = QLabel(self.clock_setting_page)
                self.c_fset_label.setGeometry(QRect(70, 290, 81, 21))
                self.c_fset_label.setObjectName("c_fset_label")

                self.c_fset_set = QPushButton(self.clock_setting_page)
                self.c_fset_set.setGeometry(QRect(220, 290, 231, 23))
                self.c_fset_set.setStyleSheet(wc.pb_f)
                self.c_fset_set.setObjectName("c_fset_set")
                self.c_fset_set.clicked.connect(self.c_setfont_set)

                self.c_fset_def = QPushButton(self.clock_setting_page)
                self.c_fset_def.setGeometry(QRect(460, 290, 231, 23))
                self.c_fset_def.setStyleSheet(wc.pb_f)
                self.c_fset_def.setObjectName("c_fset_def")
                self.c_fset_def.clicked.connect(self.c_deffont_set)

                # 배경화면 설정 <
                self.c_wallset_label = QLabel(self.clock_setting_page)
                self.c_wallset_label.setGeometry(QRect(70, 360, 101, 21))
                self.c_wallset_label.setObjectName("c_wallset_label")

                self.c_wallset_set = QPushButton(self.clock_setting_page)
                self.c_wallset_set.setGeometry(QRect(220, 360, 231, 23))
                self.c_wallset_set.setStyleSheet(wc.pb_f)
                self.c_wallset_set.setObjectName("c_wallset_set")
                self.c_wallset_set.clicked.connect(self.c_setwall_set)

                self.c_wallset_def = QPushButton(self.clock_setting_page)
                self.c_wallset_def.setGeometry(QRect(460, 360, 231, 23))
                self.c_wallset_def.setStyleSheet(wc.pb_f)
                self.c_wallset_def.setObjectName("c_wallset_def")
                self.c_wallset_def.clicked.connect(self.c_defwall_set)
                # 배경화면 설정 >

                # 적용하기
                self.c_apply = QPushButton(self.clock_setting_page)
                self.c_apply.setGeometry(QRect(580, 500, 111, 23))
                self.c_apply.setStyleSheet(wc.pb_f)
                self.c_apply.setObjectName("c_apply")
                self.c_apply.clicked.connect(self.apply)
                # 적용하기

                # 프리뷰
                self.c_preview_label = QLabel(self.clock_setting_page)
                self.c_preview_label.setGeometry(QRect(70, 500, 101, 21))
                self.c_preview_label.setObjectName("c_preview_label")

                self.c_preview = QLabel(self.clock_setting_page)
                self.c_preview.setGeometry(QRect(220, 440, 261, 141))
                self.c_preview.setAutoFillBackground(False)
                self.c_preview.setObjectName("c_preview")
                #프리뷰

                self.stacked_widget.addWidget(self.clock_setting_page)

                #######[ 문구 설정 ] 페이지 ########
                self.text_setting_page = QWidget()
                self.text_setting_page.setObjectName("text_setting_page")

                #커스텀 문구
                self.t_custext_set = QPushButton(self.text_setting_page)
                self.t_custext_set.setGeometry(QRect(220, 80, 471, 23))
                self.t_custext_set.setStyleSheet(wc.pb_f)
                self.t_custext_set.setObjectName("t_custext_set")
                self.t_custext_set.clicked.connect(self.move_tab_custext)

                self.t_custext_label = QLabel(self.text_setting_page)
                self.t_custext_label.setGeometry(QRect(70, 80, 101, 21))
                self.t_custext_label.setObjectName("t_custext_label")

                #문구 불러오기
                self.t_mode_label = QLabel(self.text_setting_page)
                self.t_mode_label.setGeometry(QRect(70, 150, 101, 21))
                self.t_mode_label.setObjectName("t_mode_label")

                self.t_mode_online = QPushButton(self.text_setting_page)
                self.t_mode_online.setGeometry(QRect(220, 150, 151, 23))
                self.t_mode_online.setStyleSheet(wc.pb_f)
                self.t_mode_online.setObjectName("t_mode_online")
                self.t_mode_online.clicked.connect(self.t_mode_set_online)

                self.t_mode_custom = QPushButton(self.text_setting_page)
                self.t_mode_custom.setGeometry(QRect(540, 150, 151, 23))
                self.t_mode_custom.setStyleSheet(wc.pb_f)
                self.t_mode_custom.setObjectName("t_mode_offline_2")
                self.t_mode_custom.clicked.connect(self.t_mode_set_custom)

                self.t_mode_offline = QPushButton(self.text_setting_page)
                self.t_mode_offline.setGeometry(QRect(380, 150, 151, 23))
                self.t_mode_offline.setStyleSheet(wc.pb_f)
                self.t_mode_offline.setObjectName("t_mode_offline")
                self.t_mode_offline.clicked.connect(self.t_mode_set_offline)

                if cinidown("where_text") == "offline":
                    self.t_mode_offline.setStyleSheet(wc.pb_t)
                elif cinidown("where_text") == "custom":
                    self.t_mode_custom.setStyleSheet(wc.pb_t)
                else:
                    self.t_mode_online.setStyleSheet(wc.pb_t)

                #문구 새로고침
                self.t_reflesh_label = QLabel(self.text_setting_page)
                self.t_reflesh_label.setGeometry(QRect(70, 220, 101, 21))
                self.t_reflesh_label.setObjectName("t_reflesh_label")

                self.t_reflesh_text = QPushButton(self.text_setting_page)
                self.t_reflesh_text.setGeometry(QRect(220, 220, 471, 23))
                self.t_reflesh_text.setStyleSheet(wc.pb_f)
                self.t_reflesh_text.setObjectName("t_reflesh_text")
                self.t_reflesh_text.clicked.connect(self.t_reflseh_set)

                #문구 정렬
                self.t_align_left = QPushButton(self.text_setting_page)
                self.t_align_left.setGeometry(QRect(220, 290, 151, 23))
                self.t_align_left.setStyleSheet(wc.pb_f)
                self.t_align_left.setObjectName("t_align_left")
                self.t_align_left.clicked.connect(self.t_align_left_set)

                self.t_align_center = QPushButton(self.text_setting_page)
                self.t_align_center.setGeometry(QRect(380, 290, 151, 23))
                self.t_align_center.setStyleSheet(wc.pb_f)
                self.t_align_center.setObjectName("t_align_center")
                self.t_align_center.clicked.connect(self.t_align_center_set)

                self.t_align_right = QPushButton(self.text_setting_page)
                self.t_align_right.setGeometry(QRect(540, 290, 151, 23))
                self.t_align_right.setStyleSheet(wc.pb_f)
                self.t_align_right.setObjectName("t_align_right")
                self.t_align_right.clicked.connect(self.t_align_right_set)

                self.t_align_label = QLabel(self.text_setting_page)
                self.t_align_label.setGeometry(QRect(70, 290, 81, 21))
                self.t_align_label.setObjectName("t_align_label")

                if cinidown("font_align") == "left":
                    self.t_align_left.setStyleSheet(wc.pb_t)
                elif cinidown("font_align") == "center":
                    self.t_align_center.setStyleSheet(wc.pb_t)
                elif cinidown("font_align") == "right":
                    self.t_align_right.setStyleSheet(wc.pb_t)

                #미리보기
                self.t_preview_label = QLabel(self.text_setting_page)
                self.t_preview_label.setGeometry(QRect(70, 500, 101, 21))
                self.t_preview_label.setObjectName("t_preview_label")

                self.t_preview = QLabel(self.text_setting_page)
                self.t_preview.setGeometry(QRect(220, 440, 261, 141))
                self.t_preview.setAutoFillBackground(False)
                self.t_preview.setStyleSheet("")
                self.t_preview.setText("")
                self.t_preview.setObjectName("t_preview")

                #적용하기
                self.t_apply = QPushButton(self.text_setting_page)
                self.t_apply.setGeometry(QRect(580, 500, 111, 23))
                self.t_apply.setStyleSheet(wc.pb_f)
                self.t_apply.setObjectName("t_apply")
                self.t_apply.clicked.connect(self.apply)

                self.stacked_widget.addWidget(self.text_setting_page)

                #########[ 시계 정보 ] 페이지 #########
                self.clock_info_page = QWidget()
                self.clock_info_page.setObjectName("clock_info_page")

                #시계 정보
                self.info_wcii_icon = QLabel(self.clock_info_page)
                self.info_wcii_icon.setGeometry(QRect(320, 70, 111, 101))
                self.info_wcii_icon.setStyleSheet("image: url(wc_source/ui/wcii_icon.png);")
                self.info_wcii_icon.setText("")
                self.info_wcii_icon.setObjectName("info_wcii_icon")

                self.info_label = QLabel(self.clock_info_page)
                self.info_label.setGeometry(QRect(10, 180, 741, 171))
                self.info_label.setObjectName("info_label")

                self.info_label.setOpenExternalLinks(True)

                #업데이트
                self.url_update = QLabel(self.clock_info_page)
                self.url_update.setGeometry(QRect(0, 370, 761, 21))
                self.url_update.setStyleSheet("")
                self.url_update.setObjectName("url_update")
                self.url_update.setText("")
                self.url_update.setOpenExternalLinks(True)
                #self.url_update.setText("<html><head/><body><p align=\"center\"><a href=\"https://whatclockisit.xyz/beta/download.html\"><span style=\" text-decoration: underline; color:#6265e7;\">업데이트가 있어요!</span></a></p></body></html>")

                #업데이트 확인하기
                self.checkupdate_button = QPushButton(self.clock_info_page)
                self.checkupdate_button.setGeometry(QRect(20, 580, 161, 21))
                self.checkupdate_button.setStyleSheet(wc.pb_f)
                self.checkupdate_button.setObjectName("checkupdate_button")
                self.checkupdate_button.clicked.connect(self.check_update)

                #오류 보내기
                self.goerror_button = QPushButton(self.clock_info_page)
                self.goerror_button.setGeometry(QRect(610, 550, 141, 21))
                self.goerror_button.setStyleSheet(wc.pb_f)
                self.goerror_button.setObjectName("goerror_button")
                self.goerror_button.clicked.connect(self.move_tab_goerror)

                #데이터 초기화
                self.reset_data = QPushButton(self.clock_info_page)
                self.reset_data.setGeometry(QRect(610, 580, 141, 23))
                self.reset_data.setStyleSheet(wc.pb_f)
                self.reset_data.setObjectName("goerror_button")
                self.reset_data.clicked.connect(self.reset)

                self.stacked_widget.addWidget(self.clock_info_page)

                ########[ 오류 보내기 ] 페이지 ########
                self.goerror_page = QWidget()
                self.goerror_page.setObjectName("goerror_page")
                #타이틀
                self.goerror_label = QLabel(self.goerror_page)
                self.goerror_label.setGeometry(QRect(50, 70, 671, 31))
                self.goerror_label.setObjectName("goerror_label")

                #이름
                self.name_label = QLabel(self.goerror_page)
                self.name_label.setGeometry(QRect(50, 130, 221, 31))
                self.name_label.setObjectName("name_label")

                self.name_line = QLineEdit(self.goerror_page)
                self.name_line.setGeometry(QRect(290, 130, 431, 31))
                self.name_line.setAutoFillBackground(False)
                self.name_line.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "color: rgb(0, 0, 0);")
                self.name_line.setFrame(False)
                self.name_line.setObjectName("name_line")
                self.name_line.setPlaceholderText("이름을 입력하세요!")

                #이메일
                self.email_label = QLabel(self.goerror_page)
                self.email_label.setGeometry(QRect(50, 190, 211, 31))
                self.email_label.setObjectName("email_label")

                self.email_line = QLineEdit(self.goerror_page)
                self.email_line.setGeometry(QRect(290, 190, 431, 31))
                self.email_line.setAutoFillBackground(False)
                self.email_line.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "color: rgb(0, 0, 0);")
                self.email_line.setFrame(False)
                self.email_line.setObjectName("email_line")
                self.email_line.setPlaceholderText("이메일을 입력하세요! (선택)")

                #답변 위치
                self.how_reply = QLabel(self.goerror_page)
                self.how_reply.setGeometry(QRect(50, 250, 211, 21))
                self.how_reply.setObjectName("how_reply")

                self.reply_discord = QPushButton(self.goerror_page)
                self.reply_discord.setGeometry(QRect(300, 250, 141, 21))
                self.reply_discord.setStyleSheet(wc.pb_t)
                self.reply_discord.setObjectName("reply_discord")
                self.reply_discord.clicked.connect(self.goerror_where_setting)

                self.reply_email = QPushButton(self.goerror_page)
                self.reply_email.setGeometry(QRect(450, 250, 131, 23))
                self.reply_email.setStyleSheet(wc.pb_f)
                self.reply_email.setObjectName("reply_email")
                self.reply_email.clicked.connect(self.goerror_where_core)

                self.reply_no = QPushButton(self.goerror_page)
                self.reply_no.setGeometry(QRect(590, 250, 131, 23))
                self.reply_no.setStyleSheet(wc.pb_f)
                self.reply_no.setObjectName("reply_no")
                self.reply_no.clicked.connect(self.goerror_where_other)

                self.error_text = QTextEdit(self.goerror_page)
                self.error_text.setGeometry(QRect(50, 350, 661, 201))
                self.error_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "color: rgb(0, 0, 0);")
                self.error_text.setObjectName("error_text")
                self.error_text.setPlaceholderText("오류에 대해서 할 말이나 프로그램 전반에 대한 말이 있다면 적어주세요\n\n"
                                                   "만약 이메일외의 수단(디스코드 DM, 카카오톡 등)으로 받고 싶다면 이 곳에 적어주세요!\n\n"
                                                   "오류를 보낼 때 자동으로 로그 파일이 같이 보내집니다!\n\n"
                                                   "만약 캡쳐등의 첨부파일을 보내실려면 먼저 이곳에서 오류 보내기를 먼저 하고\n"
                                                   "디스코드 서버, 혹은 제 이메일 주소인 hyuns@hyuns.space 로 보내주세요!")

                # self.reply_discord.setCheckable(True)
                # self.reply_email.setCheckable(True)
                # self.reply_no.setCheckable(True)

                #자세한 내용
                self.error_label = QLabel(self.goerror_page)
                self.error_label.setGeometry(QRect(50, 310, 211, 21))
                self.error_label.setObjectName("error_label")

                # #로그 확인
                self.check_log_button = QPushButton(self.goerror_page)
                self.check_log_button.setGeometry(QRect(50, 580, 141, 23))
                self.check_log_button.setStyleSheet(wc.pb_f)
                self.check_log_button.setObjectName("check_log_button")
                self.check_log_button.clicked.connect(self.check_log_set)

                #오류 보내기
                self.goerror_button_2 = QPushButton(self.goerror_page)
                self.goerror_button_2.setGeometry(QRect(570, 580, 141, 23))
                self.goerror_button_2.setStyleSheet(wc.pb_f)
                self.goerror_button_2.setObjectName("goerror_button_2")
                self.goerror_button_2.clicked.connect(self.gogoerror)


                self.stacked_widget.addWidget(self.goerror_page)

                ########[ 커스텀 텍스트 ] 페이지 ########
                self.custext_page = QWidget()
                self.custext_page.setObjectName("custext_page")

                #타이틀
                self.cus_label = QLabel(self.custext_page)
                self.cus_label.setGeometry(QRect(20, 60, 211, 21))
                self.cus_label.setStyleSheet("font: 13pt;")
                self.cus_label.setObjectName("cus_label")

                #스크롤
                self.scrollArea = QScrollArea(self.custext_page)
                self.scrollArea.setGeometry(QRect(20, 89, 711, 471))
                self.scrollArea.setAutoFillBackground(True)
                self.scrollArea.setStyleSheet("background-color: rgb(27, 27, 27);color: rgb(255, 255, 255);font: 87 11pt \"Noto Sans CJK KR Black\"")
                self.scrollArea.setFrameShadow(QFrame.Sunken)
                self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
                self.scrollArea.setWidgetResizable(False)
                self.scrollArea.setObjectName("scrollArea")

                self.scrollAreaWidgetContents = QWidget()
                self.scrollAreaWidgetContents.setGeometry(QRect(0, -510, 694, 981))
                self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

                # 7시
                self.time_07_label = QLabel(self.scrollAreaWidgetContents)
                self.time_07_label.setGeometry(QRect(30, 10, 111, 31))
                self.time_07_label.setObjectName("time_07_label")

                self.time_07 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_07.setGeometry(QRect(160, 10, 491, 31))

                self.time_07.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_07.setMaxLength(20)
                self.time_07.setObjectName("time_07")

                # 8시
                self.time_08_label = QLabel(self.scrollAreaWidgetContents)
                self.time_08_label.setGeometry(QRect(30, 50, 111, 31))
                self.time_08_label.setObjectName("time_08_label")

                self.time_08 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_08.setGeometry(QRect(160, 50, 491, 31))
                self.time_08.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_08.setMaxLength(20)
                self.time_08.setObjectName("time_08")

                # 9시
                self.time_09_label_2 = QLabel(self.scrollAreaWidgetContents)
                self.time_09_label_2.setGeometry(QRect(30, 90, 111, 31))
                self.time_09_label_2.setObjectName("time_09_label_2")

                self.time_09 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_09.setGeometry(QRect(160, 90, 491, 31))
                self.time_09.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_09.setMaxLength(20)
                self.time_09.setObjectName("time_09")

                # 10시
                self.time_10_label = QLabel(self.scrollAreaWidgetContents)
                self.time_10_label.setGeometry(QRect(30, 130, 111, 31))
                self.time_10_label.setObjectName("time_10_label")

                self.time_10 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_10.setGeometry(QRect(160, 130, 491, 31))
                self.time_10.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_10.setMaxLength(20)
                self.time_10.setObjectName("time_10")

                # 11시
                self.time_11_label = QLabel(self.scrollAreaWidgetContents)
                self.time_11_label.setGeometry(QRect(30, 170, 111, 31))
                self.time_11_label.setObjectName("time_11_label")

                self.time_11 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_11.setGeometry(QRect(160, 170, 491, 31))
                self.time_11.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_11.setMaxLength(20)
                self.time_11.setObjectName("time_11")

                # 12시
                self.time_12_label = QLabel(self.scrollAreaWidgetContents)
                self.time_12_label.setGeometry(QRect(30, 210, 111, 31))
                self.time_12_label.setObjectName("time_12_label")

                self.time_12 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_12.setGeometry(QRect(160, 210, 491, 31))
                self.time_12.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_12.setMaxLength(20)
                self.time_12.setObjectName("time_12")

                # 13시
                self.time_13_label = QLabel(self.scrollAreaWidgetContents)
                self.time_13_label.setGeometry(QRect(30, 250, 111, 31))
                self.time_13_label.setObjectName("time_13_label")

                self.time_13 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_13.setGeometry(QRect(160, 250, 491, 31))
                self.time_13.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_13.setMaxLength(20)
                self.time_13.setObjectName("time_13")

                # 14시
                self.time_14_label = QLabel(self.scrollAreaWidgetContents)
                self.time_14_label.setGeometry(QRect(30, 290, 111, 31))
                self.time_14_label.setObjectName("time_14_label")

                self.time_14 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_14.setGeometry(QRect(160, 290, 491, 31))
                self.time_14.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_14.setMaxLength(20)
                self.time_14.setObjectName("time_14")


                # 15시
                self.time_15_label = QLabel(self.scrollAreaWidgetContents)
                self.time_15_label.setGeometry(QRect(30, 330, 111, 31))
                self.time_15_label.setObjectName("time_15_label")

                self.time_15 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_15.setGeometry(QRect(160, 330, 491, 31))
                self.time_15.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_15.setMaxLength(20)
                self.time_15.setObjectName("time_15")

                # 16시
                self.time_16_label = QLabel(self.scrollAreaWidgetContents)
                self.time_16_label.setGeometry(QRect(30, 370, 111, 31))
                self.time_16_label.setObjectName("time_16_label")

                self.time_16 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_16.setGeometry(QRect(160, 370, 491, 31))
                self.time_16.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_16.setMaxLength(20)
                self.time_16.setObjectName("time_16")

                # 17시
                self.time_17_label = QLabel(self.scrollAreaWidgetContents)
                self.time_17_label.setGeometry(QRect(30, 410, 111, 31))
                self.time_17_label.setObjectName("time_17_label")

                self.time_17 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_17.setGeometry(QRect(160, 410, 491, 31))
                self.time_17.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_17.setMaxLength(20)
                self.time_17.setObjectName("time_17")

                # 18시
                self.time_18_label = QLabel(self.scrollAreaWidgetContents)
                self.time_18_label.setGeometry(QRect(30, 450, 111, 31))
                self.time_18_label.setObjectName("time_18_label")

                self.time_18 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_18.setGeometry(QRect(160, 450, 491, 31))
                self.time_18.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_18.setMaxLength(20)
                self.time_18.setObjectName("time_18")

                # 19시
                self.time_19_label = QLabel(self.scrollAreaWidgetContents)
                self.time_19_label.setGeometry(QRect(30, 490, 111, 31))
                self.time_19_label.setObjectName("time_19_label")

                self.time_19 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_19.setGeometry(QRect(160, 490, 491, 31))
                self.time_19.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_19.setMaxLength(20)
                self.time_19.setObjectName("time_19")

                # 20시
                self.time_20_label = QLabel(self.scrollAreaWidgetContents)
                self.time_20_label.setGeometry(QRect(30, 530, 111, 31))
                self.time_20_label.setObjectName("time_20_label")

                self.time_20 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_20.setGeometry(QRect(160, 530, 491, 31))
                self.time_20.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_20.setMaxLength(20)
                self.time_20.setObjectName("time_20")

                # 21시
                self.time_21_label = QLabel(self.scrollAreaWidgetContents)
                self.time_21_label.setGeometry(QRect(30, 570, 111, 31))
                self.time_21_label.setObjectName("time_21_label")

                self.time_21 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_21.setGeometry(QRect(160, 570, 491, 31))
                self.time_21.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_21.setMaxLength(20)
                self.time_21.setObjectName("time_21")

                # 22시
                self.time_22_label = QLabel(self.scrollAreaWidgetContents)
                self.time_22_label.setGeometry(QRect(30, 610, 111, 31))
                self.time_22_label.setObjectName("time_22_label")

                self.time_22 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_22.setGeometry(QRect(160, 610, 491, 31))
                self.time_22.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_22.setMaxLength(20)
                self.time_22.setObjectName("time_22")

                # 23시
                self.time_23_label = QLabel(self.scrollAreaWidgetContents)
                self.time_23_label.setGeometry(QRect(30, 650, 111, 31))
                self.time_23_label.setObjectName("time_23_label")

                self.time_23 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_23.setGeometry(QRect(160, 650, 491, 31))
                self.time_23.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_23.setMaxLength(20)
                self.time_23.setObjectName("time_23")

                # 0시
                self.time_00_label = QLabel(self.scrollAreaWidgetContents)
                self.time_00_label.setGeometry(QRect(30, 690, 111, 31))
                self.time_00_label.setObjectName("time_00_label")

                self.time_00 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_00.setGeometry(QRect(160, 690, 491, 31))
                self.time_00.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_00.setMaxLength(20)
                self.time_00.setObjectName("time_00")


                # 1시
                self.time_01_label = QLabel(self.scrollAreaWidgetContents)
                self.time_01_label.setGeometry(QRect(30, 730, 111, 31))
                self.time_01_label.setObjectName("time_01_label")

                self.time_01 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_01.setGeometry(QRect(160, 730, 491, 31))
                self.time_01.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_01.setMaxLength(20)
                self.time_01.setObjectName("time_01")

                # 2시
                self.time_02_label = QLabel(self.scrollAreaWidgetContents)
                self.time_02_label.setGeometry(QRect(30, 770, 111, 31))
                self.time_02_label.setObjectName("time_02_label")

                self.time_02 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_02.setGeometry(QRect(160, 770, 491, 31))
                self.time_02.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_02.setMaxLength(20)
                self.time_02.setObjectName("time_02")

                # 3시
                self.time_03_label = QLabel(self.scrollAreaWidgetContents)
                self.time_03_label.setGeometry(QRect(30, 810, 111, 31))
                self.time_03_label.setObjectName("time_03_label")

                self.time_03 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_03.setGeometry(QRect(160, 810, 491, 31))
                self.time_03.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_03.setMaxLength(20)
                self.time_03.setObjectName("time_03")

                # 4시
                self.time_04_label = QLabel(self.scrollAreaWidgetContents)
                self.time_04_label.setGeometry(QRect(30, 850, 111, 31))
                self.time_04_label.setObjectName("time_04_label")

                self.time_04 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_04.setGeometry(QRect(160, 850, 491, 31))
                self.time_04.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_04.setMaxLength(20)
                self.time_04.setObjectName("time_04")

                # 5시
                self.time_05_label = QLabel(self.scrollAreaWidgetContents)
                self.time_05_label.setGeometry(QRect(30, 890, 111, 31))
                self.time_05_label.setObjectName("time_05_label")

                self.time_05 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_05.setGeometry(QRect(160, 890, 491, 31))
                self.time_05.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_05.setMaxLength(20)
                self.time_05.setObjectName("time_05")

                # 6시
                self.time_06_label = QLabel(self.scrollAreaWidgetContents)
                self.time_06_label.setGeometry(QRect(30, 930, 111, 31))
                self.time_06_label.setObjectName("time_06_label")

                self.time_06 = QLineEdit(self.scrollAreaWidgetContents)
                self.time_06.setGeometry(QRect(160, 930, 491, 31))
                self.time_06.setStyleSheet("color: rgb(0, 0, 0);\n"
                                           "background-color: rgb(255, 255, 255);")
                self.time_06.setMaxLength(20)
                self.time_06.setObjectName("time_06")

                self.scrollArea.setWidget(self.scrollAreaWidgetContents)

                #초기화
                self.text_reset = QPushButton(self.custext_page)
                self.text_reset.setGeometry(QRect(20, 580, 161, 23))
                self.text_reset.setStyleSheet(wc.pb_f)
                self.text_reset.setObjectName("text_reset")
                self.text_reset.clicked.connect(self.custom_reset_set)

                #취소하기
                self.text_cancel = QPushButton(self.custext_page)
                self.text_cancel.setGeometry(QRect(470, 580, 121, 23))
                self.text_cancel.setStyleSheet(wc.pb_f)
                self.text_cancel.setObjectName("text_cancel")
                self.text_cancel.clicked.connect(self.custom_reflesh)

                #저장하기
                self.text_apply = QPushButton(self.custext_page)
                self.text_apply.setGeometry(QRect(610, 580, 121, 23))
                self.text_apply.setStyleSheet(wc.pb_f)
                self.text_apply.setObjectName("text_apply")
                self.text_apply.clicked.connect(self.custom_apply_set)

                self.stacked_widget.addWidget(self.custext_page)

                #최종
                self.preview()
                self.custom_reflesh()
                self.retranslateUi(Form)
                self.stacked_widget.setCurrentIndex(0)
                QMetaObject.connectSlotsByName(Form)
            except Exception as e:
                errorlog("<u_01> " + str(e))

        try:
            try:
                def move_tab_wcii(self, Form):
                    tab_on = "QPushButton{font-size: 17px; color: rgb(255,255,255)}\nQPushButton:hover{color: rgb(255,255,255)}"
                    tab_off = "QPushButton{font-size: 17px; color: rgb(120,120,120)}\nQPushButton:hover{color: rgb(255,255,255)}"
                    self.stacked_widget.setCurrentIndex(0)
                    self.wcii_button.setStyleSheet(tab_on)
                    self.clock_setting_button.setStyleSheet(tab_off)
                    self.text_setting_button.setStyleSheet(tab_off)
                    self.clock_info_button.setStyleSheet(tab_off)

                def move_tab_clock(self, Form):
                    tab_on = "QPushButton{font-size: 17px; color: rgb(255,255,255)}\nQPushButton:hover{color: rgb(255,255,255)}"
                    tab_off = "QPushButton{font-size: 17px; color: rgb(120,120,120)}\nQPushButton:hover{color: rgb(255,255,255)}"
                    self.stacked_widget.setCurrentIndex(1)
                    self.wcii_button.setStyleSheet(tab_off)
                    self.clock_setting_button.setStyleSheet(tab_on)
                    self.text_setting_button.setStyleSheet(tab_off)
                    self.clock_info_button.setStyleSheet(tab_off)

                def move_tab_text(self, Form):
                    tab_on = "QPushButton{font-size: 17px; color: rgb(255,255,255)}\nQPushButton:hover{color: rgb(255,255,255)}"
                    tab_off = "QPushButton{font-size: 17px; color: rgb(120,120,120)}\nQPushButton:hover{color: rgb(255,255,255)}"
                    self.stacked_widget.setCurrentIndex(2)
                    self.wcii_button.setStyleSheet(tab_off)
                    self.clock_setting_button.setStyleSheet(tab_off)
                    self.text_setting_button.setStyleSheet(tab_on)
                    self.clock_info_button.setStyleSheet(tab_off)

                def move_tab_info(self, Form):
                    tab_on = "QPushButton{font-size: 17px; color: rgb(255,255,255)}\nQPushButton:hover{color: rgb(255,255,255)}"
                    tab_off = "QPushButton{font-size: 17px; color: rgb(120,120,120)}\nQPushButton:hover{color: rgb(255,255,255)}"
                    self.stacked_widget.setCurrentIndex(3)
                    self.wcii_button.setStyleSheet(tab_off)
                    self.clock_setting_button.setStyleSheet(tab_off)
                    self.text_setting_button.setStyleSheet(tab_off)
                    self.clock_info_button.setStyleSheet(tab_on)

                def move_tab_other(self, Form):
                    tab_off = "QPushButton{font-size: 17px; color: rgb(120,120,120)}\nQPushButton:hover{color: rgb(255,255,255)}"
                    self.wcii_button.setStyleSheet(tab_off)
                    self.clock_setting_button.setStyleSheet(tab_off)
                    self.text_setting_button.setStyleSheet(tab_off)
                    self.clock_info_button.setStyleSheet(tab_off)
            except Exception as e:
                errorlog("<u_d00> " + str(e))

            try:
                def c_p_set_left(self):
                    uiniup("clock_pos", "left")
                    self.c_pos_left.setStyleSheet(wc.pb_t)
                    self.c_pos_center.setStyleSheet(wc.pb_f)
                    self.c_pos_right.setStyleSheet(wc.pb_f)
                    self.c_pos_self.setStyleSheet(wc.pb_f)
                    self.preview()

                def c_p_set_center(self):
                    uiniup("clock_pos", "center")
                    self.c_pos_left.setStyleSheet(wc.pb_f)
                    self.c_pos_center.setStyleSheet(wc.pb_t)
                    self.c_pos_right.setStyleSheet(wc.pb_f)
                    self.c_pos_self.setStyleSheet(wc.pb_f)
                    self.preview()

                def c_p_set_right(self):
                    uiniup("clock_pos", "right")
                    self.c_pos_left.setStyleSheet(wc.pb_f)
                    self.c_pos_center.setStyleSheet(wc.pb_f)
                    self.c_pos_right.setStyleSheet(wc.pb_t)
                    self.c_pos_self.setStyleSheet(wc.pb_f)
                    self.preview()

                def c_p_set_self(self):
                    uiniup("clock_pos", "self")
                    self.c_pos_left.setStyleSheet(wc.pb_f)
                    self.c_pos_center.setStyleSheet(wc.pb_f)
                    self.c_pos_right.setStyleSheet(wc.pb_f)
                    self.c_pos_self.setStyleSheet(wc.pb_t)
                    self.preview()

                def c_p_self(self):
                    uiniup("clock_pos", "self")
                    self.c_pos_left.setStyleSheet(wc.pb_f)
                    self.c_pos_center.setStyleSheet(wc.pb_f)
                    self.c_pos_right.setStyleSheet(wc.pb_f)
                    self.c_pos_self.setStyleSheet(wc.pb_t)
                    uiniup("clock_x", str(self.c_pos_x.value()))
                    uiniup("clock_y", str(self.c_pos_y.value()))
                    self.preview()

            except Exception as e:
                errorlog("<u_d01> " + str(e))

            try:

                def c_fcolor_set(self, Form):
                    col = QColorDialog.getColor()
                    print(col.isValid())
                    if col.isValid() == True:
                        uiniup("font_color", f"({col.red()}, {col.green()}, {col.blue()})")
                        self.preview()

                def c_fs_set(self):
                    uiniup('font_size', str(self.c_fsize_spin.value()))
                    self.preview()

                def c_setfont_set(self, Form):
                    c_title = "폰트파일을 골라주세요"
                    c_filter = "폰트파일(*.ttf *.otf)"
                    ff_link = QFileDialog.getOpenFileName(self ,c_title, None, c_filter)
                    print(ff_link)
                    if ff_link[0] != "":
                        ff_link = ff_link[0]
                        print(ff_link[-3:-1])
                        if ff_link[-3:-1] == "ot":
                            print("otf 감지")
                            shutil.copyfile(ff_link, wc.rsfontotf)
                            try:
                                os.remove(wc.rsfontttf)
                            except:
                                pass
                        elif ff_link[-3:-1] == "tt":
                            print("ttf 감지")
                            shutil.copyfile(ff_link, wc.rsfontttf)
                            try:
                                os.remove(wc.rsfontotf)
                            except:
                                pass

                        if self.already:
                            wcii_wallpaper()
                            self.pixmap = QPixmap(wc.showtemp).scaledToHeight(141)
                        else:
                            wcii_wallpaper(True)
                            self.pixmap = QPixmap(wc.preview).scaledToHeight(141)

                        self.c_preview.setPixmap(self.pixmap)
                        self.t_preview.setPixmap(self.pixmap)

                def c_deffont_set(self):
                    shutil.copyfile(wc.dsource + "font.otf", wc.rsfontotf)
                    if self.already:
                        wcii_wallpaper()
                        self.pixmap = QPixmap(wc.showtemp).scaledToHeight(141)
                    else:
                        wcii_wallpaper(True)
                        self.pixmap = QPixmap(wc.preview).scaledToHeight(141)

                    self.c_preview.setPixmap(self.pixmap)
                    self.t_preview.setPixmap(self.pixmap)

            except Exception as e:
                errorlog("<u_d02> " + str(e))

            try:
                def c_setwall_set(self):
                    title = "배경사진을 골라주세요"
                    filter = "사진 파일(*.png)"
                    wp_link = QFileDialog.getOpenFileName(self, title, None, filter)
                    if wp_link[0] != "":
                        uiniup('wall_mode', "picture")
                        shutil.copyfile(wp_link[0], wc.oriimage)
                        resizeimage()
                        if self.already:
                            wcii_wallpaper()
                            self.pixmap = QPixmap(wc.showtemp).scaledToHeight(141)
                        else:
                            wcii_wallpaper(True)
                            self.pixmap = QPixmap(wc.preview).scaledToHeight(141)

                        self.c_preview.setPixmap(self.pixmap)
                        self.t_preview.setPixmap(self.pixmap)

                def c_defwall_set(self):
                    col = QColorDialog.getColor()
                    print(col.isValid())
                    if col.isValid() == True:
                        uiniup("wall_color", f"({col.red()}, {col.green()}, {col.blue()})")
                        ciniup("wall_color", f"({col.red()}, {col.green()}, {col.blue()})")
                        uiniup("wall_mode", "solid")
                        ciniup("wall_mode", "solid")
                        solidimage()
                        if self.already:
                            wcii_wallpaper()
                            self.pixmap = QPixmap(wc.showtemp).scaledToHeight(141)
                        else:
                            wcii_wallpaper(True)
                            self.pixmap = QPixmap(wc.preview).scaledToHeight(141)
                        self.pixmap = QPixmap(wc.temp + "showtemp.png").scaledToHeight(141)
                        self.c_preview.setPixmap(self.pixmap)
                        self.t_preview.setPixmap(self.pixmap)

            except Exception as e:
                errorlog("<u_d03> " + str(e))

            try:

                def move_tab_custext(self):
                    tab_off = "QPushButton{font-size: 17px; color: rgb(120,120,120)}\nQPushButton:hover{color: rgb(255,255,255)}"
                    self.stacked_widget.setCurrentIndex(5)
                    self.wcii_button.setStyleSheet(tab_off)
                    self.clock_setting_button.setStyleSheet(tab_off)
                    self.text_setting_button.setStyleSheet(tab_off)
                    self.clock_info_button.setStyleSheet(tab_off)

                def t_mode_set_online(self):
                    uiniup('where_text', "online")
                    ciniup('where_text', 'online')
                    self.t_mode_online.setStyleSheet(wc.pb_t)
                    self.t_mode_offline.setStyleSheet(wc.pb_f)
                    self.t_mode_custom.setStyleSheet(wc.pb_f)
                    self.preview()


                def t_mode_set_offline(self):
                    uiniup('where_text', "offline")
                    ciniup('where_text', 'offline')
                    self.t_mode_online.setStyleSheet(wc.pb_f)
                    self.t_mode_offline.setStyleSheet(wc.pb_t)
                    self.t_mode_custom.setStyleSheet(wc.pb_f)
                    updatetext()
                    self.preview()

                def t_mode_set_custom(self):
                    uiniup('where_text', "custom")
                    ciniup('where_text', 'custom')
                    self.t_mode_online.setStyleSheet(wc.pb_f)
                    self.t_mode_offline.setStyleSheet(wc.pb_f)
                    self.t_mode_custom.setStyleSheet(wc.pb_t)
                    updatetext()
                    self.preview()
            except Exception as e:
                errorlog("<u_d04> " + str(e))

            try:
                def t_reflseh_set(self):
                    updatetext()
                    if self.already:
                        wcii_wallpaper()
                        self.pixmap = QPixmap(wc.showtemp).scaledToHeight(141)
                    else:
                        wcii_wallpaper(True)
                        self.pixmap = QPixmap(wc.preview).scaledToHeight(141)
                    self.preview()
                    #QMessageBox.about(self, "문구 업데이트 완료!", "문구를 서버에서 새로 불러왔어요!")

                def t_align_left_set(self):
                    uiniup("font_align", "left")
                    self.t_align_left.setStyleSheet(wc.pb_t)
                    self.t_align_center.setStyleSheet(wc.pb_f)
                    self.t_align_right.setStyleSheet(wc.pb_f)
                    self.preview()

                def t_align_center_set(self):
                    uiniup("font_align", "center")
                    self.t_align_left.setStyleSheet(wc.pb_f)
                    self.t_align_center.setStyleSheet(wc.pb_t)
                    self.t_align_right.setStyleSheet(wc.pb_f)
                    self.preview()

                def t_align_right_set(self):
                    uiniup("font_align", "right")
                    self.t_align_left.setStyleSheet(wc.pb_f)
                    self.t_align_center.setStyleSheet(wc.pb_f)
                    self.t_align_right.setStyleSheet(wc.pb_t)
                    self.preview()
            except Exception as e:
                errorlog("<u_d05> " + str(e))

            try:
                def custom_reflesh(self):
                    self.time_07.setText(tinidown(7))
                    self.time_08.setText(tinidown(8))
                    self.time_09.setText(tinidown(9))
                    self.time_10.setText(tinidown(10))
                    self.time_11.setText(tinidown(11))
                    self.time_12.setText(tinidown(12))
                    self.time_13.setText(tinidown(13))
                    self.time_14.setText(tinidown(14))
                    self.time_15.setText(tinidown(15))
                    self.time_21.setText(tinidown(21))
                    self.time_20.setText(tinidown(20))
                    self.time_18.setText(tinidown(18))
                    self.time_22.setText(tinidown(22))
                    self.time_17.setText(tinidown(17))
                    self.time_16.setText(tinidown(16))
                    self.time_19.setText(tinidown(19))
                    self.time_23.setText(tinidown(23))
                    self.time_00.setText(tinidown(0))
                    self.time_01.setText(tinidown(1))
                    self.time_02.setText(tinidown(2))
                    self.time_03.setText(tinidown(3))
                    self.time_04.setText(tinidown(4))
                    self.time_05.setText(tinidown(5))
                    self.time_06.setText(tinidown(6))

                def custom_apply_set(self):
                    custom_where = []
                    for i in range(0, 10):
                        custom_where.append("time_0"+str(i))
                    for i in range(10, 24):
                        custom_where.append("time_"+str(i))

                    countdown_text = 0
                    for i in custom_where:
                        custom_data = eval("self."+i+".text()")
                        tiniup(str(countdown_text), custom_data)
                        print(f"custom [{i}] => [{custom_data}]")
                        countdown_text = countdown_text + 1

                    updatetext()
                    if self.already:
                        wcii_wallpaper()
                        self.pixmap = QPixmap(wc.showtemp).scaledToHeight(141)
                    else:
                        wcii_wallpaper(True)
                        self.pixmap = QPixmap(wc.preview).scaledToHeight(141)

                def custom_reset_set(self):
                    reply = QMessageBox.question(self, '정말로 초기화 하실건가요?',
                                                 "초기화를 한 뒤에는 되돌릴 수 없습니다.",
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        shutil.copyfile(wc.dsource + "ctt.ini", wc.appctt)
                        self.custom_reflesh()

            except Exception as e:
                errorlog("<u_d06> " + str(e))

            try:

                def check_update(self):
                    self.url_update.setText("<p align=\"center\">업데이트 확인 중..<\"p>")
                    ver = vercheck(False)
                    if ver == None:
                        self.url_update.setText("<p align=\"center\">프로그램이 최신 버전이에요!<\"p>")
                    elif ver == False:
                        self.url_update.setText("<p align=\"center\">업데이트 체크에 실패했어요... 나중에 다시 시도해주세요.<\"p>")
                    else:
                        self.url_update.setText(
                            f"<html><head/><body><p align=\"center\"><a href=\"https://whatclockisit.xyz/beta/download.html\"><span style=\" text-decoration: underline; color:#6265e7;\">업데이트가 있어요! (최신 버전 : {ver})</span></a></p></body></html>")

                def check_log_set(self):
                    os.system("start %localappdata%/whatclockisit/log")

                def move_tab_goerror(self):
                    tab_on = "QPushButton{font-size: 17px; color: rgb(255,255,255)}\nQPushButton:hover{color: rgb(255,255,255)}"
                    tab_off = "QPushButton{font-size: 17px; color: rgb(120,120,120)}\nQPushButton:hover{color: rgb(255,255,255)}"
                    self.stacked_widget.setCurrentIndex(4)
                    self.wcii_button.setStyleSheet(tab_off)
                    self.clock_setting_button.setStyleSheet(tab_off)
                    self.text_setting_button.setStyleSheet(tab_off)
                    self.clock_info_button.setStyleSheet(tab_off)
            except Exception as e:
                errorlog("<u_d07> " + str(e))

            try:
                def apply(self):
                    updataini()
                    if self.already:
                        wcii_wallpaper()
                        self.pixmap = QPixmap(wc.showtemp).scaledToHeight(141)
                    else:
                        wcii_wallpaper(True)
                        self.pixmap = QPixmap(wc.preview).scaledToHeight(141)
                    self.pixmap = QPixmap(wc.showtemp).scaledToHeight(141)
                    self.c_preview.setPixmap(self.pixmap)
                    self.t_preview.setPixmap(self.pixmap)
                    QApplication.processEvents()

                def preview(self):
                    try:
                        wcii_wallpaper(True)
                        self.pixmap = QPixmap(wc.preview).scaledToHeight(141)
                        self.c_preview.setPixmap(self.pixmap)
                        self.t_preview.setPixmap(self.pixmap)
                        QApplication.processEvents()
                    except Exception as e:
                        errorlog("<u_d07.5 무시가능 > " + str(e))

                def killwcii(self, Form):
                    if alreadylive():
                        reply = QMessageBox.question(self, '지금몇시계를 종료하실 건가요?',
                                                     "지금몇시계가 코..하고 잘 시간인가요..?",
                                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if reply == QMessageBox.Yes:
                            with open(wc.ckill, "w") as f:
                                f.write("kill")
                            self.main_wcii_title.setText("<span style=\" font-size:24pt;\">너는 지금 지금몇시계를<br/>사용하지 않고 있어</span>")
                            self.main_wcii_info.setText("지금몇시계 잠 깨우기")
                            self.redbutton.setText("지금몇시계 켜기")
                            done = QMessageBox.information(self, "지금몇시계가 자러갔어요.", "나중에 또 봐요!")
                            stop_wallpaper()
                            self.already = False
                    else:
                        self.core_wakeup(Form)
            except Exception as e:
                errorlog("<u_d08> " + str(e))

            try:
                def core_wakeup(self):
                    print(alreadylive())
                    if not alreadylive():
                        print("지금몇시계 실행함")
                        os.system("start wc_core.exe")
                        self.main_wcii_title.setText("<span style=\" font-size:24pt;\">너는 지금 지금몇시계를 사용중이야</span>")
                        self.main_wcii_info.setText("지금몇시계 잠재우기")
                        self.redbutton.setText("지금몇시계 종료")
                        self.already = True
                    else:
                        print("이미 실행요청이 있었음")
                        self.killwcii(Form)

                def reset(self, Form):
                    reply = QMessageBox.question(self, '혹시 프로그램에 문제가 생겼나요..?',
                                                 "혹시 지금몇시계가 정상적으로 작동하지 않나요..?\n확인 버튼을 눌러서 데이터를 초기화 할 수 있습니다.",
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        with open(wc.ckill, "w") as f:
                            f.write("kill")
                        re = appdata_check(True, False)
                        if re == "error":
                            QMessageBox.information(self, "데이터 초기화 실패..", "다른 프로세스가 사용중입니다.. "
                                                                          "혹시 appdata와 관련된 작업이 있다면 종료후에 다시 시도해주세요!")
                        else:
                            QMessageBox.information(self, "데이터 초기화 완료!", "데이터 초기화가 완료되었습니다!\n"
                                                                         "프로그램이 종료됩니다! (다시 실행해주세요!)")
                        sys.exit(app.exec_())
            except Exception as e:
                errorlog("<u_d09> " + str(e))

            try:

                def goerror_where_setting(self): #디스코드로 답변
                    self.reply_discord.setStyleSheet(wc.pb_t)
                    self.reply_email.setStyleSheet(wc.pb_f)
                    self.reply_no.setStyleSheet(wc.pb_f)
                    self.how_reply_address = "discord"

                def goerror_where_core(self): #이메일로 답변
                    self.reply_discord.setStyleSheet(wc.pb_f)
                    self.reply_email.setStyleSheet(wc.pb_t)
                    self.reply_no.setStyleSheet(wc.pb_f)
                    self.how_reply_address = "email"

                def goerror_where_other(self): #답변을 원하지 않음
                    self.reply_discord.setStyleSheet(wc.pb_f)
                    self.reply_email.setStyleSheet(wc.pb_f)
                    self.reply_no.setStyleSheet(wc.pb_t)
                    self.how_reply_address = "no"
                    QMessageBox.information(self, "참고해주세요!", "답변 안함을 선택하셨더라도 오류를 해결, 등의 이유가 있다면 \n"
                                                             "디스코드 채널에 올라갈 수 있어요!\n\n"
                                                             "만약 자신만의 비밀이라서 아무도 모르게 하고 싶다면 및의 '자세한 내용'"
                                                             "칸에 '저만의 비밀이니 알리지 마세요'라고 적어주세요!")
            except Exception as e:
                errorlog("<u_d10> " + str(e))

            try:

                def gogoerror(self):
                    go_name = self.name_line.text()
                    go_email = self.email_line.text()
                    go_reply = self.how_reply_address
                    go_text = self.error_text.toPlainText()

                    if go_name == "":
                        QMessageBox.warning(self, "이름이 빠졌어요..", "이름을 입력해주세요...")
                        return None

                    if go_email != "":
                        if go_email.count('a') <= 0:
                            QMessageBox.warning(self, "뭔가 실수 하셨나요?", "올바른 이메일 형식이 아니에요..\n"
                                                                     "만약 이메일을 적고싶지 않다면 칸을 완전히 비워주세요.")
                            return None
                        elif go_email.count(".") <= 0:
                            QMessageBox.warning(self, "뭔가 실수 하셨나요?", "올바른 이메일 형식이 아니에요..\n"
                                                                     "만약 이메일을 적고싶지 않다면 칸을 완전히 비워주세요")
                            return None

                    if go_email == "":
                        if go_reply == "email":
                            QMessageBox.warning(self, "뭔가 실수 하셨나요?", "답변 방식으로 이메일을 선택했지만, "
                                                                     "이메일을 적지 않으셨네요..\n\n얼른 적어주세요!")
                            return None

                    reply = QMessageBox.question(self, '오류를 보내실 준비가 되셨나요?',
                                                 "오류를 제보할 준비가 되셨나요? 마음의 준비를 단단히 해주세요.\n\n오류를 Hyuns에게 알리는 동안 시간이 조금 걸릴 수 있습니다!",
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        aw = goerror(go_name, go_email, go_text, go_reply)
                        if aw == "error":
                            QMessageBox.warning(self, "오류 보내기를 실패했어요..", "오류 보내기를 실패했어요.. 인터넷 상태를 확인해주세요!\n\n"
                                                                         "혹시 인터넷이 올바르게 연결 되있음에서 이 창이 뜬다면\n"
                                                                         "제 이메일인 hyuns@hyuns.space 또는 지금몇시계 디스코드에 오류를 제보해주세요!\n\n" + aw[5:])
                        else:
                            QMessageBox.information(self, "오류를 보내는 데 성공했어요!", "오류 제보를 성경적으로 완료했어요!")
            except Exception as e:
                errorlog("<u_d11> " + str(e))

            def retranslateUi(self, Form): #글자
                _translate = QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "지금몇시계"))
                self.main_name.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">지금몇시계</span></p></body></html>"))
                self.wcii_button.setText(_translate("Form", "지금몇시계"))
                self.clock_setting_button.setText(_translate("Form", "시계 설정"))
                self.text_setting_button.setText(_translate("Form", "문구 설정"))
                self.clock_info_button.setText(_translate("Form", "시계 정보"))
                self.c_preview_label.setText(_translate("Form", "미리보기"))
                self.c_fsize_label.setText(_translate("Form", "글자 크기 (px) :"))
                self.c_pos_label.setText(_translate("Form", "시계 위치 :"))
                self.c_fset_label.setText(_translate("Form", "폰트 설정 :"))
                self.c_wallset_label.setText(_translate("Form", "배경화면 설정: "))
                self.c_pos_left.setText(_translate("Form", "왼쪽"))
                self.c_pos_center.setText(_translate("Form", "가운데"))
                self.c_pos_right.setText(_translate("Form", "오른쪽"))
                self.c_pos_self.setText(_translate("Form", "수동"))
                self.c_fset_set.setText(_translate("Form", "폰트 선택하기"))
                self.c_fset_def.setText(_translate("Form", "기본 폰트로"))
                self.c_wallset_set.setText(_translate("Form", "이미지 선택하기"))
                self.c_wallset_def.setText(_translate("Form", "단색 배경 선택하기"))
                self.c_apply.setText(_translate("Form", "적용하기"))
                self.c_pos_self_label.setText(_translate("Form", "가로 / 세로"))
                self.c_fcolor_label.setText(_translate("Form", "글자 색 : "))
                self.c_fcolor_pick.setText(_translate("Form", "글자 색 정하기"))
                self.t_apply.setText(_translate("Form", "적용하기"))
                self.t_preview_label.setText(_translate("Form", "미리보기"))
                self.t_mode_online.setText(_translate("Form", "서버에서 받아오기"))
                self.t_custext_set.setText(_translate("Form", "커스텀 문구 설정하기"))
                self.t_custext_label.setText(_translate("Form", "커스텀 문구"))
                self.t_mode_label.setText(_translate("Form", "문구 불러오기"))
                self.t_mode_offline.setText(_translate("Form", "오프라인 문구"))
                self.t_reflesh_label.setText(_translate("Form", "문구 새로고침"))
                self.t_reflesh_text.setText(_translate("Form", "문구 새로 받아오기 (온라인)"))
                self.t_align_left.setText(_translate("Form", "왼쪽"))
                self.t_align_center.setText(_translate("Form", "가운데"))
                self.t_align_right.setText(_translate("Form", "오른쪽"))
                self.t_align_label.setText(_translate("Form", "문구 정렬"))
                self.t_mode_custom.setText(_translate("Form", "커스텀 문구"))
                self.info_label.setText(_translate("Form", "<html><head/><body>"
                                                           "<p align=\"center\"><span style=\" font-size:11pt;\">지금몇시계</span></p>"
                                                           "<p align=\"center\"><span style=\" font-size:11pt;\">버전 : Beta 0.7</span></p>"
                                                           "<p align=\"center\"><span style=\" font-size:11pt;\">제작자 : 혀느현스 (Hyuns)</span></p>"
                                                           "<p align=\"center\"><span style=\" font-size:11pt;\">지금몇시계 웹 : </span>"
                                                           "<a href=\"https://whatclockisit.xyz\"><span style=\" text-decoration: underline; color:#6265e7;\">whatclockisit.xyz</span></a></p>"
                                                           "<p align=\"center\"><span style=\" font-size:11pt;\">지금몇시계 디스코드 : </span>"
                                                           "<a href=\"https://discord.gg/AwYVNNA\"><span style=\" text-decoration: underline; color:#6265e7;\">https://discord.gg/AwYVNNA</span></a></p>"
                                                           "</body></html>"))

                self.checkupdate_button.setText(_translate("Form", "업데이트 확인하기"))
                self.goerror_button.setText(_translate("Form", "오류 보내기"))
                self.reset_data.setText(_translate("Form", "데이터 초기화"))
                self.goerror_label.setText(_translate("Form", " 앗..무슨 에러가 발생했나요..? 오류를 보내주면 Hyuns가 해결할 거에요!"))
                self.name_label.setText(_translate("Form", "당신의 이름이 무엇인가요? : "))
                self.email_label.setText(_translate("Form", "이메일 주소를 알려주세요! : "))
                self.how_reply.setText(_translate("Form", "어떻게 답변을 드릴까요?"))
                self.reply_email.setText(_translate("Form", "작성한 이메일로"))
                self.reply_discord.setText(_translate("Form", "디스코드 채널에"))
                self.reply_no.setText(_translate("Form", "답변을 원하지 않음"))
                self.error_label.setText(_translate("Form", "자세한 내용을 알려주세요! (선택)"))
                self.goerror_button_2.setText(_translate("Form", "오류 보내기"))
                self.check_log_button.setText(_translate("Form", "로그 확인하기"))
                self.cus_label.setText(_translate("Form", "커스텀 문구 만들기!"))
                self.time_07_label.setText(_translate("Form", "아침 7시 (07시)"))
                self.time_08_label.setText(_translate("Form", "아침 8시 (08시)"))
                self.time_09_label_2.setText(_translate("Form", "아침 9시 (09시)"))
                self.time_10_label.setText(_translate("Form", "오전 10시 (10시)"))
                self.time_11_label.setText(_translate("Form", "오전 11시 (11시)"))
                self.time_12_label.setText(_translate("Form", "점심 12시 (12시)"))
                self.time_13_label.setText(_translate("Form", "오후 1시 (13시)"))
                self.time_14_label.setText(_translate("Form", "오후 2시 (14시)"))
                self.time_15_label.setText(_translate("Form", "오후 3시 (15시)"))
                self.time_16_label.setText(_translate("Form", "오후 4시 (16시)"))
                self.time_17_label.setText(_translate("Form", "오후 5시 (17시)"))
                self.time_18_label.setText(_translate("Form", "저녁 6시 (18시)"))
                self.time_19_label.setText(_translate("Form", "저녁 7시 (19시)"))
                self.time_20_label.setText(_translate("Form", "저녁 8시 (20시)"))
                self.time_21_label.setText(_translate("Form", "저녁 9시 (21시)"))
                self.time_22_label.setText(_translate("Form", "밤 10시 (22시)"))
                self.time_23_label.setText(_translate("Form", "밤 11시 (23시)"))
                self.time_00_label.setText(_translate("Form", "밤 12시 (00시)"))
                self.time_01_label.setText(_translate("Form", "새벽 1시 (01시)"))
                self.time_02_label.setText(_translate("Form", "새벽 2시 (02시)"))
                self.time_03_label.setText(_translate("Form", "새벽 3시 (03시)"))
                self.time_04_label.setText(_translate("Form", "새벽 4시 (04시)"))
                self.time_05_label.setText(_translate("Form", "아침 5시 (05시)"))
                self.time_06_label.setText(_translate("Form", "아침 6시 (06시)"))

                self.text_apply.setText(_translate("Form", "저장하기"))
                self.text_cancel.setText(_translate("Form", "취소하기"))
                self.text_reset.setText(_translate("Form", "기본 문구로 초기화"))
        except Exception as e:
            errorlog("<u_02> " + str(e))
except Exception as e:
    errorlog("<u_03> " + str(e))

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        Form = QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
    except Exception as e:
        errorlog("<u_04> " + str(e))

