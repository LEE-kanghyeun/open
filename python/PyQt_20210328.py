import sys
from PyQt5.QtWidgets import *

############### 윈도우 창 출력하기 ###################

app = QApplication(sys.argv)  # QApplication은 어플리케이션 객체를 호출함, 상세 설명 : https://cakel.tistory.com/entry/QApplication-%EC%86%8C%EA%B0%9C
# 괄호 속 sys.argv는 단순히 LIST[STR] 형태를 제공하기 위한 것으로, QApplication이 괄호 안에 LIST[STR] 형태를 필요로 한다.
# 아래와 같이 실행해도 똑같이 실행됨.
# a=['a']
# sys.argv란? -> print(sys.argv)   결과값 :  ['C:/Users/6509504/python_v_main/PYQT.PY.py']
# app = QApplication(sys.argv)


label = QLabel("Hello PyQt")  # GUI 창 제목
label.show()   # GUI 보여주기 실행

app.exec_() #아래 설명 참조
# app이라는 객체에 exec_ 메서드를 호출하면 프로그램은 이벤트 루프(event loop)에 진입
# 이벤트 루프란 무한 반복하면서 이벤트를 처리하는 상태를 의미합니다. 파이썬 코드는 위에서 밑으로 순서대로 실행된 후 프로그램이 종료되므로,
# 이 부분에서 코드실행이 지속되고 아래 부분으로 안넘어감. 따라서 이벤트 관련 윈도우가 화면에 계속 출력됩니다.
# 앞에서 작성한 대부분의 TUI 기반의 프로그램은 프로그램이 실행된 후 종료됐지만 GUI 프로그램은 사용자가 윈도우를 닫기 전까지는 계속 실행된 상태로 남아 있습니다.
# 이처럼 프로그램이 종료되지 않고 실행 상태로 계속 남아 있을 수 있는 이유가 바로 이벤트 루프 때문입니다.
# 이벤트 루프는 기본적으로 무한 루프 구조이며, 무한 루프 상태에서 사용자가 발생한 이벤트를 그때그때 처리해줍니다.
# 예를 들어, 사용자가 윈도우를 클릭하면 ‘클릭 이벤트’가 발생하는데 이때 이벤트 루프에서 ‘클릭 이벤트’를 처리 해주는 것입니다.





######### 윈도우 창 사이즈 조정하기  ###########

## 클래스로 setWindowTitle, setGeometry 설정 추가 ##
import sys
from PyQt5.QtWidgets import *
class MyWindow(QMainWindow): ## QMainWindow에 대해 상속받기
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")  ## 윈도우 타이틀을 변경
        self.setGeometry(300, 300, 300, 400) ## 윈도우 크기 변경


if __name__ == "__main__":    ## 해당 모듈에서 직접 실행할때만, if 아래 구문이 실행되도록 함
    #  __name__ : 모듈의 이름을 의미함,   print(__name__)  : 현재 모듈 이름 출력
    #  모듈이 현재 실행프로그램일 경우(인터프리터에서 직접 실행),  print(__name__) -> "__main__"
    #  모듈이 다른 실행프로그램일 경우(import되어 사용되는 경우),   print(__name__) -> "해당 파일 이름 (ex. execute_test)"
    #
    #  예제 : import execute_test.func()  // 아래의 execute_test.py 파일에 대해 import하여 사용하는 경우
    #
    #  //execute_test.py
    # def func():
    #     print("function working")
    #
    # if __name__ == "__main__":
    #     print("직접 실행")
    #     print(__name__)
    # else:
    #     print("임포트되어 사용됨")
    #     print(__name__)print(__name__)

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()





################### 이벤트 처리하기 ##########################
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()                         ## 윈도우 제목 / 사이즈 설정
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 400)

        btn1 = QPushButton("Click me", self)     ## 푸쉬 타입 버튼 생성 + "Click me" 이름 지정) + self로 객체화
        btn1.move(100, 200)                        ## 푸쉬 타입 버튼 위치 이동 (x축 , y축)  - (0,0)은 상단 좌측
        btn1.clicked.connect(self.btn1_clicked)  ## 버튼을 클릭했을때 : btn1.clicked
                                                 ## 버튼을 클릭했을때의 이벤트 연결 : btn1.clicked.connect  -> (괄호) 안 내용은 btn1_clicked 메소드로 연결시킴

    def btn1_clicked(self):
        QMessageBox.about(self, " push the button and return", "clicked")  # 단순 about 박스 출력   ( self, (box name), (description) )

        ## 옵션 추가에 대한 팝업 창 생성  (버튼은 no / yes / cancel 설정)
        option = QMessageBox.question(self, "QMessageBox", "Do you want to add option?", QMessageBox.No | QMessageBox.Yes | QMessageBox.Cancel)

        if option == QMessageBox.Yes:   ## 옵션 추가에 대해 yes를 눌렀을시, 아래 메시지 박스 발생시킴
            QMessageBox.information(self, "QMessageBox", "Option Added")
