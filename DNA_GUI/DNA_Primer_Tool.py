from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout
from dnatools_gui import dnatools_gui as dna, AA_table as AA, PRIMER_TOOLS as PT, Dilution_tools as DT
import os
from pathlib import Path
import re
import sys
from decimal import *

# Sequence = ""

class DNA_GUI(QtWidgets.QMainWindow):
	# = QtGui.QFont()
	#.setFontSize(18)
	def __init__(self):
		super(DNA_GUI, self).__init__()
		self.setWindowTitle("DNA_Tools")
		self.resize(580, 433)
		self.setMinimumSize(QtCore.QSize(580, 433))
		self.setMaximumSize(QtCore.QSize(580, 433))
		self.centralwidget = QtWidgets.QWidget()
		self.centralwidget.setObjectName("centralwidget")
		self.input_ouput_tabs = QtWidgets.QTabWidget(self.centralwidget)
		self.input_ouput_tabs.setGeometry(QtCore.QRect(0, 0, 581, 411))
		self.input_ouput_tabs.setMinimumSize(QtCore.QSize(581, 411))
		self.input_ouput_tabs.setMaximumSize(QtCore.QSize(581, 411))
		self.input_ouput_tabs.setObjectName("input_ouput_tabs")
		self.input_ouput_tabs.setAutoFillBackground(False)
		self.input_ouput_tabs.setStyleSheet("color:rgb(0, 102, 0)")
		self.Tab1 = QtWidgets.QWidget()
		self.Tab1.setObjectName("Tab1")
		self.tool_select = QtWidgets.QComboBox(self.Tab1)
		self.tool_select.setGeometry(QtCore.QRect(23, 20, 241, 26))
		self.tool_select.setObjectName("tool_select")
		self.tool_select.addItem("")
		self.tool_select.addItem("")
		self.tool_select.addItem("")
		self.tool_select.addItem("")
		self.tool_select.addItem("")
		self.tool_select.addItem("")
		self.Input_text = QtWidgets.QPlainTextEdit(self.Tab1)
		self.Input_text.setGeometry(QtCore.QRect(20, 60, 541, 261))
		self.Input_text.setObjectName("Input_text")
		self.submit_button = QtWidgets.QPushButton(self.Tab1)
		self.submit_button.setGeometry(QtCore.QRect(150, 340, 113, 32))
		self.submit_button.setObjectName("submit_button")
		self.submit_button.clicked.connect(self.EX)
		self.reset_button = QtWidgets.QPushButton(self.Tab1)
		self.reset_button.setGeometry(QtCore.QRect(300, 340, 113, 32))
		self.reset_button.setObjectName("reset_button")
		self.reset_button.clicked.connect(self.RS)
		self.input_ouput_tabs.addTab(self.Tab1, "")
		self.Tab2 = QtWidgets.QWidget()
		self.Tab2.setObjectName("Tab2")
		self.Output_text = QtWidgets.QPlainTextEdit(self.Tab2)
