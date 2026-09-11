# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fe15main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFrame, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QWidget)
import portraits_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(382, 597)
        palette = QPalette()
        brush = QBrush(QColor(102, 44, 36, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        brush1 = QBrush(QColor(30, 30, 30, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Segoe MDL2 Assets"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(102, 44, 36);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frmConfig = QFrame(self.centralwidget)
        self.frmConfig.setObjectName(u"frmConfig")
        self.frmConfig.setGeometry(QRect(10, 10, 361, 251))
        palette1 = QPalette()
        gradient = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient.setSpread(QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(94, 48, 48, 255))
        gradient.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush2 = QBrush(gradient)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush2)
        gradient1 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient1.setSpread(QGradient.Spread.PadSpread)
        gradient1.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(94, 48, 48, 255))
        gradient1.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush3 = QBrush(gradient1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush3)
        gradient2 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient2.setSpread(QGradient.Spread.PadSpread)
        gradient2.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(94, 48, 48, 255))
        gradient2.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush4 = QBrush(gradient2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush4)
        gradient3 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient3.setSpread(QGradient.Spread.PadSpread)
        gradient3.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(94, 48, 48, 255))
        gradient3.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush5 = QBrush(gradient3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush5)
        gradient4 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient4.setSpread(QGradient.Spread.PadSpread)
        gradient4.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(94, 48, 48, 255))
        gradient4.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush6 = QBrush(gradient4)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        gradient5 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient5.setSpread(QGradient.Spread.PadSpread)
        gradient5.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(94, 48, 48, 255))
        gradient5.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush7 = QBrush(gradient5)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush7)
        gradient6 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient6.setSpread(QGradient.Spread.PadSpread)
        gradient6.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(94, 48, 48, 255))
        gradient6.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush8 = QBrush(gradient6)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush8)
        gradient7 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient7.setSpread(QGradient.Spread.PadSpread)
        gradient7.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(94, 48, 48, 255))
        gradient7.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush9 = QBrush(gradient7)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        gradient8 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient8.setSpread(QGradient.Spread.PadSpread)
        gradient8.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(94, 48, 48, 255))
        gradient8.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush10 = QBrush(gradient8)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush10)
        self.frmConfig.setPalette(palette1)
        self.frmConfig.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.421, cy:0.233273, radius:1.53642, fx:0.421, fy:0.234, stop:0 rgba(94, 48, 48, 255), stop:0.789474 rgba(26, 16, 15, 255));\n"