#  QMessageBox : 메시지 박스 팝업 뜨게 하기
#  상세 설명 : https://m.blog.naver.com/PostView.nhn?blogId=huntingbear21&logNo=221825482802&proxyReferer=https:%2F%2Fwww.google.com%2F
#  박스 종류 : about / warning / critical / question 등 존재
#

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()






####################### Qt designer ########################
# : 아나콘다 배포판에는 C:\Anaconda3\Library\bin 디렉터리에 designer.exe 파일이 존재  -> 실행하면 디자인을 위한 UI 이미 구성되어 있음 (간편함)
#  ctrl + R 은 미리 보기 단축키
# Qt designer로 UI 완성후 저장  ->  저장된 파일은 xml 코드이므로, python으로 불러올 함수 필요함 ( 바로 uic )


import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic    ## xml 코드를 python으로 불러올 함수

form_class = uic.loadUiType(r"C:\Users\com\Desktop\main_window.ui")[0]   ## Qt designer로 완성된 'main_window.ui' 파일을 python으로 불러옴

print(type(form_class))  # : form_class의 타입은 클래스

class MyWindow(QMainWindow, form_class):   # QMainWindow와 form_class 상속받기
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # form_class 내 메소드,   setupui() 괄호안 매개변수는 누구를 부모로 할것인지 전달하게 함
                            # MyWindow가 메인 윈도우이므로, 자신이 부모여야하므로 self(자기자신)를 매개변수로 전달함
                            # 만약에 self.setupUi(self)로 선언하지 않는다면, 아래 self.pushbutton에 대해서 MyWindow가 pushbutton이 뭔지 모른다고 출력함
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        QMessageBox.about(self, "message", "clicked")
        option = QMessageBox.question(self, "QMessageBox", "Do you want to add option?",
                                      QMessageBox.No | QMessageBox.Yes | QMessageBox.Cancel)

        if option == QMessageBox.Yes:  ## 옵션 추가에 대해 yes를 눌렀을시, 아래 메시지 박스 발생시킴
            QMessageBox.information(self, "QMessageBox", "Option Added")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()





###################################  기본 위젯  #####################################


##################### QCoreApplication.instance().quit #################  : 객체 호출하여 종료시키기
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

app = QApplication(sys.argv)

label = QLabel("Hello PyQt")  # GUI 창 제목
label.move(200, 200)    # 없으면 기본 (0,0)에 위치함
label.show()   # GUI 보여주기 실행
btn1 = QPushButton("닫기")
btn1.move(200, 300)
btn1.show()
btn1.clicked.connect(QCoreApplication.instance().quit)
# QCoreApplication.instance()를 이용하면 아래 app이라는 변수가 바인딩하고 있는 동일한 객체를 얻어올 수 있습니다.
# app이 바인딩하고 있는 객체는 QApplication 클래스의 인스턴스이며, instance() 메서드는 현재 인스턴스를 반환합니다.
# 또한 해당 객체는 quit이라는 메서드를 포함하고, 버튼을 클릭했을 때 QApplication이 제공하는 quit 메서드를 호출하도록 연결함으로써 메인 윈도우가 종료되는 것입니다.
# 이 예제에서 발신자는 푸시버튼 (btn1)이고, 수신자는 어플리케이션 객체 (app)입니다.

app.exec_()


######################## QPushButton #######################  : 버튼 역할
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_UI()   ## setUi가 아님, 아래 메소드 함수임, __init__ 즉, 초기부터 setup_UI라는 메소드에 진입하라는 뜻

    def setup_UI(self):
        btn1 = QPushButton("닫기", self)
        btn1.move(20, 20)
        btn1.clicked.connect(QCoreApplication.instance().quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()





######################## QLabel #######################  : 텍스트 표시해줌

import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 400, 300, 150)    # 800 : 모니터에서 메인 윈도우 상자의 위치를 정함, 위치는 좌측 상단 꼭지점을 기준으로 함, 800은 x좌표
                                                # 400 : 모니터에서 메인 윈도우 상자의 위치를 정함, 위치는 좌측 상단 꼭지점을 기준으로 함, 400은 y좌표
                                                # 300 : 상자의 크기를 지정함, 300은 x축 너비
                                                # 150 : 상자의 크기를 지정함, 150은 y축 높이, 윈도우 좌표 설명사이트 = https://wikidocs.net/21874
        textLabel = QLabel("Message: ", self)  ## 상자 내에 라벨 'message:'로 표시
        textLabel.move(20, 20)

        self.label = QLabel("1", self)       ## 생성한 위젯을 클래스 내의 다른 메서드(setupUI가 아닌)에서 참조할 때는 변수 이름에 self를 붙여야 하고
        self.label.move(80, 20)              ## 그렇지 않은 경우에는 self를 붙이지 않는다
        self.label.resize(150, 30)           ## self.label은 setupUI 메서드뿐 아니라 btn1_clicked와 btn2_clicked라는 메서드에서도 사용함.
                                             ## textLabel은 setupUI 메서드에서만 사용하고 더는 참조되지 않기 때문에 self를 붙이지 않아도 됨
                                             ## 현재는 self.label 을 '1' 표현하게끔 해놓았지만, 아래 btn1_clicked에 진입하게되면 해당 위치의 텍스트가
                                             ## "버튼이 클릭되었습니다."로 바뀌게됨
        btn1 = QPushButton("Click", self)
        btn1.move(20, 60)
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton("Clear", self)
        btn2.move(140, 60)
        btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        self.label.setText("버튼이 클릭되었습니다.")   ## self.label의 문자를 "버튼이 클릭되었습니다."로 변경

    def btn2_clicked(self):
        self.label.clear()   ## ## self.label의 문자를 꺠끗하게 clear시킴 (삭제)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()