# 		self.Output_text = QtWidgets.QPlainTextEdit()
		self.Output_text.setGeometry(QtCore.QRect(0, 0, 571, 381))
		self.Output_text.setObjectName("Output_text")
		self.input_ouput_tabs.addTab(self.Tab2, "")
		self.setCentralWidget(self.centralwidget)
		self.Tab3 = QtWidgets.QWidget()
		self.Tab3.setObjectName("Tab3")
		self.input_ouput_tabs.addTab(self.Tab3, "")
		
		self.Tab4 = QtWidgets.QWidget()
		self.Tab4.setObjectName("Tab4")
		self.input_ouput_tabs.addTab(self.Tab4, "")	
		self.codon_table = QtWidgets.QTextEdit(self.Tab3)
		self.codon_table.setGeometry(QtCore.QRect(0, 0, 571, 381))
		self.codon_table.setObjectName("codon_table")
		self.codon_table.setText(str(AA.table))
		self.codon_table.setReadOnly(True)
		self.nn_primer_input = QtWidgets.QPlainTextEdit(self.Tab4)
		self.nn_primer_input.setGeometry(QtCore.QRect(30, 80, 511, 78))
		self.nn_primer_input.setObjectName("Primer_in")
		self.near_neighbor = QtWidgets.QComboBox(self.Tab4)
		self.near_neighbor.setGeometry(QtCore.QRect(30, 50, 104, 26))
		self.near_neighbor.setObjectName("comboBox")
		self.concentration = QtWidgets.QDoubleSpinBox(self.Tab4)
		self.concentration.setGeometry(QtCore.QRect(160, 50, 68, 24))
		self.concentration.setObjectName("concentration")
		self.micro_molar = QtWidgets.QLabel(self.Tab4)
		self.micro_molar.setGeometry(QtCore.QRect(160, 30, 63, 16))
		self.micro_molar.setObjectName("micro_molar")
		self.salt_conc = QtWidgets.QDoubleSpinBox(self.Tab4)
		self.salt_conc.setGeometry(QtCore.QRect(260, 50, 68, 24))
		self.salt_conc.setObjectName("salt_conc")
		self.salt_conc.setMaximum(1000.00)
		self.salt_conc.setMinimum(50.00)
		self.mili_molar = QtWidgets.QLabel(self.Tab4)
		self.mili_molar.setGeometry(QtCore.QRect(260, 30, 60, 16))
		self.mili_molar.setObjectName("mili_molar")
		self.pt_submision = QtWidgets.QPushButton(self.Tab4)
		self.pt_submision.setGeometry(QtCore.QRect(350, 50, 113, 21))
		self.pt_submision.setObjectName("pushButton")
		self.nn_primer_output = QtWidgets.QPlainTextEdit(self.Tab4)
		self.nn_primer_output.setGeometry(QtCore.QRect(30, 200, 511, 120))
		self.nn_primer_output.setObjectName("plainTextEdit_2")
		self.clear_pt = QtWidgets.QPushButton(self.Tab4)
		self.clear_pt.setGeometry(QtCore.QRect(230, 160, 113, 32))
		self.clear_pt.setObjectName("pushButton_2")
		self.nn_primer_output.setReadOnly(True)
		self.advice = QtWidgets.QLabel(self.Tab4)
		self.advice.setGeometry(QtCore.QRect(20, 330, 530, 50))
		self.advice.setObjectName("advice")
		self.near_neighbor.addItem("")
		self.pt_submision.clicked.connect(self.PrimerTool)
		self.clear_pt.clicked.connect(self.PT_RS)
		self.notify = QtWidgets.QLabel(self.Tab1)
		self.notify.setObjectName('notify')
		self.notify.setGeometry(QtCore.QRect(300, 20, 241, 26))
		self.notify.hide()
		
		
		
		self.Tab5 = QtWidgets.QWidget()
		self.Tab5.setObjectName("Tab5")
		self.input_ouput_tabs.addTab(self.Tab5, "")
		self.input_M1 = QtWidgets.QLineEdit(self.Tab5)
		self.input_M1.setGeometry(QtCore.QRect(440, 50, 61, 21))
		self.input_M1.setObjectName("input_M1")
		self.M1_unit = QtWidgets.QComboBox(self.Tab5)
		self.M1_unit.setGeometry(QtCore.QRect(500, 50, 52, 21))
		self.M1_unit.setObjectName("M1_unit")
		self.M1_unit.addItem("")
		self.M1_unit.addItem("")
		self.M1_unit.addItem("")
		self.M1_unit.addItem("")
		self.multiply1 = QtWidgets.QLabel(self.Tab5)
		self.multiply1.setGeometry(QtCore.QRect(140, 50, 16, 21))
# 		self.multiply1.font.setPointSize(18)
# 		self.multiply1.setFont(font)
# 		self.multiply1.setObjectName("multiply1")
		self.V1_Unit = QtWidgets.QComboBox(self.Tab5)
		self.V1_Unit.setGeometry(QtCore.QRect(90, 50, 50, 21))
		self.V1_Unit.setObjectName("V1_Unit")
		self.V1_Unit.addItem("")
		self.V1_Unit.addItem("")
		self.V1_Unit.addItem("")
		self.V1_Unit.addItem("")
# 		self.V1_Unit.addItem("")
		self.V1_Unit.setItemText(4, "")
		self.equal1 = QtWidgets.QLabel(self.Tab5)
		self.equal1.setGeometry(QtCore.QRect(280, 50, 16, 21))
# 		self.equal1.setFont(font)
		self.equal1.setObjectName("equal1")
		self.input_V1 = QtWidgets.QLineEdit(self.Tab5)
		self.input_V1.setGeometry(QtCore.QRect(10, 50, 86, 21))
		self.input_V1.setObjectName("input_V1")
		self.input_V2 = QtWidgets.QLineEdit(self.Tab5)
		self.input_V2.setGeometry(QtCore.QRect(300, 50, 61, 21))
		self.input_V2.setObjectName("input_V2")
		self.multiply2 = QtWidgets.QLabel(self.Tab5)
		self.multiply2.setGeometry(QtCore.QRect(420, 50, 21, 21))