"border-radius: 8px;")
        self.frmConfig.setFrameShape(QFrame.Shape.Panel)
        self.frmConfig.setFrameShadow(QFrame.Shadow.Raised)
        self.lblPersonagem = QLabel(self.frmConfig)
        self.lblPersonagem.setObjectName(u"lblPersonagem")
        self.lblPersonagem.setGeometry(QRect(10, 50, 71, 31))
        palette2 = QPalette()
        brush11 = QBrush(QColor(190, 141, 142, 255))
        brush11.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush11)
        brush12 = QBrush(QColor(58, 7, 21, 255))
        brush12.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush12)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush11)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush11)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush12)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush12)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush13)
        brush14 = QBrush(QColor(255, 255, 255, 255))
        brush14.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush14)
        brush15 = QBrush(QColor(190, 141, 142, 128))
        brush15.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush11)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush12)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush11)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush11)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush12)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush12)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush13)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush12)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush12)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush12)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush13)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        self.lblPersonagem.setPalette(palette2)
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(14)
        self.lblPersonagem.setFont(font1)
        self.lblPersonagem.setAutoFillBackground(False)
        self.lblPersonagem.setStyleSheet(u"background-color: rgb(58, 7, 21);    /* Tom vinho escuro do fundo da caixinha */\n"
"    color: rgb(190, 141, 142);\n"
"    /*border: 1px solid #4a1a24;     Borda sutil levemente mais clara que o fundo */\n"
"    border-radius: 4px;           /* Arredondamento dos cantos */\n"
"    padding: 3px 6px;\n"
"	margin: 1px;")
        self.lblPersonagem.setFrameShape(QFrame.Shape.Panel)
        self.lblPersonagem.setScaledContents(False)
        self.lblPersonagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblPersonagem.setWordWrap(False)
        self.lblClasse = QLabel(self.frmConfig)
        self.lblClasse.setObjectName(u"lblClasse")
        self.lblClasse.setGeometry(QRect(10, 80, 71, 31))
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush11)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush12)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush11)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush11)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush12)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush12)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush13)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush11)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush12)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush11)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush11)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush12)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush12)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush13)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush12)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush12)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush12)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush13)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        self.lblClasse.setPalette(palette3)
        self.lblClasse.setFont(font1)
        self.lblClasse.setAutoFillBackground(False)
        self.lblClasse.setStyleSheet(u"background-color: rgb(58, 7, 21);    /* Tom vinho escuro do fundo da caixinha */\n"
"    color: rgb(190, 141, 142);\n"
"    /*border: 1px solid #4a1a24;     Borda sutil levemente mais clara que o fundo */\n"
"    border-radius: 4px;           /* Arredondamento dos cantos */\n"
"    padding: 3px 6px;\n"
"	margin: 1px;")
        self.lblClasse.setFrameShape(QFrame.Shape.Panel)
        self.lblClasse.setScaledContents(False)
        self.lblClasse.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblClasse.setWordWrap(False)
        self.lblNivel = QLabel(self.frmConfig)
        self.lblNivel.setObjectName(u"lblNivel")
        self.lblNivel.setGeometry(QRect(10, 110, 71, 31))
        palette4 = QPalette()
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush11)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush12)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush11)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush11)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush12)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush12)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush13)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush11)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush12)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush11)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush11)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush12)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush12)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush13)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush12)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush12)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush12)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush13)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        self.lblNivel.setPalette(palette4)
        self.lblNivel.setFont(font1)
        self.lblNivel.setAutoFillBackground(False)
        self.lblNivel.setStyleSheet(u"background-color: rgb(58, 7, 21);    /* Tom vinho escuro do fundo da caixinha */\n"
"    color: rgb(190, 141, 142);\n"
"    /*border: 1px solid #4a1a24;     Borda sutil levemente mais clara que o fundo */\n"
"    border-radius: 4px;           /* Arredondamento dos cantos */\n"
"    padding: 3px 6px;\n"
"	margin: 1px;")
        self.lblNivel.setFrameShape(QFrame.Shape.Panel)
        self.lblNivel.setScaledContents(False)
        self.lblNivel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblNivel.setWordWrap(False)
        self.cbbPersonagem = QComboBox(self.frmConfig)
        self.cbbPersonagem.setObjectName(u"cbbPersonagem")
        self.cbbPersonagem.setGeometry(QRect(90, 50, 171, 31))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        self.cbbPersonagem.setFont(font2)
        self.cbbPersonagem.setStyleSheet(u"/* Estado Normal da ComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(58, 7, 21);\n"
"    color: rgb(255, 234, 228);\n"
"    border: 1px solid rgb(112, 24, 37);\n"
"    border-radius: 4px;\n"
"    padding: 4px 8px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-size: 14px;\n"
"	margin: 1px;\n"
"}\n"
"\n"
"/* Hover e Foco */\n"
"QComboBox:hover {\n"
"    border: 1px solid rgb(129, 50, 66);\n"
"    /*background-color: #3b161f;*/\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid rgb(129, 50, 66);\n"
"}\n"
"\n"
"/* Seta de Sele\u00e7\u00e3o (Drop-down Button) */\n"
"/*QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left: 1px solid #54222b;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background-color: #230d12;\n"
"}/*\n"
"\n"
"/* \u00cdcone da Seta Desenhado via CSS */\n"
"/*QComboBox::down-arrow {\n"
"    image: none;\n"
"	position: relative;\n"
"background: non"
                        "e;\n"
"border:none;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 6px solid #e2c097;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover {\n"
"    border-top-color: #ffffff;\n"
"}*/\n"
"\n"
"/* Estiliza\u00e7\u00e3o da Lista Suspensa (Menu Aberto) */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #1e0b0f;\n"
"    color: #e2c097;\n"
"    border: 2px solid #54222b;\n"
"    selection-background-color: #54222b;\n"
"    selection-color: #ffffff;\n"
"    padding: 4px;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Itens da Lista ao Passar o Mouse */\n"
"QComboBox QAbstractItemView::item {\n"
"    min-height: 24px;\n"
"    padding-left: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #3b161f;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* --- BARRA DE ROLAGEM DA COMBOBOX --- */\n"
"QComboBox QAbstractItemView QScrollBar:vertical {\n"
"    background-color: #1a080c; /* Cor do fundo d"
                        "a trilha */\n"
"    width: 8px;                 /* Largura da barra */\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* O bloco que voc\u00ea arrasta */\n"
"QComboBox QAbstractItemView QScrollBar::handle:vertical {\n"
"    background-color: #54222b;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Hover no bloco */\n"
"QComboBox QAbstractItemView QScrollBar::handle:vertical:hover {\n"
"    background-color: #883543;\n"
"}\n"
"\n"
"/* Remove as setinhas de topo e base */\n"
"QComboBox QAbstractItemView QScrollBar::add-line:vertical,\n"
"QComboBox QAbstractItemView QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::add-page:vertical,\n"
"QComboBox QAbstractItemView QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.cbbPersonagem.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)
        self.cbbClasse = QComboBox(self.frmConfig)
        self.cbbClasse.setObjectName(u"cbbClasse")
        self.cbbClasse.setGeometry(QRect(90, 80, 171, 31))
        self.cbbClasse.setFont(font2)
        self.cbbClasse.setStyleSheet(u"/* Estado Normal da ComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(58, 7, 21);\n"
"    color: rgb(255, 234, 228);\n"
"    border: 1px solid rgb(112, 24, 37);\n"
"    border-radius: 4px;\n"
"    padding: 4px 8px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-size: 14px;\n"
"	margin: 1px;\n"
"}\n"
"\n"
"/* Hover e Foco */\n"
"QComboBox:hover {\n"
"    border: 1px solid rgb(129, 50, 66);\n"
"    /*background-color: #3b161f;*/\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid rgb(129, 50, 66);\n"
"}\n"
"\n"
"/* Seta de Sele\u00e7\u00e3o (Drop-down Button) */\n"
"/*QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left: 1px solid #54222b;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background-color: #230d12;\n"
"}/*\n"
"\n"
"/* \u00cdcone da Seta Desenhado via CSS */\n"
"/*QComboBox::down-arrow {\n"
"    image: none;\n"
"	position: relative;\n"
"background: non"
                        "e;\n"
"border:none;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 6px solid #e2c097;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:hover {\n"
"    border-top-color: #ffffff;\n"
"}*/\n"
"\n"
"/* Estiliza\u00e7\u00e3o da Lista Suspensa (Menu Aberto) */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #1e0b0f;\n"
"    color: #e2c097;\n"
"    border: 2px solid #54222b;\n"
"    selection-background-color: #54222b;\n"
"    selection-color: #ffffff;\n"
"    padding: 4px;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Itens da Lista ao Passar o Mouse */\n"
"QComboBox QAbstractItemView::item {\n"
"    min-height: 24px;\n"
"    padding-left: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #3b161f;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* --- BARRA DE ROLAGEM DA COMBOBOX --- */\n"
"QComboBox QAbstractItemView QScrollBar:vertical {\n"
"    background-color: #1a080c; /* Cor do fundo d"
                        "a trilha */\n"
"    width: 8px;                 /* Largura da barra */\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* O bloco que voc\u00ea arrasta */\n"
"QComboBox QAbstractItemView QScrollBar::handle:vertical {\n"
"    background-color: #54222b;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Hover no bloco */\n"
"QComboBox QAbstractItemView QScrollBar::handle:vertical:hover {\n"
"    background-color: #883543;\n"
"}\n"
"\n"
"/* Remove as setinhas de topo e base */\n"
"QComboBox QAbstractItemView QScrollBar::add-line:vertical,\n"
"QComboBox QAbstractItemView QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView QScrollBar::add-page:vertical,\n"
"QComboBox QAbstractItemView QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.cbbClasse.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)
        self.spbLevel = QSpinBox(self.frmConfig)
        self.spbLevel.setObjectName(u"spbLevel")
        self.spbLevel.setGeometry(QRect(90, 110, 171, 31))
        self.spbLevel.setFont(font2)
        self.spbLevel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.spbLevel.setStyleSheet(u"/* --- Estado Normal da SpinBox --- */\n"
"QSpinBox, QDoubleSpinBox {\n"
"    background-color: rgb(58, 7, 21);\n"
"    color: rgb(255, 234, 228);\n"
"    border: 1px solid rgb(112, 24, 37);\n"
"    border-radius: 4px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-size: 14px;\n"
"    margin: 1px;\n"
"	padding: 0px 30px 0px 0px\n"
"}\n"
"\n"
"/* Hover e Foco */\n"
"QSpinBox:hover, QDoubleSpinBox:hover {\n"
"    border: 1px solid rgb(129, 50, 66);\n"
"}\n"
"\n"
"QSpinBox:focus, QDoubleSpinBox:focus {\n"
"    border: 1px solid rgb(129, 50, 66);\n"
"}")
        self.spbLevel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.spbLevel.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.spbLevel.setMinimum(1)
        self.spbLevel.setMaximum(20)
        self.btnCalcular = QPushButton(self.frmConfig)
        self.btnCalcular.setObjectName(u"btnCalcular")
        self.btnCalcular.setGeometry(QRect(100, 190, 161, 51))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei"])
        font3.setPointSize(16)
        self.btnCalcular.setFont(font3)
        self.btnCalcular.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCalcular.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.495, cy:0.153727, radius:1.53642, fx:0.495, fy:0.154, stop:0 rgba(168, 40, 56, 255), stop:0.789474 rgba(95, 18, 28, 255));\n"
"    color: rgb(255, 234, 228);\n"
"    border-top: 1px solid rgb(148, 58, 77);     /* Bordas superior e esquerda mais claras (Luz) */\n"
"    border-left: 1px solid rgb(148, 58, 77);\n"
"    border-bottom: 1px solid rgb(78, 41, 40);  /* Bordas inferior e direita mais escuras (Sombra) */\n"
"    border-right: 1px solid rgb(148, 58, 77);    /* Borda sutil levemente mais clara que o fundo */\n"
"    border-radius: 4px;           /* Arredondamento dos cantos */\n"
"    padding: 3px 6px;\n"
"	margin: 1px;\n"
"")
        self.frmInfoTitulo = QFrame(self.frmConfig)
        self.frmInfoTitulo.setObjectName(u"frmInfoTitulo")
        self.frmInfoTitulo.setGeometry(QRect(0, 0, 361, 41))
        palette5 = QPalette()
        gradient9 = QLinearGradient(0, 0, 0.5, 0)
        gradient9.setSpread(QGradient.Spread.PadSpread)
        gradient9.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient9.setColorAt(0, QColor(148, 58, 77, 255))
        gradient9.setColorAt(1, QColor(116, 25, 38, 255))
        brush16 = QBrush(gradient9)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush16)
        gradient10 = QLinearGradient(0, 0, 0.5, 0)
        gradient10.setSpread(QGradient.Spread.PadSpread)
        gradient10.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient10.setColorAt(0, QColor(148, 58, 77, 255))
        gradient10.setColorAt(1, QColor(116, 25, 38, 255))
        brush17 = QBrush(gradient10)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush17)
        gradient11 = QLinearGradient(0, 0, 0.5, 0)
        gradient11.setSpread(QGradient.Spread.PadSpread)
        gradient11.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient11.setColorAt(0, QColor(148, 58, 77, 255))
        gradient11.setColorAt(1, QColor(116, 25, 38, 255))
        brush18 = QBrush(gradient11)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush18)
        gradient12 = QLinearGradient(0, 0, 0.5, 0)
        gradient12.setSpread(QGradient.Spread.PadSpread)
        gradient12.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient12.setColorAt(0, QColor(148, 58, 77, 255))
        gradient12.setColorAt(1, QColor(116, 25, 38, 255))
        brush19 = QBrush(gradient12)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush19)
        gradient13 = QLinearGradient(0, 0, 0.5, 0)
        gradient13.setSpread(QGradient.Spread.PadSpread)
        gradient13.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient13.setColorAt(0, QColor(148, 58, 77, 255))
        gradient13.setColorAt(1, QColor(116, 25, 38, 255))
        brush20 = QBrush(gradient13)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush20)
        gradient14 = QLinearGradient(0, 0, 0.5, 0)
        gradient14.setSpread(QGradient.Spread.PadSpread)
        gradient14.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient14.setColorAt(0, QColor(148, 58, 77, 255))
        gradient14.setColorAt(1, QColor(116, 25, 38, 255))
        brush21 = QBrush(gradient14)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush21)
        gradient15 = QLinearGradient(0, 0, 0.5, 0)
        gradient15.setSpread(QGradient.Spread.PadSpread)
        gradient15.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient15.setColorAt(0, QColor(148, 58, 77, 255))
        gradient15.setColorAt(1, QColor(116, 25, 38, 255))
        brush22 = QBrush(gradient15)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush22)
        gradient16 = QLinearGradient(0, 0, 0.5, 0)
        gradient16.setSpread(QGradient.Spread.PadSpread)
        gradient16.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient16.setColorAt(0, QColor(148, 58, 77, 255))
        gradient16.setColorAt(1, QColor(116, 25, 38, 255))
        brush23 = QBrush(gradient16)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush23)
        gradient17 = QLinearGradient(0, 0, 0.5, 0)
        gradient17.setSpread(QGradient.Spread.PadSpread)
        gradient17.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient17.setColorAt(0, QColor(148, 58, 77, 255))
        gradient17.setColorAt(1, QColor(116, 25, 38, 255))
        brush24 = QBrush(gradient17)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush24)
        self.frmInfoTitulo.setPalette(palette5)
        self.frmInfoTitulo.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.5, y2:0, stop:0 rgb(148, 58, 77), stop:1 rgb(116, 25, 38));")
        self.frmInfoTitulo.setFrameShape(QFrame.Shape.Panel)
        self.frmInfoTitulo.setFrameShadow(QFrame.Shadow.Plain)
        self.frmInfoTitulo.setLineWidth(0)
        self.lblPersonagem_2 = QLabel(self.frmInfoTitulo)
        self.lblPersonagem_2.setObjectName(u"lblPersonagem_2")
        self.lblPersonagem_2.setGeometry(QRect(10, 0, 111, 41))
        self.lblPersonagem_2.setFont(font3)
        self.lblPersonagem_2.setAutoFillBackground(False)
        self.lblPersonagem_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblPersonagem_2.setFrameShape(QFrame.Shape.NoFrame)
        self.lblPersonagem_2.setScaledContents(False)
        self.lblPersonagem_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblPersonagem_2.setWordWrap(False)
        self.frmInfoTitulo_4 = QFrame(self.frmInfoTitulo)
        self.frmInfoTitulo_4.setObjectName(u"frmInfoTitulo_4")
        self.frmInfoTitulo_4.setGeometry(QRect(0, 20, 361, 21))
        palette6 = QPalette()
        gradient18 = QLinearGradient(0, 0, 0.5, 0)
        gradient18.setSpread(QGradient.Spread.PadSpread)
        gradient18.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient18.setColorAt(0, QColor(148, 58, 77, 255))
        gradient18.setColorAt(1, QColor(116, 25, 38, 255))
        brush25 = QBrush(gradient18)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush25)
        gradient19 = QLinearGradient(0, 0, 0.5, 0)
        gradient19.setSpread(QGradient.Spread.PadSpread)
        gradient19.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient19.setColorAt(0, QColor(148, 58, 77, 255))
        gradient19.setColorAt(1, QColor(116, 25, 38, 255))
        brush26 = QBrush(gradient19)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush26)
        gradient20 = QLinearGradient(0, 0, 0.5, 0)
        gradient20.setSpread(QGradient.Spread.PadSpread)
        gradient20.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient20.setColorAt(0, QColor(148, 58, 77, 255))
        gradient20.setColorAt(1, QColor(116, 25, 38, 255))
        brush27 = QBrush(gradient20)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush27)
        gradient21 = QLinearGradient(0, 0, 0.5, 0)
        gradient21.setSpread(QGradient.Spread.PadSpread)
        gradient21.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient21.setColorAt(0, QColor(148, 58, 77, 255))
        gradient21.setColorAt(1, QColor(116, 25, 38, 255))
        brush28 = QBrush(gradient21)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush28)
        gradient22 = QLinearGradient(0, 0, 0.5, 0)
        gradient22.setSpread(QGradient.Spread.PadSpread)
        gradient22.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient22.setColorAt(0, QColor(148, 58, 77, 255))
        gradient22.setColorAt(1, QColor(116, 25, 38, 255))
        brush29 = QBrush(gradient22)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush29)
        gradient23 = QLinearGradient(0, 0, 0.5, 0)
        gradient23.setSpread(QGradient.Spread.PadSpread)
        gradient23.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient23.setColorAt(0, QColor(148, 58, 77, 255))
        gradient23.setColorAt(1, QColor(116, 25, 38, 255))
        brush30 = QBrush(gradient23)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush30)
        gradient24 = QLinearGradient(0, 0, 0.5, 0)
        gradient24.setSpread(QGradient.Spread.PadSpread)
        gradient24.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient24.setColorAt(0, QColor(148, 58, 77, 255))
        gradient24.setColorAt(1, QColor(116, 25, 38, 255))
        brush31 = QBrush(gradient24)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush31)
        gradient25 = QLinearGradient(0, 0, 0.5, 0)
        gradient25.setSpread(QGradient.Spread.PadSpread)
        gradient25.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient25.setColorAt(0, QColor(148, 58, 77, 255))
        gradient25.setColorAt(1, QColor(116, 25, 38, 255))
        brush32 = QBrush(gradient25)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush32)
        gradient26 = QLinearGradient(0, 0, 0.5, 0)
        gradient26.setSpread(QGradient.Spread.PadSpread)
        gradient26.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient26.setColorAt(0, QColor(148, 58, 77, 255))
        gradient26.setColorAt(1, QColor(116, 25, 38, 255))
        brush33 = QBrush(gradient26)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush33)
        self.frmInfoTitulo_4.setPalette(palette6)
        self.frmInfoTitulo_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.5, y2:0, stop:0 rgb(148, 58, 77), stop:1 rgb(116, 25, 38));\n"