######################## QLineEdit #######################  : 한 줄의 텍스트를 입력할 수 있는 위젯


import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 400, 300, 400)

        # Label
        label = QLabel("종목코드", self)
        label.move(20, 80)

        # LineEdit1
        self.lineEdit1 = QLineEdit("", self)   ## QLineEdit은 입력창을 의미함. ""는 입력창을 빈칸으로 놔두라는 뜻임, 만약 "1"로 한다면 입력창에 1이 처음부터 채워져있음
        self.lineEdit1.move(80, 80)
        self.lineEdit1.textChanged.connect(self.lineEditChanged)  ## textChanged는 입력 창에 삽입/삭제 등으로 변화가 생겼을때를 의미하며
                                                                  ## .connect를 통해 텍스트가 변화되면  객체의 lineEditChanged 메소드로 이동됨
        self.lineEdit1.returnPressed.connect(self.lineEditChanged) ## returnPressed는 입력 창에 enter까지 쳐야 변화를 인식함.


        # # StatusBar               ->  StatusBar를 self.statusBar와 같이 객체의 속성으로 지정하려면 이런식으로 구성할수 있다.
        # self.statusBar = QStatusBar(self)    // 객체의 QStatusBar에 대해  self.statusBar를 대입함.
        # # <QStatusBar 주요 메서드>
        # showMessage( )	문자열을 상태바에 출력합니다.
        # currentMessage( )	상태바에 출력된 현재 메시지를 얻어옵니다.
        # clearMessage( )	상태바에 출력된 메시지를 지웁니다.

        # self.setStatusBar(self.statusBar)  // self.setStatusBar로 StatusBar가 무엇인지 지정해줌 , 여기서는 self.statusBar

    def lineEditChanged(self):
        self.statusBar().showMessage(self.lineEdit1.text())
        # # 메인 윈도우는 메뉴 바, TOOL 바 , STATUS 바, WIDGET(DOCK & CENTRAL)로 이루어져있다.
        # # 메인 윈도우의 레이아웃 설명 =   https: // wikidocs.net / 21928



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()







######################## QRadioButton 과  QGroupBox #######################
# QRadioButton: 사용자로부터 여러 가지 옵션 중 하나를 입력받을 때 사용
# QGroupBox : 네모 박스 형태의 경계선을 만드는 데 사용 (제목 삽입 가능)

import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        groupBox = QGroupBox("시간 단위", self)
        groupBox.move(10, 10)      # 위치 조정
        groupBox.resize(280, 80)   # 크기를 조절하기 위해 resize 메서드를 호출

        self.radio1 = QRadioButton("일봉", self)
        self.radio1.move(20, 20)   # groupBox 안에 들어가도록, 위치 조정
        self.radio1.setChecked(True)  # 해당 항목(radio1)이 처음부터 체크되어서 출력되도록 설정 (FALSE이면 선택안되어 있음)
        self.radio1.clicked.connect(self.radioButtonClicked)

        self.radio2 = QRadioButton("주봉", self)
        self.radio2.move(20, 40)
        self.radio2.clicked.connect(self.radioButtonClicked)

        self.radio3 = QRadioButton("월봉", self)
        self.radio3.move(20, 60)
        self.radio3.clicked.connect(self.radioButtonClicked)

        self.statusBar = QStatusBar(self)  ## 객체의 QStatusBar에 대해  self.statusBar를 대입함.
        self.setStatusBar(self.statusBar)  ## self.setStatusBar로 StatusBar가 무엇인지 지정해줌 , 여기서는 self.statusBar

    def radioButtonClicked(self):
        msg = ""
        if self.radio1.isChecked():   ## radio1 선택 되어지면,
            msg = "일봉"
        elif self.radio2.isChecked(): ## radio2 선택 되어지면,
            msg = "주봉"
        else:
            msg = "월봉"              ## 그 외 선택 되어지면,
        self.statusBar.showMessage(msg + "선택 됨")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()






######################## QCheckBox #######################
# : QCheckBox는 여러 옵션 중 하나만 선택할 수 있었던 QRadioButton과 달리 여러 옵션을 동시에 선택할 수 있음