# 		self.multiply2.setFont(font)
		self.multiply2.setObjectName("multiply2")
		self.M2_unit = QtWidgets.QComboBox(self.Tab5)
		self.M2_unit.setGeometry(QtCore.QRect(230, 50, 52, 21))
		self.M2_unit.setObjectName("M2_unit")
		self.M2_unit.addItem("")
		self.M2_unit.addItem("")
		self.M2_unit.addItem("")
		self.M2_unit.addItem("")
		self.V2_Unit = QtWidgets.QComboBox(self.Tab5)
		self.V2_Unit.setGeometry(QtCore.QRect(360, 50, 51, 21))
		self.V2_Unit.setObjectName("V2_Unit")
		self.V2_Unit.addItem("")
		self.V2_Unit.addItem("")
		self.V2_Unit.addItem("")
		self.V2_Unit.addItem("")
		self.input_M2 = QtWidgets.QLineEdit(self.Tab5)
		self.input_M2.setGeometry(QtCore.QRect(170, 50, 61, 21))
		self.input_M2.setObjectName("input_M2")
		self.Concentration1 = QtWidgets.QLabel(self.Tab5)
		self.Concentration1.setGeometry(QtCore.QRect(29, 30, 101, 20))
		self.Concentration1.setObjectName("Concentration1")
		self.Volume1 = QtWidgets.QLabel(self.Tab5)
		self.Volume1.setGeometry(QtCore.QRect(460, 30, 81, 20))
		self.Volume1.setObjectName("Volume1")
		self.Volume2 = QtWidgets.QLabel(self.Tab5)
		self.Volume2.setGeometry(QtCore.QRect(320, 30, 90, 20))
		self.Volume2.setObjectName("Volume2")
		self.Concentration2 = QtWidgets.QLabel(self.Tab5)
		self.Concentration2.setGeometry(QtCore.QRect(180, 30, 101, 20))
		self.Parenth = QtWidgets.QLabel(self.Tab5)
		self.Parenth2 = QtWidgets.QLabel(self.Tab5)
		self.Parenth.setGeometry(QtCore.QRect(410,50,16,21))
		self.Parenth2.setGeometry(QtCore.QRect(160,50,16,21))
		self.Parenth.setObjectName("Parenth")
		self.Parenth2.setObjectName("Parenth2")
		self.Concentration2.setObjectName("Concentration2")
		self.input_mass_mw = QtWidgets.QLineEdit(self.Tab5)
		self.input_mass_mw.setGeometry(QtCore.QRect(160, 190, 61, 21))
		self.input_mass_mw.setObjectName("input_mass_mw")
		self.divide1 = QtWidgets.QLabel(self.Tab5)
		self.divide1.setGeometry(QtCore.QRect(280, 190, 16, 21))
# 		self.divide1.setFont(font)
		self.divide1.setObjectName("divide1")
		self.M_fromMW_unit = QtWidgets.QComboBox(self.Tab5)
		self.M_fromMW_unit.setGeometry(QtCore.QRect(80, 190, 51, 21))
		self.M_fromMW_unit.setObjectName("M_fromMW_unit")
		self.M_fromMW_unit.addItem("")
		self.M_fromMW_unit.addItem("")
		self.M_fromMW_unit.addItem("")
		self.M_fromMW_unit.addItem("")
		self.Mass_MW_unit = QtWidgets.QComboBox(self.Tab5)
		self.Mass_MW_unit.setGeometry(QtCore.QRect(220, 190, 51, 22))
		self.Mass_MW_unit.setObjectName("Mass_MW_unit")
		self.Mass_MW_unit.addItem("")
		self.Mass_MW_unit.addItem("")
		self.Mass_MW_unit.addItem("")
		self.Mass_MW_unit.addItem("")
		self.multipy3 = QtWidgets.QLabel(self.Tab5)
		self.multipy3.setGeometry(QtCore.QRect(420, 190, 21, 21))
# 		self.multipy3.setFont(font)
		self.multipy3.setObjectName("multipy3")
		self.input_Vol_mw = QtWidgets.QLineEdit(self.Tab5)
		self.input_Vol_mw.setGeometry(QtCore.QRect(310, 190, 61, 21))
		self.input_Vol_mw.setObjectName("input_Vol_mw")
		self.Mass1 = QtWidgets.QLabel(self.Tab5)
		self.Mass1.setGeometry(QtCore.QRect(180, 170, 81, 20))
		self.Mass1.setObjectName("Mass1")
		self.Vol3 = QtWidgets.QLabel(self.Tab5)
		self.Vol3.setGeometry(QtCore.QRect(330, 170, 51, 20))
		self.Vol3.setObjectName("Vol3")
		self.input_C_mw = QtWidgets.QLineEdit(self.Tab5)
		self.input_C_mw.setGeometry(QtCore.QRect(20, 190, 61, 21))
		self.input_C_mw.setObjectName("input_C_mw")
		self.Equal2 = QtWidgets.QLabel(self.Tab5)
		self.Equal2.setGeometry(QtCore.QRect(140, 190, 16, 21))