"border-radius: 0px;")
        self.frmInfoTitulo_4.setFrameShape(QFrame.Shape.Panel)
        self.frmInfoTitulo_4.setFrameShadow(QFrame.Shadow.Plain)
        self.frmInfoTitulo_4.setLineWidth(0)
        self.frmInfoTitulo_4.raise_()
        self.lblPersonagem_2.raise_()
        self.frame_2 = QFrame(self.frmConfig)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(5, 45, 261, 141))
        font4 = QFont()
        font4.setPointSize(9)
        self.frame_2.setFont(font4)
        self.frame_2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.frame_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);\n"
"border-radius: 10px;")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(0)
        self.chkAuto = QCheckBox(self.frmConfig)
        self.chkAuto.setObjectName(u"chkAuto")
        self.chkAuto.setGeometry(QRect(10, 150, 151, 31))
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei"])
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.chkAuto.setFont(font5)
        self.chkAuto.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chkAuto.setAutoFillBackground(False)
        self.chkAuto.setStyleSheet(u"QCheckBox{\n"
"background-color: rgb(58, 7, 21);  \n"
"color: rgb(190, 141, 142);\n"
"border-radius: 4px;           \n"
"margin: 1px;\n"
"padding: 0px 0px 0px 10px;\n"
"spacing: 10px;\n"
"}\n"
"")
        self.chkAuto.setIconSize(QSize(16, 16))
        self.chkAuto.setChecked(False)
        self.chkAuto.setTristate(False)
        self.frame_2.raise_()
        self.lblPersonagem.raise_()
        self.lblClasse.raise_()
        self.lblNivel.raise_()
        self.cbbPersonagem.raise_()
        self.cbbClasse.raise_()
        self.spbLevel.raise_()
        self.btnCalcular.raise_()
        self.frmInfoTitulo.raise_()
        self.chkAuto.raise_()
        self.frame_avg_stats = QFrame(self.centralwidget)
        self.frame_avg_stats.setObjectName(u"frame_avg_stats")
        self.frame_avg_stats.setGeometry(QRect(10, 270, 361, 271))
        palette7 = QPalette()
        gradient27 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient27.setSpread(QGradient.Spread.PadSpread)
        gradient27.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient27.setColorAt(0, QColor(94, 48, 48, 255))
        gradient27.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush34 = QBrush(gradient27)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush34)
        gradient28 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient28.setSpread(QGradient.Spread.PadSpread)
        gradient28.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient28.setColorAt(0, QColor(94, 48, 48, 255))
        gradient28.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush35 = QBrush(gradient28)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush35)
        gradient29 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient29.setSpread(QGradient.Spread.PadSpread)
        gradient29.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient29.setColorAt(0, QColor(94, 48, 48, 255))
        gradient29.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush36 = QBrush(gradient29)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush36)
        gradient30 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient30.setSpread(QGradient.Spread.PadSpread)
        gradient30.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient30.setColorAt(0, QColor(94, 48, 48, 255))
        gradient30.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush37 = QBrush(gradient30)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush37)
        gradient31 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient31.setSpread(QGradient.Spread.PadSpread)
        gradient31.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient31.setColorAt(0, QColor(94, 48, 48, 255))
        gradient31.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush38 = QBrush(gradient31)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush38)
        gradient32 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient32.setSpread(QGradient.Spread.PadSpread)
        gradient32.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient32.setColorAt(0, QColor(94, 48, 48, 255))
        gradient32.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush39 = QBrush(gradient32)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush39)
        gradient33 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient33.setSpread(QGradient.Spread.PadSpread)
        gradient33.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient33.setColorAt(0, QColor(94, 48, 48, 255))
        gradient33.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush40 = QBrush(gradient33)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush40)
        gradient34 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient34.setSpread(QGradient.Spread.PadSpread)
        gradient34.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient34.setColorAt(0, QColor(94, 48, 48, 255))
        gradient34.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush41 = QBrush(gradient34)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush41)
        gradient35 = QRadialGradient(0.421, 0.233273, 1.53642, 0.421, 0.234)
        gradient35.setSpread(QGradient.Spread.PadSpread)
        gradient35.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient35.setColorAt(0, QColor(94, 48, 48, 255))
        gradient35.setColorAt(0.789474, QColor(26, 16, 15, 255))
        brush42 = QBrush(gradient35)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush42)
        self.frame_avg_stats.setPalette(palette7)
        self.frame_avg_stats.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.421, cy:0.233273, radius:1.53642, fx:0.421, fy:0.234, stop:0 rgba(94, 48, 48, 255), stop:0.789474 rgba(26, 16, 15, 255));\n"
