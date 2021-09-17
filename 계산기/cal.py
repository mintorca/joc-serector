import sys
import math
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui_form = uic.loadUiType("qtCalculator.ui" )[0]
class QtCalculator(QMainWindow, ui_form):
    def __init__(self ):
        super(QtCalculator,self ).__init__()
        self .setupUi(self )
        self .B0.clicked.connect(self .B0_click)
        self .B1.clicked.connect(self .B1_click)
        self .B2.clicked.connect(self .B2_click)
        self .B3.clicked.connect(self .B3_click)
        self .B4.clicked.connect(self .B4_click)
        self .B5.clicked.connect(self .B5_click)
        self .B6.clicked.connect(self .B6_click)
        self .B7.clicked.connect(self .B7_click)
        self .B8.clicked.connect(self .B8_click)
        self .B9.clicked.connect(self .B9_click)
        self .DIV.clicked.connect(self .DIV_click)
        self .MUL.clicked.connect(self .MUL_click)
        self .PLUS.clicked.connect(self .PLUS_click)
        self .EQUAL.clicked.connect(self .EQUAL_click)
        self .C.clicked.connect(self .C_click)
        self .DIF.clicked.connect(self .DIF_click)
        self .REMAIN.clicked.connect(self .REMAIN_click)
        self .BP.clicked.connect(self .BP_click)
        self .BACK.clicked.connect(self .BACK_click)
        self .MR.clicked.connect(self .MR_click)
        self .MP.clicked.connect(self .MP_click)
        self .MC.clicked.connect(self .MC_click)
        self .MS.clicked.connect(self .MS_click)
        self .MM.clicked.connect(self .MM_click)
        self .SQRT.clicked.connect(self .SQRT_click)
        self .DIVX.clicked.connect(self .DIVX_click)
        self .SIGN.clicked.connect(self .SIGN_click)
        self .CE.clicked.connect(self .CE_click)

    def B0_click(self ): self .lineEdit.insert('0')
    def B1_click(self ): self .lineEdit.insert('1')
    def B2_click(self ): self .lineEdit.insert('2')
    def B3_click(self ): self .lineEdit.insert('3')
    def B4_click(self ): self .lineEdit.insert('4')
    def B5_click(self ): self .lineEdit.insert('5')
    def B6_click(self ): self .lineEdit.insert('6')
    def B7_click(self ): self .lineEdit.insert('7')
    def B8_click(self ): self .lineEdit.insert('8')
    def B9_click(self ): self .lineEdit.insert('9')
    def DIV_click(self ): self .lineEdit.insert('/')
    def DIF_click(self ): self .lineEdit.insert('-' )
    def MUL_click(self ): self .lineEdit.insert('*')
    def PLUS_click(self ): self .lineEdit.insert('+' )
    def REMAIN_click(self ): self .lineEdit.insert('%' )
    def BP_click(self ): self .lineEdit.insert('.' )
    def BACK_click(self ): self .lineEdit.backspace( )
    def EQUAL_click(self ):
        result = eval(str(self .lineEdit.text()))
        self .lineEdit.insert(" = " + str(result))
    def C_click(self ):
        self .lineEdit.clear()
    def MC_click(self ):
        global memo
        memo='0'
        self .lineEdit.setText(str(memo))
    def MR_click(self):
        self .lineEdit.setText(str(memo))
    def MP_click(self):
        global memo
        s=eval(str(self .lineEdit.text()))
        memo=memo+s
        self .lineEdit.setText(str(memo))
    def MS_click(self):
        global memo
        memo=eval(str(self.lineEdit.text()))
    def MM_click(self):
        global memo
        out=eval(str(self.lineEdit.text()))
        memo=memo-out
        self .lineEdit.setText(str(memo))
    def SQRT_click(self ):
        x=eval(str(self.lineEdit.text()))
        self .lineEdit.insert(" = " + str(math.sqrt(x)))
    def DIVX_click(self ):
        fr=float(eval(str(self.lineEdit.text())))
        ac=1/fr
        self .lineEdit.insert(" 1/X= " + str(ac))
    global base
    global kill
    def SIGN_click(self ):
        global base
        global kill
        base=eval(str(self.lineEdit.text()))
        kill=base-2*base
        self.lineEdit.clear()
        self.lineEdit.insert(str(gam))
    def CE_click(self ):
        ap=0
        am=0
        au=0
        ad=0
        last=0
        leng=str(self.lineEdit.text())
        ap=leng.rfind('+')
        am=leng.rfind('-')
        au=leng.rfind('*')
        ad=leng.rfind('/')
        if ap>=am and au and ad:
            last=ap
        if am>=ap and au and ad:
            last=am
        if au>=ap and am and ad:
            last=au  
        if ad>=ap and au and am:
            last=ad
             
        self .lineEdit.clear()
        self.lineEdit.insert(leng[:last+1])
    
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = QtCalculator()
    myWindow.show()
    app.exec_()