# 		self.Equal2.setFont(font)
		self.Equal2.setObjectName("Equal2")
		self.Concentration3 = QtWidgets.QLabel(self.Tab5)
		self.Concentration3.setGeometry(QtCore.QRect(29, 170, 101, 20))
		self.Concentration3.setObjectName("Concentration3")
		self.input_MW_mw = QtWidgets.QLineEdit(self.Tab5)
		self.input_MW_mw.setGeometry(QtCore.QRect(440, 190, 61, 21))
		self.input_MW_mw.setObjectName("input_MW_mw")
		self.MW = QtWidgets.QLabel(self.Tab5)
		self.MW.setGeometry(QtCore.QRect(440, 170, 111, 20))
# 		self.MW.setFont(font)
		self.MW.setLineWidth(0)
		self.MW.setObjectName("MW")
		self.parenthesis1 = QtWidgets.QLabel(self.Tab5)
		self.parenthesis1.setGeometry(QtCore.QRect(300, 190, 16, 21))
# 		self.parenthesis1.setFont(font)
		self.parenthesis1.setObjectName("parenthesis1")
		self.parenthesis2 = QtWidgets.QLabel(self.Tab5)
		self.parenthesis2.setGeometry(QtCore.QRect(550, 190, 16, 21))
# 		self.parenthesis2.setFont(font)
		self.parenthesis2.setObjectName("parenthesis2")
		self.Vol_fromMW_unit = QtWidgets.QComboBox(self.Tab5)
		self.Vol_fromMW_unit.setGeometry(QtCore.QRect(370, 190, 51, 21))
		self.Vol_fromMW_unit.setObjectName("Vol_fromMW_unit")
		self.Vol_fromMW_unit.addItem("")
		self.Vol_fromMW_unit.addItem("")
		self.Vol_fromMW_unit.addItem("")
		self.Vol_fromMW_unit.addItem("")
		self.g_per_mol = QtWidgets.QLineEdit(self.Tab5)
		self.g_per_mol.setGeometry(QtCore.QRect(503, 190, 41, 21))
		self.g_per_mol.setObjectName("g_per_mol")
		self.Vol4 = QtWidgets.QLabel(self.Tab5)
		self.Vol4.setGeometry(QtCore.QRect(20, 320, 101, 20))
		self.Vol4.setObjectName("Vol4")
		self.resus_vol_unit = QtWidgets.QComboBox(self.Tab5)
		self.resus_vol_unit.setGeometry(QtCore.QRect(80, 340, 51, 21))
		self.resus_vol_unit.setObjectName("resus_vol_unit")
		self.resus_vol_unit.addItem("")
		self.resus_vol_unit.addItem("")
		self.resus_vol_unit.addItem("")
		self.resus_vol_unit.addItem("")
		self.input_Vol_resus = QtWidgets.QLineEdit(self.Tab5)
		self.input_Vol_resus.setGeometry(QtCore.QRect(20, 340, 61, 21))
		self.input_Vol_resus.setObjectName("input_Vol_resus")
		self.equal3 = QtWidgets.QLabel(self.Tab5)
		self.equal3.setGeometry(QtCore.QRect(140, 340, 16, 21))
# 		self.equal3.setFont(font)
		self.equal3.setObjectName("equal3")
		self.resus_mass_unit = QtWidgets.QComboBox(self.Tab5)
		self.resus_mass_unit.setGeometry(QtCore.QRect(220, 340, 65, 22))
		self.resus_mass_unit.setObjectName("resus_mass_unit")
		self.resus_mass_unit.addItem("")
		self.resus_mass_unit.addItem("")
		self.resus_mass_unit.addItem("")
		self.resus_mass_unit.addItem("")
		self.input_mass_resus = QtWidgets.QLineEdit(self.Tab5)
		self.input_mass_resus.setGeometry(QtCore.QRect(160, 340, 61, 21))
		self.input_mass_resus.setObjectName("input_mass_resus")
		self.mass2 = QtWidgets.QLabel(self.Tab5)
		self.mass2.setGeometry(QtCore.QRect(180, 320, 81, 20))
		self.mass2.setObjectName("mass2")
		self.divide2 = QtWidgets.QLabel(self.Tab5)
		self.divide2.setGeometry(QtCore.QRect(285, 340, 16, 21))