"border-radius: 8px;")
        self.frame_avg_stats.setFrameShape(QFrame.Shape.Panel)
        self.frame_avg_stats.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_avg_stats.setLineWidth(0)
        self.frmInfoTitulo_2 = QFrame(self.frame_avg_stats)
        self.frmInfoTitulo_2.setObjectName(u"frmInfoTitulo_2")
        self.frmInfoTitulo_2.setGeometry(QRect(0, 0, 361, 41))
        palette8 = QPalette()
        gradient36 = QLinearGradient(0, 0, 0.5, 0)
        gradient36.setSpread(QGradient.Spread.PadSpread)
        gradient36.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient36.setColorAt(0, QColor(148, 58, 77, 255))
        gradient36.setColorAt(1, QColor(116, 25, 38, 255))
        brush43 = QBrush(gradient36)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush43)
        gradient37 = QLinearGradient(0, 0, 0.5, 0)
        gradient37.setSpread(QGradient.Spread.PadSpread)
        gradient37.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient37.setColorAt(0, QColor(148, 58, 77, 255))
        gradient37.setColorAt(1, QColor(116, 25, 38, 255))
        brush44 = QBrush(gradient37)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush44)
        gradient38 = QLinearGradient(0, 0, 0.5, 0)
        gradient38.setSpread(QGradient.Spread.PadSpread)
        gradient38.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient38.setColorAt(0, QColor(148, 58, 77, 255))
        gradient38.setColorAt(1, QColor(116, 25, 38, 255))
        brush45 = QBrush(gradient38)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush45)
        gradient39 = QLinearGradient(0, 0, 0.5, 0)
        gradient39.setSpread(QGradient.Spread.PadSpread)
        gradient39.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient39.setColorAt(0, QColor(148, 58, 77, 255))
        gradient39.setColorAt(1, QColor(116, 25, 38, 255))
        brush46 = QBrush(gradient39)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush46)
        gradient40 = QLinearGradient(0, 0, 0.5, 0)
        gradient40.setSpread(QGradient.Spread.PadSpread)
        gradient40.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient40.setColorAt(0, QColor(148, 58, 77, 255))
        gradient40.setColorAt(1, QColor(116, 25, 38, 255))
        brush47 = QBrush(gradient40)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush47)
        gradient41 = QLinearGradient(0, 0, 0.5, 0)
        gradient41.setSpread(QGradient.Spread.PadSpread)
        gradient41.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient41.setColorAt(0, QColor(148, 58, 77, 255))
        gradient41.setColorAt(1, QColor(116, 25, 38, 255))
        brush48 = QBrush(gradient41)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush48)
        gradient42 = QLinearGradient(0, 0, 0.5, 0)
        gradient42.setSpread(QGradient.Spread.PadSpread)
        gradient42.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient42.setColorAt(0, QColor(148, 58, 77, 255))
        gradient42.setColorAt(1, QColor(116, 25, 38, 255))
        brush49 = QBrush(gradient42)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush49)
        gradient43 = QLinearGradient(0, 0, 0.5, 0)
        gradient43.setSpread(QGradient.Spread.PadSpread)
        gradient43.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient43.setColorAt(0, QColor(148, 58, 77, 255))
        gradient43.setColorAt(1, QColor(116, 25, 38, 255))
        brush50 = QBrush(gradient43)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush50)
        gradient44 = QLinearGradient(0, 0, 0.5, 0)
        gradient44.setSpread(QGradient.Spread.PadSpread)
        gradient44.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient44.setColorAt(0, QColor(148, 58, 77, 255))
        gradient44.setColorAt(1, QColor(116, 25, 38, 255))
        brush51 = QBrush(gradient44)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush51)
        self.frmInfoTitulo_2.setPalette(palette8)
        self.frmInfoTitulo_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.5, y2:0, stop:0 rgb(148, 58, 77), stop:1 rgb(116, 25, 38));")
        self.frmInfoTitulo_2.setFrameShape(QFrame.Shape.Panel)
        self.frmInfoTitulo_2.setFrameShadow(QFrame.Shadow.Plain)
        self.frmInfoTitulo_2.setLineWidth(0)
        self.lblPersonagem_3 = QLabel(self.frmInfoTitulo_2)
        self.lblPersonagem_3.setObjectName(u"lblPersonagem_3")
        self.lblPersonagem_3.setGeometry(QRect(10, 0, 151, 41))
        self.lblPersonagem_3.setFont(font3)
        self.lblPersonagem_3.setAutoFillBackground(False)
        self.lblPersonagem_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblPersonagem_3.setFrameShape(QFrame.Shape.NoFrame)
        self.lblPersonagem_3.setScaledContents(False)
        self.lblPersonagem_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lblPersonagem_3.setWordWrap(False)
        self.frmInfoTitulo_3 = QFrame(self.frmInfoTitulo_2)
        self.frmInfoTitulo_3.setObjectName(u"frmInfoTitulo_3")
        self.frmInfoTitulo_3.setGeometry(QRect(0, 20, 361, 21))
        palette9 = QPalette()
        gradient45 = QLinearGradient(0, 0, 0.5, 0)
        gradient45.setSpread(QGradient.Spread.PadSpread)
        gradient45.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient45.setColorAt(0, QColor(148, 58, 77, 255))
        gradient45.setColorAt(1, QColor(116, 25, 38, 255))
        brush52 = QBrush(gradient45)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush52)
        gradient46 = QLinearGradient(0, 0, 0.5, 0)
        gradient46.setSpread(QGradient.Spread.PadSpread)
        gradient46.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient46.setColorAt(0, QColor(148, 58, 77, 255))
        gradient46.setColorAt(1, QColor(116, 25, 38, 255))
        brush53 = QBrush(gradient46)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush53)
        gradient47 = QLinearGradient(0, 0, 0.5, 0)
        gradient47.setSpread(QGradient.Spread.PadSpread)
        gradient47.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient47.setColorAt(0, QColor(148, 58, 77, 255))
        gradient47.setColorAt(1, QColor(116, 25, 38, 255))
        brush54 = QBrush(gradient47)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush54)
        gradient48 = QLinearGradient(0, 0, 0.5, 0)
        gradient48.setSpread(QGradient.Spread.PadSpread)
        gradient48.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient48.setColorAt(0, QColor(148, 58, 77, 255))
        gradient48.setColorAt(1, QColor(116, 25, 38, 255))
        brush55 = QBrush(gradient48)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush55)
        gradient49 = QLinearGradient(0, 0, 0.5, 0)
        gradient49.setSpread(QGradient.Spread.PadSpread)
        gradient49.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient49.setColorAt(0, QColor(148, 58, 77, 255))
        gradient49.setColorAt(1, QColor(116, 25, 38, 255))
        brush56 = QBrush(gradient49)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush56)
        gradient50 = QLinearGradient(0, 0, 0.5, 0)
        gradient50.setSpread(QGradient.Spread.PadSpread)
        gradient50.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient50.setColorAt(0, QColor(148, 58, 77, 255))
        gradient50.setColorAt(1, QColor(116, 25, 38, 255))
        brush57 = QBrush(gradient50)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush57)
        gradient51 = QLinearGradient(0, 0, 0.5, 0)
        gradient51.setSpread(QGradient.Spread.PadSpread)
        gradient51.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient51.setColorAt(0, QColor(148, 58, 77, 255))
        gradient51.setColorAt(1, QColor(116, 25, 38, 255))
        brush58 = QBrush(gradient51)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush58)
        gradient52 = QLinearGradient(0, 0, 0.5, 0)
        gradient52.setSpread(QGradient.Spread.PadSpread)
        gradient52.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient52.setColorAt(0, QColor(148, 58, 77, 255))
        gradient52.setColorAt(1, QColor(116, 25, 38, 255))
        brush59 = QBrush(gradient52)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush59)
        gradient53 = QLinearGradient(0, 0, 0.5, 0)
        gradient53.setSpread(QGradient.Spread.PadSpread)
        gradient53.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient53.setColorAt(0, QColor(148, 58, 77, 255))
        gradient53.setColorAt(1, QColor(116, 25, 38, 255))
        brush60 = QBrush(gradient53)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush60)
        self.frmInfoTitulo_3.setPalette(palette9)
        self.frmInfoTitulo_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.5, y2:0, stop:0 rgb(148, 58, 77), stop:1 rgb(116, 25, 38));\n"