import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        self.checkBox1 = QCheckBox("5일 이동평균선", self)
        self.checkBox1.move(10, 20)
        self.checkBox1.resize(150, 30)  ## checkBox1의 크기 지정
        self.checkBox1.stateChanged.connect(self.checkBoxState)  ## stateChanged : 상태 변화 감지 :

        self.checkBox2 = QCheckBox("20일 이동평균선", self)
        self.checkBox2.move(10, 50)
        self.checkBox2.resize(200, 30) ## checkBox2의 크기 지정
        self.checkBox2.stateChanged.connect(self.checkBoxState)

        self.checkBox3 = QCheckBox("60일 이동평균선", self)
        self.checkBox3.move(10, 80)
        self.checkBox3.resize(150, 30) ## checkBox3의 크기 지정
        self.checkBox3.stateChanged.connect(self.checkBoxState)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def checkBoxState(self):
        msg = ""
        if self.checkBox1.isChecked() == True:   ## 중복 체크가 가능하므로, 모두 IF 문으로 구성
            msg += "5일 "                        ## 체크시, msg에 문구 더하기
        if self.checkBox2.isChecked() == True:
            msg += "20일 "
        if self.checkBox3.isChecked() == True:
            msg += "60일 "
        self.statusBar.showMessage(msg) # 이벤트 발생시, 코드가 위에서부터 아래로 실행되므로, 나중에 선택되었더라도
                                        # 윗쪽에 위치한 코드인 '5일'이 '20일', '60일' 보다 항상 statusBar 앞쪽에 표시된다. (주의)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()




######################## QCheckBox #######################
# : 사용자로부터 정숫값을 입력받을 때 사용 (입력창 존재), 화살표를 이용하여 값을 가감 (화살표 존재)

import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        label = QLabel("매도수량: ", self)  ## 라벨 쓰기
        label.move(10, 20)

        ## spinBox 쓰기
        self.spinBox = QSpinBox(self)  ## QSpinBox로 객체 속성화 하기, 객체 속성화 잉름은 spinBox
        self.spinBox.move(70, 25)    ## 위치 지정
        self.spinBox.resize(80, 22)  ## 크기 지정
        self.spinBox.setValue(10)    ## 입력창 초기값 설정해주기 - 초기값: 10,   설정한하면 초기값은 0으로 설정됨
        self.spinBox.setSingleStep(10)  ## 화살표 스텝 정해주기 - step: 10,   default : 1
        self.spinBox.setMinimum(1)    ## spinBox 최소값 정해주기 - 최소값 : 1  ,   default : 0
        self.spinBox.setMaximum(1000)  ## spinBox 최대값 정해주기 - 최대값 : 1000  ,   default : 무한대
        self.spinBox.valueChanged.connect(self.spinBoxChanged)  ## spinBox의 값이 바뀌면 self.spinBoxChanged 메소드로 연결

        self.statusBar = QStatusBar(self)   ## statusBar 객체 속성화 하기
        self.setStatusBar(self.statusBar)   ## setStatusBar로 Bar 셋하기

    def spinBoxChanged(self):
        val = self.spinBox.value()   ## self.spinBox의 값을 val이라는 변수로 저장
        msg = '%d 주를 매도합니다.' % val  ## msg 값  val 이용하여 설정하기
        self.statusBar.showMessage(msg)   ## statusBar에 표현하기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()





########################  QTableWidget (1)  #######################
# : 행과 열로 구성된 2차원 포맷 형태의 데이터를 표현

import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        self.tableWidget = QTableWidget(self)   ## QTableWidget(self)로 위젯테이블 설정 - 객체 속성으로 지정, 이름은 self.tableWidget
        self.tableWidget.resize(290, 290)    ## 크기 지정
        self.tableWidget.setRowCount(2)   ## 행 갯수 지정 : 2
        self.tableWidget.setColumnCount(2)  ## 열 갯수 지정 : 2
        self.setTableWidgetData() ## 메소드 연결

    def setTableWidgetData(self):
        self.tableWidget.setItem(0, 0, QTableWidgetItem("(0,0)"))  ## setItem으로 테이블 값 입력
        self.tableWidget.setItem(0, 1, QTableWidgetItem("(0,1)"))  ## 첫번째 인자 : 행 인덱스
        self.tableWidget.setItem(1, 0, QTableWidgetItem("(1,0)"))  ## 두번째 인자 : 열 인덱스
        self.tableWidget.setItem(1, 1, QTableWidgetItem("(1,1)"))  ## 세번째 인자 : 입력 내용, - 내용은 아래와 같음
        # QTableWidgetItem("(1,1)")으로 입력시, (1,1)로 입력됨  - QTableWidgetItem은 괄호 안 내용을 입력값으로 지정해주는 역할
        # QTableWidget에 아이템으로 삽입하려면 먼저 데이터를 이렇게 QTableWidgetItem 객체로 만들어야함.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()




########################  QTableWidget (2)  #######################
# : 행과 열로 구성된 2차원 포맷 형태의 데이터를 표현,  -  주식 데이터 표현해보기


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