# 		self.divide2.setFont(font)
		self.divide2.setObjectName("divide2")
		self.Concentration4 = QtWidgets.QLabel(self.Tab5)
		self.Concentration4.setGeometry(QtCore.QRect(299, 320, 141, 20))
		self.Concentration4.setObjectName("Concentration4")
		self.resus_M_unit = QtWidgets.QComboBox(self.Tab5)
		self.resus_M_unit.setGeometry(QtCore.QRect(360, 340, 52, 21))
		self.resus_M_unit.setObjectName("resus_M_unit")
		self.resus_M_unit.addItem("")
		self.resus_M_unit.addItem("")
		self.resus_M_unit.addItem("")
		self.resus_M_unit.addItem("")
		self.input_C_resus = QtWidgets.QLineEdit(self.Tab5)
		self.input_C_resus.setGeometry(QtCore.QRect(300, 340, 61, 21))
		self.input_C_resus.setObjectName("input_C_resus")
		self.Descript1 = QtWidgets.QLabel(self.Tab5)
		self.Descript1.setGeometry(QtCore.QRect(1, 80, 221, 32))
		self.Descript1.setObjectName("Descript1")
		self.Descript2 = QtWidgets.QLabel(self.Tab5)
		self.Descript2.setGeometry(QtCore.QRect(1, 220, 161, 16))
		self.Descript2.setObjectName("Descript2")
		self.Descript3 = QtWidgets.QLabel(self.Tab5)
		self.Descript3.setGeometry(QtCore.QRect(1, 365, 221, 16))
		self.Descript3.setObjectName("Descript3")
		self.calc_go1 = QtWidgets.QPushButton(self.Tab5)
		self.calc_go2 = QtWidgets.QPushButton(self.Tab5)
		self.calc_go3 = QtWidgets.QPushButton(self.Tab5)
		self.calc_go1.setObjectName("calc_go1")
		self.calc_go2.setObjectName("calc_go2")
		self.calc_go3.setObjectName("calc_go3")
		self.calc_go1.setGeometry(QtCore.QRect(240, 80, 100, 16))
		self.calc_go2.setGeometry(QtCore.QRect(240, 220, 100, 16))
		self.calc_go3.setGeometry(QtCore.QRect(240, 365, 100, 16))
		self.border1 = QtWidgets.QLabel(self.Tab5)
		self.border2 = QtWidgets.QLabel(self.Tab5)
		self.border1.setObjectName("border1")
		self.border2.setObjectName("border2")
		self.border1.setGeometry(QtCore.QRect(0, 130, 580, 16))
		self.border2.setGeometry(QtCore.QRect(0, 280, 580, 16))
		self.g_per_mol.setReadOnly(True)
		self.calc_go1.clicked.connect(self.known_molarity_dilution)
		self.calc_go2.clicked.connect(self.Conc)
		self.calc_go3.clicked.connect(self.RESUS)
		self.input_V1.setReadOnly(False)
		self.explanation = QtWidgets.QLabel(self.Tab5)
		self.explanation.setObjectName("explanation")
		self.explanation.setGeometry(QtCore.QRect(345,70,201,71))
		self.explanation.hide()
