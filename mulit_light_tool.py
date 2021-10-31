# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lighting_tools_v01.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from Katana import Nodes3DAPI
from Katana import NodegraphAPI
from Katana import ScenegraphManager

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPainterPath
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QFileDialog

import Gaffer_Multi_Light_Control_module as lcm
import os

class Ui_Dobi_ligting_tools(object):

    def setupUi(self, Dobi_ligting_tools):
        Dobi_ligting_tools.setObjectName("Dobi_ligting_tools")
        Dobi_ligting_tools.resize(765, 630)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dobi_ligting_tools)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_gridLayout = QtWidgets.QGridLayout()
        self.main_gridLayout.setObjectName("main_gridLayout")
        self.TI_groupBox = QtWidgets.QGroupBox(Dobi_ligting_tools)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.TI_groupBox.setFont(font)
        self.TI_groupBox.setObjectName("TI_groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.TI_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TL_tabWidget = QtWidgets.QTabWidget(self.TI_groupBox)
        self.TL_tabWidget.setStyleSheet("")
        self.TL_tabWidget.setObjectName("TL_tabWidget")
        self.TL1_tab = QtWidgets.QWidget()
        self.TL1_tab.setObjectName("TL1_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.TL1_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.TL1_listWidget = QtWidgets.QListWidget(self.TL1_tab)
        self.TL1_listWidget.setObjectName("TL1_listWidget")
        self.verticalLayout_5.addWidget(self.TL1_listWidget)
        self.TL_tabWidget.addTab(self.TL1_tab, "")
        self.TL2_tab = QtWidgets.QWidget()
        self.TL2_tab.setObjectName("TL2_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.TL2_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.TL2_listWidget = QtWidgets.QListWidget(self.TL2_tab)
        self.TL2_listWidget.setObjectName("TL2_listWidget")
        self.verticalLayout_4.addWidget(self.TL2_listWidget)
        self.TL_tabWidget.addTab(self.TL2_tab, "")
        self.TL3_tab = QtWidgets.QWidget()
        self.TL3_tab.setObjectName("TL3_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.TL3_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TL3_listWidget = QtWidgets.QListWidget(self.TL3_tab)
        self.TL3_listWidget.setObjectName("TL3_listWidget")
        self.verticalLayout_2.addWidget(self.TL3_listWidget)
        self.TL_tabWidget.addTab(self.TL3_tab, "")
        self.gridLayout_3.addWidget(self.TL_tabWidget, 0, 0, 1, 1)
        self.view_groupBox = QtWidgets.QGroupBox(self.TI_groupBox)
        self.view_groupBox.setObjectName("view_groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.view_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.view_graphicsView = QtWidgets.QLabel(self.view_groupBox)
        self.view_graphicsView.setObjectName("view_graphicsView")
        self.verticalLayout_3.addWidget(self.view_graphicsView)
        self.gridLayout_3.addWidget(self.view_groupBox, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.main_gridLayout.addWidget(self.TI_groupBox, 1, 0, 1, 1)
        self.MLC_groupBox = QtWidgets.QGroupBox(Dobi_ligting_tools)
        self.MLC_groupBox.setFont(font)
        self.MLC_groupBox.setObjectName("MLC_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.MLC_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.param_comboBox = QtWidgets.QComboBox(self.MLC_groupBox)
        self.param_comboBox.setFont(font)
        self.param_comboBox.setObjectName("param_comboBox")
        self.param_comboBox.addItem("")
        self.param_comboBox.addItem("")
        self.param_comboBox.addItem("")
        self.param_comboBox.addItem("")
        self.param_comboBox.addItem("")
        self.param_comboBox.addItem("")
        self.param_comboBox.addItem("")
        self.param_comboBox.addItem("")
        self.param_comboBox.addItem("")
        self.param_comboBox.addItem("")
        self.param_comboBox.addItem("")
        self.gridLayout_2.addWidget(self.param_comboBox, 0, 1, 1, 1)
        self.param_label = QtWidgets.QLabel(self.MLC_groupBox)
        self.param_label.setFont(font)
        self.param_label.setObjectName("param_label")
        self.gridLayout_2.addWidget(self.param_label, 0, 0, 1, 1)
        self.values_label = QtWidgets.QLabel(self.MLC_groupBox)
        self.values_label.setFont(font)
        self.values_label.setObjectName("values_label")
        self.gridLayout_2.addWidget(self.values_label, 0, 2, 1, 1)
        self.values_lineEdit = QtWidgets.QLineEdit(self.MLC_groupBox)
        self.values_lineEdit.setFont(font)
        self.values_lineEdit.setObjectName("values_lineEdit")
        self.gridLayout_2.addWidget(self.values_lineEdit, 0, 3, 1, 1)
        self.run_pushButton = QtWidgets.QPushButton(self.MLC_groupBox)
        self.run_pushButton.setFont(font)
        self.run_pushButton.setObjectName("run_pushButton")
        self.gridLayout_2.addWidget(self.run_pushButton, 0, 4, 1, 1)
        self.example_lineEdit = QtWidgets.QLineEdit(self.MLC_groupBox)
        font = QtGui.QFont()
        font.setItalic(True)
        self.example_lineEdit.setFont(font)
        self.example_lineEdit.setStyleSheet("Background: transparent")
        self.example_lineEdit.setFrame(False)
        self.example_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.example_lineEdit.setReadOnly(True)
        self.example_lineEdit.setClearButtonEnabled(False)
        self.example_lineEdit.setObjectName("example_lineEdit")
        self.gridLayout_2.addWidget(self.example_lineEdit, 1, 3, 1, 1)
        self.PL_groupBox = QtWidgets.QGroupBox(self.MLC_groupBox)
        self.PL_groupBox.setMinimumSize(QtCore.QSize(551, 0))
        self.PL_groupBox.setObjectName("PL_groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.PL_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.PL_del_pushButton = QtWidgets.QPushButton(self.PL_groupBox)
        self.PL_del_pushButton.setObjectName("PL_del_pushButton")
        self.gridLayout_4.addWidget(self.PL_del_pushButton, 2, 1, 1, 1)
        self.PL_add_pushButton = QtWidgets.QPushButton(self.PL_groupBox)
        self.PL_add_pushButton.setEnabled(True)
        self.PL_add_pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.PL_add_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PL_add_pushButton.setAutoFillBackground(False)
        self.PL_add_pushButton.setObjectName("PL_add_pushButton")
        self.gridLayout_4.addWidget(self.PL_add_pushButton, 1, 1, 1, 1)
        self.PL_listView = QtWidgets.QListWidget(self.PL_groupBox)
        self.PL_listView.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.PL_listView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.PL_listView.setLayoutMode(QtWidgets.QListView.Batched)
        self.PL_listView.setObjectName("PL_listView")
        self.gridLayout_4.addWidget(self.PL_listView, 0, 0, 4, 1)
        self.PL_rep_pushButton = QtWidgets.QPushButton(self.PL_groupBox)
        self.PL_rep_pushButton.setObjectName("PL_rep_pushButton")
        self.gridLayout_4.addWidget(self.PL_rep_pushButton, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.PL_groupBox, 2, 0, 1, 5)
        self.param_label.raise_()
        self.values_label.raise_()
        self.param_comboBox.raise_()
        self.values_lineEdit.raise_()
        self.run_pushButton.raise_()
        self.PL_groupBox.raise_()
        self.example_lineEdit.raise_()
        self.main_gridLayout.addWidget(self.MLC_groupBox, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.main_gridLayout)
        self.retranslateUi(Dobi_ligting_tools)
        self.TL_tabWidget.setCurrentIndex(2)


        ###connect wigets
        self.run_pushButton.clicked.connect(self.multi_light_controls)
        self.PL_add_pushButton.clicked.connect(self.add_path_list)
        self.PL_del_pushButton.clicked.connect(self.del_path_list)
        self.PL_rep_pushButton.clicked.connect(self.rep_path_list)
        self.param_comboBox.currentIndexChanged.connect(self.values_example_list)
        self.TL1_listWidget.currentItemChanged.connect(self.proj_image_path)
        self.TL2_listWidget.currentItemChanged.connect(self.image_path)
        self.TL3_listWidget.currentItemChanged.connect(self.image_path)


        ###setTabOrder
        QtCore.QMetaObject.connectSlotsByName(Dobi_ligting_tools)
        Dobi_ligting_tools.setTabOrder(self.param_comboBox, self.values_lineEdit)
        Dobi_ligting_tools.setTabOrder(self.values_lineEdit, self.run_pushButton)
        Dobi_ligting_tools.setTabOrder(self.run_pushButton, self.PL_listView)
        Dobi_ligting_tools.setTabOrder(self.PL_listView, self.PL_rep_pushButton)
        Dobi_ligting_tools.setTabOrder(self.PL_rep_pushButton, self.PL_add_pushButton)
        Dobi_ligting_tools.setTabOrder(self.PL_add_pushButton, self.PL_del_pushButton)
        Dobi_ligting_tools.setTabOrder(self.PL_del_pushButton, self.TL_tabWidget)
        Dobi_ligting_tools.setTabOrder(self.TL_tabWidget, self.TL3_listWidget)
        Dobi_ligting_tools.setTabOrder(self.TL3_listWidget, self.view_graphicsView)
        Dobi_ligting_tools.setTabOrder(self.view_graphicsView, self.TL2_listWidget)
        Dobi_ligting_tools.setTabOrder(self.TL2_listWidget, self.TL1_listWidget)



        ### tex 리스트 불러오기 
        for item in self.tex_proj_additems():
            self.TL1_listWidget.addItem(str(item))


        for item in self.tex_hdir2_additems():
            self.TL2_listWidget.addItem(str(item))


        for item in self.light_filter_additems():
            self.TL3_listWidget.addItem(str(item))


    ###hdri#1 선택이미지 불러오기
    def proj_image_path(self, current, previous):
        tex_current_text = current.text()

        tex_path, tex_names = os.path.split(tex_current_text)
        tex_name, tex_ext = os.path.splitext(tex_names)

        jpg_image_path = "/storenext/user/lgt/joonsoo/TEX_IMAGES/light_filter/jpg/no_image.jpg"
        for i in self.proj_jpg_list():
            jpg_path, jpg_names = os.path.split(i)
            jpg_name, jpg_ext = os.path.splitext(jpg_names)

            if tex_name == jpg_name:
                jpg_image_path = os.path.join(jpg_path, jpg_names)
            else:
                top_split = tex_name.split('_TOP')
                bot_split = tex_name.split('_BOT')

                if top_split[0] == jpg_name or bot_split[0] == jpg_name:
                    jpg_image_path = os.path.join(jpg_path, jpg_names)
                else:
                    continue


        ### tex_view 불러오기    
        image_path = jpg_image_path
        image_profile = QtGui.QImage(image_path)
        image_profile = image_profile.scaled(200,200, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.view_graphicsView.setPixmap(QtGui.QPixmap.fromImage(image_profile))
        self.view_graphicsView.setScaledContents(True)

    
    ### hdri #1 jpg 리스트 가져오기
    def proj_jpg_list(self):
        get_proj_file = NodegraphAPI.NodegraphGlobals.GetProjectFile()
        split_proh_file = (get_proj_file.split(os.path.sep))

        proj_path = os.path.join("/show", split_proh_file[2], "assets/global/lgt/hdri")

        jpg_list = []
        for path, dir, files in os.walk(proj_path):
            file_jpg = [file for file in files if file.endswith(".jpg")]
            for file in file_jpg:
                file_path = os.path.join(path, file)
                jpg_list.append(file_path)
        return jpg_list






    ###hdri#2, light_filter 선택이미지 불러오기
    def image_path(self, current, previous):
        current_text = current.text()

        path, names = os.path.split(current_text)
        name, ext = os.path.splitext(names)

        jpg_path =  os.path.join(path + "/jpg/" + name + ".jpg")

        ### tex_view 불러오기    
        image_path = jpg_path
        image_profile = QtGui.QImage(image_path)
        image_profile = image_profile.scaled(200,200, aspectRatioMode=QtCore.Qt.IgnoreAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.view_graphicsView.setPixmap(QtGui.QPixmap.fromImage(image_profile))
        self.view_graphicsView.setScaledContents(True)




    def retranslateUi(self, Dobi_ligting_tools):
        _translate = QtCore.QCoreApplication.translate
        Dobi_ligting_tools.setWindowTitle(_translate("Dobi_ligting_tools", "Dobi_ligting_tools"))
        self.TI_groupBox.setTitle(_translate("Dobi_ligting_tools", "Tex_Images"))
        self.TL_tabWidget.setTabText(self.TL_tabWidget.indexOf(self.TL1_tab), _translate("Dobi_ligting_tools", "hdir#1"))
        self.TL_tabWidget.setTabText(self.TL_tabWidget.indexOf(self.TL2_tab), _translate("Dobi_ligting_tools", "hidr#2"))
        self.TL_tabWidget.setTabText(self.TL_tabWidget.indexOf(self.TL3_tab), _translate("Dobi_ligting_tools", "light_filter"))
        self.view_groupBox.setTitle(_translate("Dobi_ligting_tools", "View"))
        self.MLC_groupBox.setTitle(_translate("Dobi_ligting_tools", "Multi_Light_Control"))
        self.param_comboBox.setItemText(0, _translate("Dobi_ligting_tools", "Exposure"))
        self.param_comboBox.setItemText(1, _translate("Dobi_ligting_tools", "Intensity"))
        self.param_comboBox.setItemText(2, _translate("Dobi_ligting_tools", "LightGroup"))
        self.param_comboBox.setItemText(3, _translate("Dobi_ligting_tools", "SpecularAmount"))
        self.param_comboBox.setItemText(4, _translate("Dobi_ligting_tools", "DiffuseAmount"))
        self.param_comboBox.setItemText(5, _translate("Dobi_ligting_tools", "EnableShadows"))
        self.param_comboBox.setItemText(6, _translate("Dobi_ligting_tools", "Normalize"))
        self.param_comboBox.setItemText(7, _translate("Dobi_ligting_tools", "VisibleInRefraction"))
        self.param_comboBox.setItemText(8, _translate("Dobi_ligting_tools", "CameraVisibility"))
        self.param_comboBox.setItemText(9, _translate("Dobi_ligting_tools", "LightLinking"))
        self.param_comboBox.setItemText(10, _translate("Dobi_ligting_tools", "ShadowLinking"))
        self.param_label.setText(_translate("Dobi_ligting_tools", "Parameter"))
        self.values_label.setText(_translate("Dobi_ligting_tools", "Values"))
        self.run_pushButton.setText(_translate("Dobi_ligting_tools", "Run"))
        self.example_lineEdit.setText(_translate("Dobi_ligting_tools", "<int>  1, 100, 1000 ..."))
        self.PL_groupBox.setTitle(_translate("Dobi_ligting_tools", "Path_List"))
        self.PL_del_pushButton.setText(_translate("Dobi_ligting_tools", "Del"))
        self.PL_add_pushButton.setText(_translate("Dobi_ligting_tools", "Add"))
        self.PL_rep_pushButton.setText(_translate("Dobi_ligting_tools", "Replace"))



    ###example label change list
    def values_example_list(self):
        unlimit_int_list = ["Exposure", "Intensity"]
        limit_int_list = ["DiffuseAmount", "SpecularAmount"]
        linking_list = ["LightLinking", "ShadowLinking"]
        ml_list = ["LightGroup"]
        boll_list = ["EnableShadows", "Normalize", "VisibleInRefraction", "CameraVisibility"]

        if self.param_comboBox.currentText() in unlimit_int_list:
            self.example_lineEdit.setText("<int>  1, 100, 1000 ...")
        elif self.param_comboBox.currentText() in limit_int_list:
            self.example_lineEdit.setText("<int> 0 --- 1")
        elif self.param_comboBox.currentText() in linking_list:
            self.example_lineEdit.setText("<str> on, off")
        elif self.param_comboBox.currentText() in ml_list:
            self.example_lineEdit.setText("<str> ml1, ml2, ml3 ...")
        elif self.param_comboBox.currentText() in boll_list:
            self.example_lineEdit.setText("<bol> 1(yes), 0(no)")

    ###for katana 카타나용 노드이름 변경
    def convert_param_values(self):
        if self.param_comboBox.currentText() == "Exposure":
            convert_param_value = "exposure"
        elif self.param_comboBox.currentText() == "Intensity":
            convert_param_value = "intensity"
        elif self.param_comboBox.currentText() == "LightGroup":
            convert_param_value = "lightGroup"
        elif self.param_comboBox.currentText() == "SpecularAmount":
            convert_param_value = "specular"
        elif self.param_comboBox.currentText() == "DiffuseAmount":
            convert_param_value = "diffuse"
        elif self.param_comboBox.currentText() == "EnableShadows":
            convert_param_value = "enableShadows"
        elif self.param_comboBox.currentText() == "Normalize":
            convert_param_value = "areaNormalize"
        elif self.param_comboBox.currentText() == "VisibleInRefraction":
            convert_param_value = "visibleInRefractionPath"
        elif self.param_comboBox.currentText() == "CameraVisibility":
            convert_param_value = "camera"
        elif self.param_comboBox.currentText() == "LightLinking":
            convert_param_value = "LightLinkSetup_illumination"
        elif self.param_comboBox.currentText() == "ShadowLinking":
            convert_param_value = "LightLinkSetup_shadow"
        return convert_param_value


    ###scene graph node 
    def selected_scene_object(self):
        selected_scene_graph_names = ScenegraphManager.getActiveScenegraph()
        selected_scene_graph_locations = selected_scene_graph_names.getSelectedLocations()
        return selected_scene_graph_locations


    ###path list 버튼 컨트롤
    def add_path_list(self):
        listitems = self.selected_scene_object()

        for item in listitems:
            self.PL_listView.addItem(item)

    def rep_path_list(self):
        self.PL_listView.clear()
        listitems = self.selected_scene_object()

        for item in listitems:
            self.PL_listView.addItem(item)

    def del_path_list(self):
        listitem = self.PL_listView.selectedItems()
        if not listitem:
            self.PL_listView.clear()
        for item in listitem:
            self.PL_listView.takeItem(self.PL_listView.row(item))


    ###RUN 실행, 메시지박스 
    def multi_light_controls(self):
        param_value = self.values_lineEdit.text()
        param_name = self.convert_param_values()
        sclected_node_values = lcm.get_light_material(self.selected_scene_object())
        path_list = [self.PL_listView.item(i).text() for i in range(self.PL_listView.count())]

        if sclected_node_values == []:
            QtWidgets.QMessageBox.warning(Dobi_ligting_tools, "error!! Selected", "     Do select light     ")

        else:
            try: 
                filterList = ["LightLinking", "ShadowLinking"]
                if self.param_comboBox.currentText() == "CameraVisibility":
                    lcm.set_camera_viz(sclected_node_values, param_value)
                    QtWidgets.QMessageBox.information(Dobi_ligting_tools, "QMessageBox", "  Done..!! ")
                elif self.param_comboBox.currentText() in filterList:
                    if path_list == []:
                        QtWidgets.QMessageBox.warning(Dobi_ligting_tools, "error!! Path List", " Input Path List ")
                    else:
                        lcm.set_multi_linking(sclected_node_values, path_list, param_value, param_name)
                        QtWidgets.QMessageBox.information(Dobi_ligting_tools, "QMessageBox", "  Done..!! ")
                else:
                    lcm.set_material_values(sclected_node_values, param_name, param_value)
                    QtWidgets.QMessageBox.information(Dobi_ligting_tools, "QMessageBox", "  Done..!! ")

            except:
                QtWidgets.QMessageBox.warning(Dobi_ligting_tools, "error!! value", "input correct value ")


    ### light_filter 리스트 가져오기
    def light_filter_additems(self):
        path_dir = "/storenext/user/lgt/joonsoo/TEX_IMAGES/light_filter"
        file_list = os.listdir(path_dir)
        file_list_tex = [file for file in file_list if file.endswith(".tex")]

        tex_list = [] 
        for texs in file_list_tex:
            tex = os.path.join(path_dir, texs)
            tex_list.append(tex)
        return tex_list

    ### hdri#2 리스트 가져오기
    def tex_hdir2_additems(self):
        path_dir = "/storenext/user/lgt/joonsoo/TEX_IMAGES/sample_hdri"

        file_list = os.listdir(path_dir)
        file_list_tex = [file for file in file_list if file.endswith(".tex")]

        tex_list = [] 
        for texs in file_list_tex:
            tex = os.path.join(path_dir, texs)
            tex_list.append(tex)
        return tex_list

    ### hdri #1 리스트 가져오기
    def tex_proj_additems(self):
        get_proj_file = NodegraphAPI.NodegraphGlobals.GetProjectFile()
        split_proh_file = (get_proj_file.split(os.path.sep))


        if split_proh_file == ['']:
            return []

        else:
            proj_path = os.path.join("/show", split_proh_file[2], "assets/global/lgt/hdri")

            tex_list = []
            for path, dir, files in os.walk(proj_path):
                file_tex = [file for file in files if file.endswith(".tex")]
                for file in file_tex:
                    file_path = os.path.join(path, file)
                    tex_list.append(file_path)
            return tex_list




Dobi_ligting_tools = QtWidgets.QDialog()
ui = Ui_Dobi_ligting_tools()
Dobi_ligting_tools.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
Dobi_ligting_tools.setWindowFlags(Qt.WindowStaysOnTopHint)
ui.setupUi(Dobi_ligting_tools)
Dobi_ligting_tools.show()