kospi_top5 = {
    'code': ['005930', '015760', '005380', '090430', '012330'],
    'name': ['삼성전자', '한국전력', '현대차', '아모레퍼시픽', '현대모비스'],
    'cprice': ['1,269,000', '60,100', '132,000', '414,500', '243,500']
}
column_idx_lookup = {'code': 0, 'name': 1, 'cprice': 2}

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290, 290)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  ## 편집에 대해 설정 하기 (설정사항 아래 참조)
        ## QAbstractItemView.NoEditTriggers : 사용자가 QTableWidget의 아이템 항목을 수정할 수 없도록 설정

        self.setTableWidgetData()

    def setTableWidgetData(self):
        column_headers = ['종목코드', '종목명', '종가']
        self.tableWidget.setHorizontalHeaderLabels(column_headers) ## column에 대한 라벨(인덱스 명칭)을 설정,
                                                       ## row에 대한 라벨을 설정할 때는 setVerticalHeaderLabels 메서드를 사용

        for k, v in kospi_top5.items():  ## kospi_top5.items()에서 k: key (ex 'code'), v : value (ex '삼성전자')
            col = column_idx_lookup[k]   ## print(column_idx_lookup)의 결과값 : {'code': 0, 'name': 1, 'cprice': 2}

            for row, val in enumerate(v):     ## value에 대해 index(row)와 value(val)를 뽑아냄
                item = QTableWidgetItem(val)  ## val 값을 테이블 위젯의 입력값으로 지정함 - 위의 QTableWidgetItem("(0,0)")처럼
                if col == 2:
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)  ## 종가는 우측 정렬로 표현 (default : 좌측 정렬)

                self.tableWidget.setItem(row, col, item)

        self.tableWidget.resizeColumnsToContents()   ## 테이블의 열 방향 (x축 방향) 크기를 컨텐츠에 알맞게 재조정
        self.tableWidget.resizeRowsToContents()  ## 테이블의 행 방향 (y축 방향) 크기를 컨텐츠에 알맞게 재조정
                                             ## 위 코드 없으면, tableWidget의 290 x 290 크기 안에서 데이터 값이 잘린 채로 표현됨

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    print(column_idx_lookup, kospi_top5.items(), sep= '\n')  ## 값들 확인해보기
    app.exec_()




#####################################   Layout   ####################################
# 사용자가 윈도우의 크기를 변경하거나 할때, 메인 윈도우와 테이블 등의 크기가 연계되지 않기때문에
# 전체적으로 매칭되지 않는 문제가 존재함.   -> Layout 사용으로 해결
# PyQt는 레이아웃 매니저로 QVBoxLayout, QHBoxLayout, QBoxLayout, QGridLayout, QLayout이라는 다섯 가지 클래스를 제공


########################  QVBoxLayout  #######################
# : 이름을 통해 짐작할 수 있듯이 위젯을 수직 방향으로 나열함. (코딩 LINE 순서대로 위에서부터 아래로 레이아웃 배치함)

import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):  ###  (중요!!!) QWidget을 상속받는다. QMainwindow가 아니다.
## QMainWindow에서는 QHBoxLayout, QVBoxLayout 등 사용 못함. QMainWindow 자체 layout 사용 (Tool bar, status bar 같은...)
## QPushBuuton 같은 위젯은 둘다 동일하게 사용 가능
## QMainWindow와 QWidget 동시에 사용하는 케이스    ->   https://www.javaer101.com/ko/article/46028133.html

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)


        self.textEdit = QTextEdit()   ## QLineEdit 과 달리 2줄 이상의 텍스트를 입력받는 텍스트 입력창 , self.textEdit로 객체속성화
        self.pushButton= QPushButton('저장')
        self.lineEdit = QLineEdit(self)
        self.textEdit2 = QTextEdit()


        layout = QVBoxLayout()           # layout이라는 QHBoxLayout()의 객체를 생성
        layout.addWidget(self.textEdit)  # layout이라는 QVBoxLayout() 객체에 self.textEdit 추가 (제일 위)
        layout.addWidget(self.pushButton)  # layout이라는 QVBoxLayout() 객체에 self.textEdit 추가 (위에서 2번째)
        layout.addWidget(self.lineEdit)  # layout이라는 QVBoxLayout() 객체에 self.lineEdit1 추가 (3번째)
        layout.addWidget(self.textEdit2)  # layout이라는 QVBoxLayout() 객체에 self.textEdit2 추가 (맨 아래)

        self.setLayout(layout)  # self.setLayout()을 통해 SET까지 해줘야 실제 레이아룻 배치완료됨, 괄호 안은 레이아웃 객체 삽입했음

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


########################  QVBoxLayout  #######################
# : QHBoxLayout은 행(row) 방향으로 위젯을 배치할 때 사용하는 레이아웃 매니저

import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):     ##  QWidget 사용
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 100)

        self.pushButton1= QPushButton("Button1")
        self.pushButton2= QPushButton("Button2")
        self.pushButton3= QPushButton("Button3")

        layout = QHBoxLayout()               # layout이라는 QHBoxLayout()의 객체를 생성
        layout.addWidget(self.pushButton2)   # pushButton2가 가장 먼저 추가되었으므로, 가장 왼쪽에 위치
        layout.addWidget(self.pushButton1)   # pushButton1가 2번째로 추가되었으므로, 가장 왼쪽에서 2번째에 위치
        layout.addWidget(self.pushButton3)   # pushButton1가 3번째로 추가되었으므로, 가장 오른쪽에 위치

        self.setLayout(layout)               # 레이아웃 셋 하기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()