# 		self.V1_Unit.hide()
		self.retranslateUi(DNA_GUI)
		self.input_ouput_tabs.setCurrentIndex(0)
		self.onlyInt = QtGui.QIntValidator()
		self.input_M1.setValidator(self.onlyInt)
		self.input_M2.setValidator(self.onlyInt)
		self.input_V2.setValidator(self.onlyInt)
		self.input_mass_mw.setValidator(self.onlyInt)
		self.input_Vol_mw.setValidator(self.onlyInt)
		self.input_MW_mw.setValidator(self.onlyInt)
		self.input_mass_resus.setValidator(self.onlyInt)
		self.input_C_resus.setValidator(self.onlyInt)


	def retranslateUi(self, DNA_GUI):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("DNA_Tools", "DNA Tools"))
		self.tool_select.setItemText(0, _translate("DNA_Tools", "~Select A Tool~"))
		self.tool_select.setItemText(1, _translate("DNA_Tools", "Transcription"))
		self.tool_select.setItemText(2, _translate("DNA_Tools", "Reverse Transcription"))
		self.tool_select.setItemText(3, _translate("DNA_Tools", "Reverse Compliment"))
		self.tool_select.setItemText(4, _translate("DNA_Tools", "Translation (1 letter)"))
		self.tool_select.setItemText(5, _translate("DNA_Tools", "Translation (3 letter)"))
		
		self.near_neighbor.setItemText(0, _translate("DNA_Tools", "Primer Tool"))
		
		self.concentration.setValue(0.5)
		self.salt_conc.setValue(50.0)

		self.Input_text.setPlaceholderText(_translate("DNA_Tools", ">Input sequence i.e. ATG or atg (or paste with ctrl + v)"))
		self.submit_button.setText(_translate("DNA_Tools", "Submit"))
		self.reset_button.setText(_translate("DNA_Tools", "Reset"))
		self.micro_molar.setText(_translate("DNA_Tools", "[oligo] μM"))
		self.mili_molar.setText(_translate("DNA_Tools", "[Na+] mM"))
		self.pt_submision.setText(_translate("DNA_Tools", "SUBMIT"))
		self.clear_pt.setText(_translate("DNA_Tools", "CLEAR"))
		self.advice.setText(_translate("DNA_Tools", "Primer design tips:\ni) Limit repeating A/T's (these decrease the local TM within the primer)\nii) begin/end with G or C (This increases the primer-DNA stability at the primers termini)"))
		self.nn_primer_input.setPlaceholderText(_translate("DNA_Tools", ">Input primer sequence"))
		self.nn_primer_output.setPlaceholderText(_translate("DNA_Tools", "Primer info (i.e. Tm˚c, %GC, etc) displayed here"))
		self.notify.setText(_translate("DNA_Tools", "RESULTS IN OUTPUT TAB"))
		self.input_M1.setPlaceholderText(_translate("DNA_Tools", "M1"))
		self.input_V1.setPlaceholderText(_translate("DNA_Tools", "V1"))
		self.input_M2.setPlaceholderText(_translate("DNA_Tools", "M2"))
		self.input_V2.setPlaceholderText(_translate("DNA_Tools", "V2"))
		
		self.input_ouput_tabs.setTabText(self.input_ouput_tabs.indexOf(self.Tab1), _translate("DNA_Tools", "DNA Tool (Input)"))
		self.input_ouput_tabs.setTabText(self.input_ouput_tabs.indexOf(self.Tab2), _translate("DNA_Tools", "~Empty~"))
		self.input_ouput_tabs.setTabText(self.input_ouput_tabs.indexOf(self.Tab3), _translate("DNA_Tools", "Codon Table"))
		self.input_ouput_tabs.setTabText(self.input_ouput_tabs.indexOf(self.Tab4), _translate("DNA_Tools", "Primer tool"))
		
		self.input_ouput_tabs.setTabText(self.input_ouput_tabs.indexOf(self.Tab5), _translate("DNA_Tools", "Dilution Tools"))
		
		self.M1_unit.setItemText(0, _translate("DNA_Tools", "M"))
		self.M1_unit.setItemText(1, _translate("DNA_Tools", "mM"))
		self.M1_unit.setItemText(2, _translate("DNA_Tools", "uΜ"))
		self.M1_unit.setItemText(3, _translate("DNA_Tools", "nM"))
		
		self.multiply1.setText(_translate("DNA_Tools", "="))
		
		self.V1_Unit.setItemText(0, _translate("DNA_Tools", "L"))
		self.V1_Unit.setItemText(1, _translate("DNA_Tools", "ml"))
		self.V1_Unit.setItemText(2, _translate("DNA_Tools", "ul"))
		self.V1_Unit.setItemText(3, _translate("DNA_Tools", "nl"))
		
		self.equal1.setText(_translate("DNA_Tools", "x"))
		self.multiply2.setText(_translate("DNA_Tools", " ÷"))
		
		self.M2_unit.setItemText(0, _translate("DNA_Tools", "M"))
		self.M2_unit.setItemText(1, _translate("DNA_Tools", "mM"))
		self.M2_unit.setItemText(2, _translate("DNA_Tools", "uΜ"))
		self.M2_unit.setItemText(3, _translate("DNA_Tools", "nM"))
		
		self.V2_Unit.setItemText(0, _translate("DNA_Tools", "L"))
		self.V2_Unit.setItemText(1, _translate("DNA_Tools", "ml"))
		self.V2_Unit.setItemText(2, _translate("DNA_Tools", "ul"))
		self.V2_Unit.setItemText(3, _translate("DNA_Tools", "nl"))
		
		self.Concentration1.setText(_translate("DNA_Tools", "Required Vol"))
		self.Volume1.setText(_translate("DNA_Tools", "Initial [C]"))
		self.Volume2.setText(_translate("DNA_Tools", "Target Volume"))
		self.Concentration2.setText(_translate("DNA_Tools", "Target [C]"))
		self.divide1.setText(_translate("DNA_Tools", "÷"))
		
		self.M_fromMW_unit.setItemText(0, _translate("DNA_Tools", "M"))
		self.M_fromMW_unit.setItemText(1, _translate("DNA_Tools", "mM"))
		self.M_fromMW_unit.setItemText(2, _translate("DNA_Tools", "μΜ"))
		self.M_fromMW_unit.setItemText(3, _translate("DNA_Tools", "nM"))
		
		self.Mass_MW_unit.setItemText(0, _translate("DNA_Tools", "g"))
		self.Mass_MW_unit.setItemText(1, _translate("DNA_Tools", "mg"))
		self.Mass_MW_unit.setItemText(2, _translate("DNA_Tools", "ug"))
		self.Mass_MW_unit.setItemText(3, _translate("DNA_Tools", "ng"))
		
		self.multipy3.setText(_translate("DNA_Tools", " x"))
		self.Mass1.setText(_translate("DNA_Tools", "Mass"))
		self.Vol3.setText(_translate("DNA_Tools", "Volume"))
		self.Equal2.setText(_translate("DNA_Tools", "="))
		self.Concentration3.setText(_translate("DNA_Tools", "Concentration"))
		self.MW.setText(_translate("DNA_Tools", "Molecular Weight"))
		self.parenthesis1.setText(_translate("DNA_Tools", "("))
		self.parenthesis2.setText(_translate("DNA_Tools", ")"))
		
		self.Vol_fromMW_unit.setItemText(0, _translate("DNA_Tools", "L"))
		self.Vol_fromMW_unit.setItemText(1, _translate("DNA_Tools", "ml"))
		self.Vol_fromMW_unit.setItemText(2, _translate("DNA_Tools", "ul"))
		self.Vol_fromMW_unit.setItemText(3, _translate("DNA_Tools", "nl"))
		
		self.g_per_mol.setText(_translate("DNA_Tools", "g/mol"))
		self.Vol4.setText(_translate("DNA_Tools", "Volume Needed"))
		
		self.resus_vol_unit.setItemText(0, _translate("DNA_Tools", "L"))
		self.resus_vol_unit.setItemText(1, _translate("DNA_Tools", "ml"))
		self.resus_vol_unit.setItemText(2, _translate("DNA_Tools", "ul"))
		self.resus_vol_unit.setItemText(3, _translate("DNA_Tools", "nl"))
		
		self.equal3.setText(_translate("DNA_Tools", "="))
		self.Parenth.setText(_translate("DNA_Tools", ")"))
		self.Parenth2.setText(_translate("DNA_Tools", "("))
		
		self.resus_mass_unit.setItemText(0, _translate("DNA_Tools", "mol"))
		self.resus_mass_unit.setItemText(1, _translate("DNA_Tools", "mmol"))
		self.resus_mass_unit.setItemText(2, _translate("DNA_Tools", "umol"))
		self.resus_mass_unit.setItemText(3, _translate("DNA_Tools", "nmol"))
		
		self.mass2.setText(_translate("DNA_Tools", "Oligo amount"))
		self.divide2.setText(_translate("DNA_Tools", "÷"))
		self.Concentration4.setText(_translate("DNA_Tools", "Desired Concentration"))
		
		self.resus_M_unit.setItemText(0, _translate("DNA_Tools", "M"))
		self.resus_M_unit.setItemText(1, _translate("DNA_Tools", "mM"))
		self.resus_M_unit.setItemText(2, _translate("DNA_Tools", "uΜ"))
		self.resus_M_unit.setItemText(3, _translate("DNA_Tools", "nM"))
		self.Descript1.setText(_translate("DNA_Tools", "~Dilution of Known Concentration~"'\n(M1•V1=M2•V2)'))
		self.Descript2.setText(_translate("DNA_Tools", "~Concentration from MW~"))
		self.Descript3.setText(_translate("DNA_Tools", "~Volume required for resuspension~"))
		self.calc_go1.setText(_translate("DNA_Tools", "CALC"))
		self.calc_go2.setText(_translate("DNA_Tools", "CALC"))
		self.calc_go3.setText(_translate("DNA_Tools", "CALC"))
		self.border1.setText(_translate("DNA_Tools", "–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––"))
		self.border2.setText(_translate("DNA_Tools", "–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––"))
