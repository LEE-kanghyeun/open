# https://ybworld.tistory.com/39?category=929856
# https://investox.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A9%80%ED%8B%B0%EC%93%B0%EB%A0%88%EB%93%9C-%EC%98%A4%EB%A5%98%EC%97%86%EC%9D%B4-%EC%A2%85%EB%A3%8C%ED%95%98%EA%B8%B0-QThread-GUI
# http://lvzuufx.blogspot.com/2015/10/qt_21.html

# python 내장 'threading' vs pyqt 내장 'Qthread'
# threading은 gui가 종료되어도 하나의 쓰레드로서 자신의일을 마칠때까지 쓰레드가 돌아가는반면에,
# QThread는gui가꺼지면, 같이쓰레드가종료됩니다.
# https: // coding - yoon.tistory.com / 46?category = 830190


###  : 불안정함. 실제로 main loop간의 시간적 term이 필요함
###  : main loop 안에서 thread 여러번 호출은 안정적임.


import time
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import * #QThread 클래스 선언하기, QThread 클래스를 쓰려면 QtCore 모듈을 import 해야함.

form_class = uic.loadUiType("Qthread_pyqt2.ui")[0]


class Thread1(QThread):
#초기화 메서드 구현
    def __init__(self, parent = None): #parent는 WndowClass에서 전달하는 self이다.(WidnowClass의 인스턴스)
        super().__init__(parent)
        self.parent = parent #self.parent를 사용하여 WindowClass 위젯을 제어할 수 있다.


    def run(self):  #쓰레드로 동작시킬 함수 내용 구현
        print('11')
        self.parent.textBrowser.append("경주마1이 출발하였습니다.")
        for i in range(20):
            # print('1')
            self.parent.textBrowser.append("경주마1이" + str(i) + "km째 달리고 있습니다.")
            # print(self.isFinished())
            time.sleep(0.2)

        # self.parent.textBrowser.append("경주마1이 결승지에 도착하였습니다.")
        self.stop()

    def stop(self):          ### 이게 없으면, Thread가 중복되거나, 오류발생할수 있음 (재실행시 실행안됨 등)
                             # 멀티쓰레드를 종료하는 메소드 : stop, quit, wait 모두 Qthread 내장함수
        self.quit()
        # print('wait 전')
        # self.wait(5000)  # 3초 대기 (바로 안꺼질수도 있으므로)
        # print('wait 후')
        # while self.isFinished() is True :
        #      print(self.isFinished())
        self.__del__()

    def isfinished(self):
        return self.isFinished()

    def __del__(self):
        print(self.__class__, '삭제')


class Thread2(QThread):
#초기화 메서드 구현
    def __init__(self, parent = None): #parent는 WndowClass에서 전달하는 self이다.(WidnowClass의 인스턴스)
        super().__init__(parent)
        self.parent = parent #self.parent를 사용하여 WindowClass 위젯을 제어할 수 있다.


    def run(self):  #쓰레드로 동작시킬 함수 내용 구현
        self.parent.textBrowser.append("경주마2가 출발하였습니다.")
        for i in range(20):
            # print('2')
            self.parent.textBrowser.append("경주마2가" + str(i) + "km째 달리고 있습니다.")
            time.sleep(0.2)

        self.parent.textBrowser.append("경주마2이 결승지에 도착하였습니다.")
        self.stop()

    def stop(self):          ### 이게 없으면, Thread가 중복되거나, 오류발생할수 있음 (재실행시 실행안됨 등)
                             # 멀티쓰레드를 종료하는 메소드 : stop, quit, wait 모두 Qthread 내장함수
        self.quit()
        # self.wait(5000)  # 3초 대기 (바로 안꺼질수도 있으므로)
        # while self.isFinished():
        #     pass
        self.__del__()

    def isfinished(self):
        return self.isFinished()

    def __del__(self):
        print(self.__class__, '삭제')

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.thread_list = []
        self.thread_finished_list = []


        # 각 버튼에 대한 함수 연결
        self.runButton1.clicked.connect(self.actionFunction1)
        self.runButton2.clicked.connect(self.actionFunction2)

    def actionFunction1(self):
        h1 = Thread1(parent=self)   ## Thread (Worker)의 객체화
        self.thread_list.append(h1)
        h1.start()               ########### 중요 ########## : h1.run()이 아니라 start()인 이유는 QThread 는 자체의 이벤트 루프를 가지고 있다.
                                                        # 따라서 QThread.start() 를 호출하면 자동으로 QThread::run() 이 실행되어 이벤트 루프에 진입하게 된다
                                                        # h1.run()으로 실행하면, 병렬처리가 안됨 (Thread1 클래스 실행하는 동안, 메인 윈도우 멈춤)

    def actionFunction2(self):
        h2 = Thread2(parent=self)   ## Thread (Worker)의 객체화
        self.thread_list.append(h2)
        h2.start()              ########### 중요 ########## : h2.run()이 아니라 start()인 이유는 QThread 는 자체의 이벤트 루프를 가지고 있다.
                                                        # 따라서 QThread.start() 를 호출하면 자동으로 QThread::run() 이 실행되어 이벤트 루프에 진입하게 된다
                                                        # h2.run()으로 실행하면, 병렬처리가 안됨 (Thread1 클래스 실행하는 동안, 메인 윈도우 멈춤)



    def closeEvent(self, event):   ##
        quit_msg = "Are you sure you want to exit the program?"
        reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # 멀티쓰레드를 종료하는 stop 메소드를 실행함

            for i in self.thread_list:
                self.thread_finished_list.append(i.isfinished())

            print(self.thread_finished_list)
            if sum(self.thread_finished_list) == len(self.thread_list):
                event.accept()
        else:
            event.ignore()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

#
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5 import uic
# import sys
#
# form_class = uic.loadUiType("Qthread_pyqt2.ui")[0]
#
# class Worker(QThread):
#
#     def __init__(self, parent):
#         print('2')
#         super().__init__(parent)
#         print('3')
#         self.parent = parent
#         print('4')
#         self.power = True                           # run 매소드 루프 플래그
#         self.run()
#
#     def run(self):
#         i=0
#         while self.power:
#             # print(i)
#             self.parent.textBrowser.append("경주마1이" + str(i) + "km째 달리고 있습니다.")
#             i += 1
#
#     def stop(self):
#         # 멀티쓰레드를 종료하는 메소드
#         self.power = False
#         self.quit()
#         self.wait(3000)  # 3초 대기 (바로 안꺼질수도)
#
#
# class MainWindow(QMainWindow, form_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.runButton1.clicked.connect(self.actionFunction1)
#
#         # thread start
#     def actionFunction1(self):
#         print('1')
#         self.worker = Worker(parent = self)
#         print('1')
#         self.worker.start()
#
#     def closeEvent(self, event):
#         quit_msg = "Are you sure you want to exit the program?"
#         reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)
#
#         if reply == QMessageBox.Yes:
#             # 멀티쓰레드를 종료하는 stop 메소드를 실행함
#             self.worker.stop()
#             event.accept()
#         else:
#             event.ignore()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainWindow = MainWindow()
#     mainWindow.show()
#     app.exec_()
#
#
#