########################  QGridLayout  #######################
# : 격자 형태의 UI를 구성하는 데 사용
# QLabel, QLineEdit, QPushButton 위젯을 배치한다고 하면, QGridLayout은 QHBoxLayout이나 QVBoxLayout과 달리
# 격자에서 위젯을 배치할 좌표를 입력받는다.

import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 100)

        self.label1 = QLabel("ID: ")
        self.label2 = QLabel("Password: ")
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.pushButton1= QPushButton("Sign In")

        layout = QGridLayout()

        layout.addWidget(self.label1, 0, 0)      # 각 아이템을 좌표의 개념으로 삽입함 ->  label1 : (0,0)
        layout.addWidget(self.lineEdit1, 0, 1)   # 각 아이템을 좌표의 개념으로 삽입함 ->  label2 : (0,1)
        layout.addWidget(self.pushButton1, 0, 2) # 각 아이템을 좌표의 개념으로 삽입함 ->  pushButton1 : (0,2)

        layout.addWidget(self.label2, 1, 0)      # 각 아이템을 좌표의 개념으로 삽입함 ->  label2 : (1,2)
        layout.addWidget(self.lineEdit2, 1, 1)   # 각 아이템을 좌표의 개념으로 삽입함 ->  label2 : (1,1)

        self.setLayout(layout)                   # 레이아웃 set 하기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


####################### Layout 중첩으로 활용하기 (1) #######################

import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 500, 300)

        groupBox = QGroupBox("검색옵션")
        checkBox1 = QCheckBox("상한가")
        checkBox2 = QCheckBox("하한가")
        checkBox3 = QCheckBox("시가총액 상위")
        checkBox4 = QCheckBox("시가총액 하위")
        checkBox5 = QCheckBox("회전율 상위")
        checkBox6 = QCheckBox("대량거래상위")
        checkBox7 = QCheckBox("환산주가상위")
        checkBox8 = QCheckBox("외국인한도소진상위")
        checkBox9 = QCheckBox("투자자별순위")

        tableWidget = QTableWidget(10, 5)    ## QTableWidget을 10 X 5로 구성
        tableWidget.setHorizontalHeaderLabels(["종목코드", "종목명", "현재가", "등락률", "거래량"])
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()

        leftInnerLayOut = QVBoxLayout()      ## groupbox 및 check box용 QVBoxLayout (수직 레이아웃) 객체 생성
        leftInnerLayOut.addWidget(checkBox1)
        leftInnerLayOut.addWidget(checkBox2)
        leftInnerLayOut.addWidget(checkBox3)
        leftInnerLayOut.addWidget(checkBox4)
        leftInnerLayOut.addWidget(checkBox5)
        leftInnerLayOut.addWidget(checkBox6)
        leftInnerLayOut.addWidget(checkBox7)
        leftInnerLayOut.addWidget(checkBox8)
        leftInnerLayOut.addWidget(checkBox9)   ## leftInnerLayout 객체에 check 박스 1부터 9까지를 추가하는 과정.

        groupBox.setLayout(leftInnerLayOut)    ## group box에 check box 추가하는 방법  (아래 참고)
        # groupbox라는 객체 [QGroupBox("검색옵션") 할당] 에 check box가 추가되어있는 leftInnerLayOut 객체를 추가함
        #   ->  groupBox는 leftInnerLayOut 객체까지 포함한 그룹 객체가 됨

        groupBoxLayOut = QVBoxLayout()      ## groupbox용  QVBoxLayout (수직 레이아웃) 객체 생성
        groupBoxLayOut.addWidget(groupBox)  ## 추가                  -> 1개 항목이라 QHBoxLayout로 해도 됨


        tableLayOut = QVBoxLayout()          ## table widget용  QVBoxLayout (수직 레이아웃) 객체 생성
        tableLayOut.addWidget(tableWidget)   ## 객체에 tableWidget 추가

        layout = QHBoxLayout()               ## QVBoxLayout (수평 레이아웃) 객체 생성
        layout.addLayout(groupBoxLayOut)     ## QVBoxLayout 객체에 groupBoxLayOut과 tableLayOut 추가
        layout.addLayout(tableLayOut)        ## QVBoxLayout 객체에 groupBoxLayOut과 tableLayOut 추가

        self.setLayout(layout)               ## 레이아웃 SET


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()

####################### Layout 중첩으로 활용하기 (2) #######################
# -> 테이블 추가