# self.calc_go3.clicked.connect(self.RESUS)
	
	def EX(self, DNA_GUI):
		x = self.Input_text.toPlainText()
		y = self.tool_select.currentText()
		if y == "Transcription":
			self.Output_text.appendPlainText(str(dna.FW_TRANSCRIPTION(x)))
			self.notify.show()
			self.input_ouput_tabs.setTabText(self.input_ouput_tabs.indexOf(self.Tab2),("DNA Tool (Output)"))
# 			self.Tab2.show()
		elif y == "Reverse Transcription":
			self.Output_text.appendPlainText(str(dna.RV_TRANSCRIPTION(x)))
			self.notify.show()
			self.input_ouput_tabs.setTabText(self.input_ouput_tabs.indexOf(self.Tab2),("DNA Tool (Output)"))
# 			self.Tab2.show()
		elif y == "Reverse Compliment":
			self.Output_text.appendPlainText(str(dna.REVERSE_COMP(x)))
			self.notify.show()
			self.input_ouput_tabs.setTabText(self.input_ouput_tabs.indexOf(self.Tab2),("DNA Tool (Output)"))
# 			self.Tab2.show()
		elif y == "Translation (1 letter)":
			self.Output_text.appendPlainText(str(dna.S_Translation(x)))
			self.notify.show()
			self.input_ouput_tabs.setTabText(self.input_ouput_tabs.indexOf(self.Tab2),("DNA Tool (Output)"))
# 			self.Tab2.show()
		elif y == "Translation (3 letter)":
			self.Output_text.appendPlainText(str(dna.T_Translation(x)))
			self.notify.show()
			self.input_ouput_tabs.setTabText(self.input_ouput_tabs.indexOf(self.Tab2),("DNA Tool (Output)"))