"border-radius: 0px;")
        self.frmInfoTitulo_3.setFrameShape(QFrame.Shape.Panel)
        self.frmInfoTitulo_3.setFrameShadow(QFrame.Shadow.Plain)
        self.frmInfoTitulo_3.setLineWidth(0)
        self.frmInfoTitulo_3.raise_()
        self.lblPersonagem_3.raise_()
        self.lblClasse_2 = QLabel(self.frame_avg_stats)
        self.lblClasse_2.setObjectName(u"lblClasse_2")
        self.lblClasse_2.setGeometry(QRect(10, 50, 71, 31))
        palette10 = QPalette()
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush11)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush12)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush11)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush11)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush12)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush12)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush13)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush11)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush12)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush11)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush11)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush12)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush12)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush13)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush12)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush12)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush12)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush13)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        self.lblClasse_2.setPalette(palette10)
        self.lblClasse_2.setFont(font1)
        self.lblClasse_2.setAutoFillBackground(False)
        self.lblClasse_2.setStyleSheet(u"background-color: rgb(58, 7, 21);    /* Tom vinho escuro do fundo da caixinha */\n"
"    color: rgb(190, 141, 142);\n"
"    /*border: 1px solid #4a1a24;     Borda sutil levemente mais clara que o fundo */\n"
"    border-radius: 4px;           /* Arredondamento dos cantos */\n"
"    padding: 3px 6px;\n"
"	margin: 1px;")
        self.lblClasse_2.setFrameShape(QFrame.Shape.Panel)
        self.lblClasse_2.setScaledContents(False)
        self.lblClasse_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblClasse_2.setWordWrap(False)
        self.lblClasse_3 = QLabel(self.frame_avg_stats)
        self.lblClasse_3.setObjectName(u"lblClasse_3")
        self.lblClasse_3.setGeometry(QRect(10, 80, 71, 31))
        palette11 = QPalette()
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush11)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush12)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush11)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush11)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush12)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush12)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush13)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush11)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush12)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush11)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush11)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush12)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush12)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush13)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush12)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush12)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush12)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush13)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        self.lblClasse_3.setPalette(palette11)
        self.lblClasse_3.setFont(font1)
        self.lblClasse_3.setAutoFillBackground(False)
        self.lblClasse_3.setStyleSheet(u"background-color: rgb(58, 7, 21);    /* Tom vinho escuro do fundo da caixinha */\n"
"    color: rgb(190, 141, 142);\n"
"    /*border: 1px solid #4a1a24;     Borda sutil levemente mais clara que o fundo */\n"
"    border-radius: 4px;           /* Arredondamento dos cantos */\n"
"    padding: 3px 6px;\n"
"	margin: 1px;")
        self.lblClasse_3.setFrameShape(QFrame.Shape.Panel)
        self.lblClasse_3.setFrameShadow(QFrame.Shadow.Plain)
        self.lblClasse_3.setScaledContents(False)
        self.lblClasse_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblClasse_3.setWordWrap(False)
        self.lblClasse_3.setMargin(0)
        self.lblClasse_4 = QLabel(self.frame_avg_stats)
        self.lblClasse_4.setObjectName(u"lblClasse_4")
        self.lblClasse_4.setGeometry(QRect(10, 140, 71, 31))
        palette12 = QPalette()
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush11)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush12)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush11)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush11)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush12)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush12)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush13)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush11)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush12)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush11)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush11)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush12)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush12)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush13)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush12)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush12)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush12)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush13)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        self.lblClasse_4.setPalette(palette12)
        self.lblClasse_4.setFont(font1)
        self.lblClasse_4.setAutoFillBackground(False)
        self.lblClasse_4.setStyleSheet(u"background-color: rgb(58, 7, 21);    /* Tom vinho escuro do fundo da caixinha */\n"
"    color: rgb(190, 141, 142);\n"
"     /*border: 1px solid #4a1a24;    Borda sutil levemente mais clara que o fundo */\n"
"    border-radius: 4px;           /* Arredondamento dos cantos */\n"
"    padding: 3px 6px;\n"
"	margin: 1px;")
        self.lblClasse_4.setFrameShape(QFrame.Shape.Panel)
        self.lblClasse_4.setFrameShadow(QFrame.Shadow.Plain)
        self.lblClasse_4.setScaledContents(False)
        self.lblClasse_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblClasse_4.setWordWrap(False)
        self.lblClasse_4.setMargin(0)
        self.lblClasse_5 = QLabel(self.frame_avg_stats)
        self.lblClasse_5.setObjectName(u"lblClasse_5")
        self.lblClasse_5.setGeometry(QRect(10, 110, 71, 31))
        palette13 = QPalette()
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush11)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush12)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush11)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush11)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush12)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush12)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush13)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush11)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush12)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush11)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush11)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush12)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush12)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush13)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush12)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush12)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush12)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush13)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        self.lblClasse_5.setPalette(palette13)
        self.lblClasse_5.setFont(font1)
        self.lblClasse_5.setAutoFillBackground(False)
        self.lblClasse_5.setStyleSheet(u"background-color: rgb(58, 7, 21);    /* Tom vinho escuro do fundo da caixinha */\n"
"    color: rgb(190, 141, 142);\n"
"    /*border: 1px solid #4a1a24;     Borda sutil levemente mais clara que o fundo */\n"
"    border-radius: 4px;           /* Arredondamento dos cantos */\n"
"    padding: 3px 6px;\n"
"	margin: 1px;")
        self.lblClasse_5.setFrameShape(QFrame.Shape.Panel)
        self.lblClasse_5.setScaledContents(False)
        self.lblClasse_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblClasse_5.setWordWrap(False)
        self.lblClasse_6 = QLabel(self.frame_avg_stats)
        self.lblClasse_6.setObjectName(u"lblClasse_6")
        self.lblClasse_6.setGeometry(QRect(10, 200, 71, 31))
        palette14 = QPalette()
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush11)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush12)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush11)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush11)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush12)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush12)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush13)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush11)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush12)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush11)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush11)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush12)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush12)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush13)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush12)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush12)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush12)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush13)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        self.lblClasse_6.setPalette(palette14)
        self.lblClasse_6.setFont(font1)
        self.lblClasse_6.setAutoFillBackground(False)
        self.lblClasse_6.setStyleSheet(u"background-color: rgb(58, 7, 21);    /* Tom vinho escuro do fundo da caixinha */\n"
"    color: rgb(190, 141, 142);\n"
"    /*border: 1px solid #4a1a24;     Borda sutil levemente mais clara que o fundo */\n"
"    border-radius: 4px;           /* Arredondamento dos cantos */\n"
"    padding: 3px 6px;\n"
"	margin: 1px;")
        self.lblClasse_6.setFrameShape(QFrame.Shape.Panel)
        self.lblClasse_6.setScaledContents(False)
        self.lblClasse_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblClasse_6.setWordWrap(False)
        self.lblClasse_7 = QLabel(self.frame_avg_stats)
        self.lblClasse_7.setObjectName(u"lblClasse_7")
        self.lblClasse_7.setGeometry(QRect(10, 230, 71, 31))
        palette15 = QPalette()
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush11)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush12)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush11)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush11)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush12)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush12)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush13)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush11)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush12)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush11)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush11)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush12)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush12)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush13)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush12)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush12)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush12)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush13)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        self.lblClasse_7.setPalette(palette15)
        self.lblClasse_7.setFont(font1)
        self.lblClasse_7.setAutoFillBackground(False)
        self.lblClasse_7.setStyleSheet(u"background-color: rgb(58, 7, 21);    /* Tom vinho escuro do fundo da caixinha */\n"
"    color: rgb(190, 141, 142);\n"
"    /*border: 1px solid #4a1a24;     Borda sutil levemente mais clara que o fundo */\n"
"    border-radius: 4px;           /* Arredondamento dos cantos */\n"
"    padding: 3px 6px;\n"
"	margin: 1px;")
        self.lblClasse_7.setFrameShape(QFrame.Shape.Panel)
        self.lblClasse_7.setFrameShadow(QFrame.Shadow.Plain)
        self.lblClasse_7.setScaledContents(False)
        self.lblClasse_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblClasse_7.setWordWrap(False)
        self.lblClasse_7.setMargin(0)
        self.lblClasse_8 = QLabel(self.frame_avg_stats)
        self.lblClasse_8.setObjectName(u"lblClasse_8")
        self.lblClasse_8.setGeometry(QRect(10, 170, 71, 31))
        palette16 = QPalette()
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush11)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush12)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush1)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush11)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush11)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush12)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush12)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush13)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush11)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush12)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush1)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush11)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush11)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush12)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush12)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush13)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush12)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush1)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush12)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush12)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush13)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        self.lblClasse_8.setPalette(palette16)
        self.lblClasse_8.setFont(font1)
        self.lblClasse_8.setAutoFillBackground(False)
        self.lblClasse_8.setStyleSheet(u"background-color: rgb(58, 7, 21);    /* Tom vinho escuro do fundo da caixinha */\n"
"    color: rgb(190, 141, 142);\n"
"    /*border: 1px solid #4a1a24;     Borda sutil levemente mais clara que o fundo */\n"
"    border-radius: 4px;           /* Arredondamento dos cantos */\n"
"    padding: 3px 6px;\n"
"	margin: 1px;")
        self.lblClasse_8.setFrameShape(QFrame.Shape.Panel)
        self.lblClasse_8.setFrameShadow(QFrame.Shadow.Plain)
        self.lblClasse_8.setScaledContents(False)
        self.lblClasse_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblClasse_8.setWordWrap(False)
        self.lblClasse_8.setMargin(0)
        self.lblHpInt = QLabel(self.frame_avg_stats)
        self.lblHpInt.setObjectName(u"lblHpInt")
        self.lblHpInt.setGeometry(QRect(90, 50, 30, 31))
        self.lblHpInt.setFont(font3)
        self.lblHpInt.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.lblAtkInt = QLabel(self.frame_avg_stats)
        self.lblAtkInt.setObjectName(u"lblAtkInt")
        self.lblAtkInt.setGeometry(QRect(90, 80, 30, 31))
        self.lblAtkInt.setFont(font3)
        self.lblAtkInt.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblSpdInt = QLabel(self.frame_avg_stats)
        self.lblSpdInt.setObjectName(u"lblSpdInt")
        self.lblSpdInt.setGeometry(QRect(90, 140, 30, 31))
        self.lblSpdInt.setFont(font3)
        self.lblSpdInt.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblSklInt = QLabel(self.frame_avg_stats)
        self.lblSklInt.setObjectName(u"lblSklInt")
        self.lblSklInt.setGeometry(QRect(90, 110, 30, 31))
        self.lblSklInt.setFont(font3)
        self.lblSklInt.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblResInt = QLabel(self.frame_avg_stats)
        self.lblResInt.setObjectName(u"lblResInt")
        self.lblResInt.setGeometry(QRect(90, 230, 30, 31))
        self.lblResInt.setFont(font3)
        self.lblResInt.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblDefInt = QLabel(self.frame_avg_stats)
        self.lblDefInt.setObjectName(u"lblDefInt")
        self.lblDefInt.setGeometry(QRect(90, 200, 30, 31))
        self.lblDefInt.setFont(font3)
        self.lblDefInt.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblLckInt = QLabel(self.frame_avg_stats)
        self.lblLckInt.setObjectName(u"lblLckInt")
        self.lblLckInt.setGeometry(QRect(90, 170, 30, 31))
        self.lblLckInt.setFont(font3)
        self.lblLckInt.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame = QFrame(self.frame_avg_stats)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(5, 45, 151, 221))
        self.frame.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 80);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.frame.setLineWidth(0)
        self.portrait = QWidget(self.frame_avg_stats)
        self.portrait.setObjectName(u"portrait")
        self.portrait.setGeometry(QRect(50, 0, 361, 361))
        self.portrait.setAutoFillBackground(False)
        self.portrait.setStyleSheet(u"border-image: url(:/portraits/Kliff.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.lblResDec = QLabel(self.frame_avg_stats)
        self.lblResDec.setObjectName(u"lblResDec")
        self.lblResDec.setGeometry(QRect(120, 227, 30, 31))
        font6 = QFont()
        font6.setFamilies([u"Microsoft YaHei"])
        font6.setPointSize(12)
        self.lblResDec.setFont(font6)
        self.lblResDec.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblResDec.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.lblAtkDec = QLabel(self.frame_avg_stats)
        self.lblAtkDec.setObjectName(u"lblAtkDec")
        self.lblAtkDec.setGeometry(QRect(120, 77, 30, 31))
        self.lblAtkDec.setFont(font6)
        self.lblAtkDec.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblAtkDec.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.lblSpdDec = QLabel(self.frame_avg_stats)
        self.lblSpdDec.setObjectName(u"lblSpdDec")
        self.lblSpdDec.setGeometry(QRect(120, 137, 30, 31))
        self.lblSpdDec.setFont(font6)
        self.lblSpdDec.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblSpdDec.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.lblLckDec = QLabel(self.frame_avg_stats)
        self.lblLckDec.setObjectName(u"lblLckDec")
        self.lblLckDec.setGeometry(QRect(120, 167, 30, 31))
        self.lblLckDec.setFont(font6)
        self.lblLckDec.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblLckDec.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.lblSklDec = QLabel(self.frame_avg_stats)
        self.lblSklDec.setObjectName(u"lblSklDec")
        self.lblSklDec.setGeometry(QRect(120, 107, 30, 31))
        self.lblSklDec.setFont(font6)
        self.lblSklDec.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblSklDec.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.lblDefDec = QLabel(self.frame_avg_stats)
        self.lblDefDec.setObjectName(u"lblDefDec")
        self.lblDefDec.setGeometry(QRect(120, 197, 30, 31))
        self.lblDefDec.setFont(font6)
        self.lblDefDec.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblDefDec.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.lblHpDec = QLabel(self.frame_avg_stats)
        self.lblHpDec.setObjectName(u"lblHpDec")
        self.lblHpDec.setGeometry(QRect(120, 47, 30, 31))
        self.lblHpDec.setFont(font6)
        self.lblHpDec.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lblHpDec.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.widget = QWidget(self.frame_avg_stats)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setGeometry(QRect(163, 225, 191, 41))
        self.widget.setStyleSheet(u" \n"
"    background-color: qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:1, y2:0.5, stop:0.126 rgba(153, 36, 32, 252), stop:0.705263 rgba(65, 12, 19, 237));\n"
"    border: 1px solid #7a1d28;\n"
"    \n"
"    /* Cantos em ordem: topo-esq, topo-dir, baixo-dir, baixo-esq */\n"
"    /* Cria a curva em cima/embaixo mantendo as laterais retas */\n"
"    border-top-left-radius: 90px 13px;\n"
"    border-top-right-radius: 90px 13px;\n"
"    border-bottom-right-radius: 90px 13px;\n"
"    border-bottom-left-radius: 90px 13px;\n"
"    \n"
"")
        self.lbl_nome_avg = QLabel(self.widget)
        self.lbl_nome_avg.setObjectName(u"lbl_nome_avg")
        self.lbl_nome_avg.setGeometry(QRect(0, 0, 191, 41))
        self.lbl_nome_avg.setFont(font1)
        self.lbl_nome_avg.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.lbl_nome_avg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.portrait.raise_()
        self.frame.raise_()
        self.lblClasse_2.raise_()
        self.lblClasse_3.raise_()
        self.lblClasse_4.raise_()
        self.lblClasse_5.raise_()
        self.lblClasse_6.raise_()
        self.lblClasse_7.raise_()
        self.lblClasse_8.raise_()
        self.lblHpInt.raise_()
        self.lblAtkInt.raise_()
        self.lblSpdInt.raise_()
        self.lblSklInt.raise_()
        self.lblResInt.raise_()
        self.lblDefInt.raise_()
        self.lblLckInt.raise_()
        self.lblResDec.raise_()
        self.lblAtkDec.raise_()
        self.lblSpdDec.raise_()
        self.lblLckDec.raise_()
        self.lblSklDec.raise_()
        self.lblDefDec.raise_()
        self.lblHpDec.raise_()
        self.frmInfoTitulo_2.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 382, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblPersonagem.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.lblClasse.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.lblNivel.setText(QCoreApplication.translate("MainWindow", u"Level", None))
        self.btnCalcular.setText(QCoreApplication.translate("MainWindow", u"CALCULATE", None))
        self.lblPersonagem_2.setText(QCoreApplication.translate("MainWindow", u"Unit Info", None))
        self.chkAuto.setText(QCoreApplication.translate("MainWindow", u"Auto Calculate", None))
        self.lblPersonagem_3.setText(QCoreApplication.translate("MainWindow", u"Average Stats", None))
        self.lblClasse_2.setText(QCoreApplication.translate("MainWindow", u"HP", None))
        self.lblClasse_3.setText(QCoreApplication.translate("MainWindow", u"ATK", None))
        self.lblClasse_4.setText(QCoreApplication.translate("MainWindow", u"SPD", None))
        self.lblClasse_5.setText(QCoreApplication.translate("MainWindow", u"SKILL", None))
        self.lblClasse_6.setText(QCoreApplication.translate("MainWindow", u"DEF", None))
        self.lblClasse_7.setText(QCoreApplication.translate("MainWindow", u"RES", None))
        self.lblClasse_8.setText(QCoreApplication.translate("MainWindow", u"LCK", None))
        self.lblHpInt.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lblAtkInt.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lblSpdInt.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lblSklInt.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lblResInt.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lblDefInt.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lblLckInt.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lblResDec.setText("")
        self.lblAtkDec.setText("")
        self.lblSpdDec.setText("")
        self.lblLckDec.setText("")
        self.lblSklDec.setText("")
        self.lblDefDec.setText("")
        self.lblHpDec.setText("")
        self.lbl_nome_avg.setText("")
    # retranslateUi