import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 500, 300)

        groupBox = QGroupBox("검색옵션")
        checkBox1 = QCheckBox("상한가")
        checkBox2 = QCheckBox("하한가")
        checkBox3 = QCheckBox("시가총액 상위")
        checkBox4 = QCheckBox("시가총액 하위")
        checkBox5 = QCheckBox("회전율 상위")
        checkBox6 = QCheckBox("대량거래상위")
        checkBox7 = QCheckBox("환산주가상위")
        checkBox8 = QCheckBox("외국인한도소진상위")
        checkBox9 = QCheckBox("투자자별순위")

        ## 첫번째 테이블
        self.tableWidget1 = QTableWidget(10,5)    ## QTableWidget을 10 X 5로 구성
        self.tableWidget1.setHorizontalHeaderLabels(["종목코드", "종목명", "현재가", "등락률", "거래량"])
        self.tableWidget1.resizeColumnsToContents()
        self.tableWidget1.resizeRowsToContents()


        ## 두번째 테이블
        self.tableWidget2 = QTableWidget(self)
        self.tableWidget2.setRowCount(2)     ## 행 갯수 지정 : 2
        self.tableWidget2.setColumnCount(2)  ## 열 갯수 지정 : 2
        self.setTableWidgetData()            ## 메소드 연결
        column_headers = ['총자산', '부채']
        self.tableWidget2.setHorizontalHeaderLabels(column_headers)

        leftInnerLayOut = QVBoxLayout()      ## groupbox 및 check box용 QVBoxLayout (수직 레이아웃) 객체 생성
        leftInnerLayOut.addWidget(checkBox1)
        leftInnerLayOut.addWidget(checkBox2)
        leftInnerLayOut.addWidget(checkBox3)
        leftInnerLayOut.addWidget(checkBox4)
        leftInnerLayOut.addWidget(checkBox5)
        leftInnerLayOut.addWidget(checkBox6)
        leftInnerLayOut.addWidget(checkBox7)
        leftInnerLayOut.addWidget(checkBox8)
        leftInnerLayOut.addWidget(checkBox9)   ## 여기까지는 leftInnerLayout 객체에 check 박스를 추가함.

        groupBox.setLayout(leftInnerLayOut)    ## group box에 check box 추가하는 방법  (아래 참고)
        # groupbox라는 객체 [QGroupBox("검색옵션") 할당] 에 check box가 추가되어있는 leftInnerLayOut 객체를 추가함
        #   ->  groupBox는 leftInnerLayOut 객체까지 포함한 그룹 객체가 됨

        groupBoxLayOut = QVBoxLayout()      ## groupbox용  QVBoxLayout (수직 레이아웃) 객체 생성
        groupBoxLayOut.addWidget(groupBox)  ## 추가                  -> 1개 항목이라 QHBoxLayout로 해도 됨


        tableLayOut = QVBoxLayout()          ## table widget용  QVBoxLayout (수직 레이아웃) 객체 생성
        tableLayOut.addWidget(self.tableWidget1)   ## 객체에 tableWidget1 추가
        tableLayOut.addWidget(self.tableWidget2)   ## 객체에 tableWidget2 추가
        layout = QHBoxLayout()               ## QVBoxLayout (수평 레이아웃) 객체 생성
        layout.addLayout(groupBoxLayOut)     ## QVBoxLayout 객체에 groupBoxLayOut과 tableLayOut 추가
        layout.addLayout(tableLayOut)        ## QVBoxLayout 객체에 groupBoxLayOut과 tableLayOut 추가

        self.setLayout(layout)               ## 레이아웃 SET

    def setTableWidgetData(self):            ## 두번째 테이블 입력 메소드
        self.tableWidget2.setItem(0, 0, QTableWidgetItem("(0,0)"))  ## setItem으로 테이블 값 입력
        self.tableWidget2.setItem(0, 1, QTableWidgetItem("(0,1)"))  ## 첫번째 인자 : 행 인덱스
        self.tableWidget2.setItem(1, 0, QTableWidgetItem("(1,0)"))  ## 두번째 인자 : 열 인덱스
        self.tableWidget2.setItem(1, 1, QTableWidgetItem("(1,1)"))  ## 세번째 인자 : 입력 내용, - 내용은 아래와 같음


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()




#####################################  DialLog  ######################################
#  : 다이얼로그는 사용자와의 상호작용을 위해 사용되는 윈도우를 의미

######################## QFileDialog ########################
# : 사용자가 파일이나 디렉터리를 선택할 수 있게 하는 다이얼로그 창 (흔히 인터넷 사이트에서 파일 업로드 할때, 파일/폴더 디렉터리 찾는 창)

import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("PyStock v0.1")

        self.pushButton = QPushButton("File Open")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)  # QFileDialog 창이 화면에 출력되고,
                                                   # 사용자가 파일을 선택한 후 [열기] 버튼을 클릭하면
                                                   # 해당 파일의 절대 경로가 반환되어 fname에 저장
        self.label.setText(fname[0]) ## label에 fname(선택한 파일의 디렉터리) 값 입력하기
        print(fname)                 ## fname 출력해본 값  : ('C:/Users/com/python/python_v_test/15.py', 'All Files (*)')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()




######################## QInputDialog ########################
# : 용자로부터 간단한 텍스트, 정수, 실수를 받을 때 사용  (edit 시리즈와 다른 점은 팝업으로 발생함)