# 			self.Tab2.show()
		else:
			pass
	
	def RS(self, DNA_GUI):
		self.Output_text.clear()
		self.Input_text.clear()
		self.notify.hide()
		self.input_ouput_tabs.setTabText(self.input_ouput_tabs.indexOf(self.Tab2),("~Empty~"))
	
	def PrimerTool(self, DNA_GUI):
		x = self.nn_primer_input.toPlainText()
		C = self.concentration.value()
		NA = self.salt_conc.value()
		if len(x) >= 14:
			self.nn_primer_output.appendPlainText(str(PT.l_nearneigh(x, C, NA)))
		elif len(x) < 14:
			self.nn_primer_output.appendPlainText(str(PT.s_nearneigh(x, C, NA)))
	
	def PT_RS(self, DNA_GUI):
		self.nn_primer_input.clear()
		self.nn_primer_output.clear()
	
	def known_molarity_dilution(self, DNA_GUI):
		ua = self.M1_unit.currentIndex()
		ub = self.V1_Unit.currentIndex()
		uc = self.M2_unit.currentIndex()
		ud = self.V2_Unit.currentIndex()
		m1 = self.input_M1.text()
		m2 = self.input_M2.text()
		v2 = self.input_V2.text()
		def calculator(m1,m2,v2):
			Values = []
			Values = [float(m1), float(m2), float(v2)]
			argA = []
			argC= []
			argD = []
			u1 = 1
			u2 = 1
			u3 = 1
			u4 = 1
			unit_ = {
			0:1,
			1:0.001,
			2:10**-6,
			3:10**-9}
			for k, v in unit_.items():
				if ua == k:
					u1 = v
				if ub == k:
					u2 = v
				if uc == k:
					u3 = v
				if ud == k:
					u4 = v
			argA = (Values[0])*(u1)
			argC = (Values[1])*(u3)
			argD = (Values[2])*(u4)
			b = (argD*argC)/argA
			g = (b)/u2
			B = round(g,10)
			br = round(b,9)
			R = argD - br
		
			self.input_V1.setText(str(B))
			self.explanation.setText(f"Add {br} L of solution,\nplus {R} L of buffer")
			self.explanation.show()
		if m1 and m2 and v2 != '':
			calculator(m1,m2,v2)
		else:
			pass
		
	def Conc(self, DNA_GUI):
		ua = self.Mass_MW_unit.currentIndex()
		ub = self.Vol_fromMW_unit.currentIndex()
		uc = self.M_fromMW_unit.currentIndex()
		mass = self.input_mass_mw.text()
		vol = self.input_Vol_mw.text()
		mw = self.input_MW_mw.text()
		def calculator(mass,vol,mw):
			Values = [float(mass), float(vol), float(mw)]
			argA = []
			argC= []
			argD = []
			u1 = 1
			u2 = 1
			u3 = 1
			unit_ = {
			0:1,
			1:0.001,
			2:10**-6,
			3:10**-9}
			for k, v in unit_.items():
				if ua == k:
					u1 = v
				if ub == k:
					u2 = v
				if uc == k:
					u3 = v
			argA = (Values[0])*(u1)
			argC = (Values[1])*(u2)
			argD = (Values[2])
			Outty = DT.Concentration(argA,argC,argD)/u3
			self.input_C_mw.setText(str(Outty))
		if mass and vol and mw != '':
			calculator(mass,vol,mw)
		else:
			pass
		
	def RESUS(self, DNA_GUI):
		ua = self.resus_mass_unit.currentIndex()
		ub = self.resus_M_unit.currentIndex()
		uc = self.resus_vol_unit.currentIndex()
		mass = self.input_mass_resus.text()
		C = self.input_C_resus.text()
		def calculator(mass, C):
			Values = [float(mass), float(C)]
			argA = []
			argC= []
			u1 = 1
			u2 = 1
			u3 = 1
			unit_ = {
			0:1,
			1:0.001,
			2:10**-6,
			3:10**-9}
			for k, v in unit_.items():
				if ua == k:
					u1 = v
				if ub == k:
					u2 = v
				if uc == k:
					u3 = v
			argA = (Values[0])*(u1)
			argC = (Values[1])*(u2)
			Outty = DT.resuspension(argA,argC)/u3
			self.input_Vol_resus.setText(str(Outty))
		if mass and C != '':
			calculator(mass,C)
		else:
			pass
		

def executed():
	import sys
	app = QtWidgets.QApplication(sys.argv)
	win = DNA_GUI()
	win.show()
	sys.exit(app.exec_())
executed()
## Need to add place holder text for input seq primer tool, need to link signals to code, need to add other primer tool?!

'''
For Dilution Tools, all fields right of the equation are required to execute calculations. Else, pass.
Also, changing a variable will overwrite previous output..
'''