import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("PyStock v0.1")

        self.pushButton = QPushButton("Input number")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButtonClicked(self):
        text, ok = QInputDialog.getInt(self, '매수 수량', '매수 수량을 입력하세요.')
        # getInt () 괄호안 첫번째 인자 :  부모  (여기서는 MyWindow 객체를 의미)
        # getInt () 괄호안 두번째 인자 : QInputDialog 창 (생성 팝업)에 head에 표시될 텍스트
        # getInt () 괄호안 세번째 인자 : QInputDialog 창 (생성 팝업) 내부에 표시될 텍스트
        # getInt 메서드는 (text, ok)라는 튜플 형태로 값을 반환.
        # text에는 사용자가 입력한 값이 반환되고, ok는 사용자가 OK 버튼을 누른 경우에 True 값을 가짐

        if ok:     ## ok가 True로 반환받았다면 (사용자가 ok버튼을 눌렀다면)
            self.label.setText(str(text))  ## 라벨에 텍스트 입력력
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


######################## 메인 윈도우와 다이얼로그의 상호 작용 ########################

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class LogInDialog(QDialog):  ## Dialog용 클래스, QDialog를 부모로 상속받음
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.id = None
        self.password = None

    def setupUI(self):
        self.setGeometry(1100, 200, 300, 100)
        self.setWindowTitle("Sign In")                                 ## 다이얼로그 창 헤드에 텍스트 삽입하기
        self.setWindowIcon(QIcon(r'C:\Users\com\Desktop\icon.png'))    ## 다이얼로그 창 헤드에 아이콘 삽입하기
        # 아이콘 찾기 좋은 사이트 ->  https://www.iconfinder.com/
        label1 = QLabel("ID: ")
        label2 = QLabel("Password: ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.pushButton1= QPushButton("Sign In")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()                    ## QGridLayout()로  각 항목 위치 배열하기
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):  ## pushButton1 'sign' 버튼이 눌리면, self.id, self.password에 입력 값을 대입
        self.id = self.lineEdit1.text()
        self.password = self.lineEdit2.text()
        self.close()


class MyWindow(QWidget):    ## 메인 윈도우
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("PyStock v0.1")
        self.setWindowIcon(QIcon('icon.png'))    ## 메인 윈도우 아이콘 추가 (기본 아이콘)

        self.pushButton = QPushButton("Sign In")
        self.pushButton.clicked.connect(self.pushButtonClicked)  ## 눌리면 pushButtonClicked로 진입 (Dialog 진입 메소드)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)   ## 버튼 위젯 추가
        layout.addWidget(self.label)        ## id, password 입력시, 메인 윈도우에서 그 값을 표시할 label 위젯 추가

        self.setLayout(layout)

    def pushButtonClicked(self):
        dlg = LogInDialog()                 ## LogInDialog() 클래스 인스턴스 생성
        dlg.exec_()                         ## dlg 인스턴스에 대해 이벤트 루프 실행   (중요 !!!!!) -> dlg 클래스에 머무르게 됨
        id = dlg.id
        password = dlg.password
        self.label.setText("id: %s password: %s" % (id, password))  ## label에 텍스트 입력하기

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()




#####################################  PyQT와 matplotlib 연동  ######################################

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas_datareader.data as web

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(600, 200, 1200, 600)
        self.setWindowTitle("PyChart Viewer v0.1")
        self.setWindowIcon(QIcon('icon.png'))

        self.lineEdit = QLineEdit()
        self.pushButton = QPushButton("차트그리기")
        self.pushButton.clicked.connect(self.pushButtonClicked)

        self.fig = plt.Figure()               ## 그래프를 객체 속성화 함
        self.canvas = FigureCanvas(self.fig)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        # Right Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.lineEdit)
        rightLayout.addStretch(3)                    ## 괄호안 숫자 크기 만큼의 빈공간을 추가함 (간격 띄우기)
        rightLayout.addWidget(self.pushButton)
        rightLayout.addStretch(1)                    ## 괄호안 숫자 크기 만큼의 빈공간을 추가함 (간격 띄우기)

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 5)       ## 해당 레이아웃의 늘림인자 비율, left : right = 5 : 2
        layout.setStretchFactor(rightLayout, 2)      ## 최소값은 0 (기본값, default)이다.  1이면 0에 비해 1배 늘어남.

        self.setLayout(layout)

    def pushButtonClicked(self):
        code = self.lineEdit.text()
        df = web.DataReader(code + ".KS", "yahoo")
        df['MA20'] = df['Adj Close'].rolling(window=20).mean()   ## 20일 평균값
        df['MA60'] = df['Adj Close'].rolling(window=60).mean()   ## 60일 평균값

        ax = self.fig.add_subplot(111)                           ## subplot을 ax 객체로 생성
        ax.plot(df.index, df['Adj Close'], label='Adj Close')
        ax.plot(df.index, df['MA20'], label='MA20')
        ax.plot(df.index, df['MA60'], label='MA60')
        ax.legend(loc='upper right')
        ax.grid()
        self.canvas.draw()            ## canvas 객체에 [ FigureCanvas(self.fig) ] 그림을 그리는 메소드, plt.show() 아님


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()