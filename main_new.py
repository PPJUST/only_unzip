import os
import re

from PySide6.QtGui import QColor, QIcon, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

from module import function_archive
import module.function_file
import module.function_password
from constant import _ICON_MAIN, _ICON_DEFAULT, _ICON_DEFAULT_WITH_OUTPUT, \
    _PASSWORD_EXPORT, _ICON_PAGE_EXTRACT, _ICON_PAGE_HISTORY, _ICON_PAGE_PASSWORD, _ICON_PAGE_SETTING, _ICON_PAGE_HOME, \
    _ICON_STOP
from module import function_password
from module import function_static
from module.class_state import StateError, StateUpdateUI, StateSchedule
from module.function_config import Config
from ui.drop_label import DropLabel
from ui.history_listWidget import HistoryListWidget
from ui.ui_main import Ui_MainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 添加自定义控件
        self.dropped_label = DropLabel()
        self.ui.verticalLayout_dropped_label.addWidget(self.dropped_label)

        self.history_listWidget = HistoryListWidget()
        self.ui.verticalLayout_history.addWidget(self.history_listWidget)

        # 初始化
        function_static.init_settings()  # 检查初始文件
        self.load_config()
        self.check_output_folder()
        self.icon_gif_droplabel = None  # 动图对象，显示在拖入控件中

        # 设置ui
        self.ui.stackedWidget_main.setCurrentIndex(0)  # 将主页面设为第1页
        self.ui.stackedWidget_schedule.setCurrentIndex(0)  # 将信息页设为第1页
        self.change_page(self.ui.buttonGroup.id(self.ui.buttonGroup.buttons()[0]))  # 设置第一个按钮的颜色
        self.ui.button_page_home.setIcon(QIcon(_ICON_PAGE_HOME))
        self.ui.button_page_history.setIcon(QIcon(_ICON_PAGE_HISTORY))
        self.ui.button_page_password.setIcon(QIcon(_ICON_PAGE_PASSWORD))
        self.ui.button_page_setting.setIcon(QIcon(_ICON_PAGE_SETTING))
        self.ui.button_stop.setIcon(QIcon(_ICON_STOP))

        # 实例化子线程
        # self.qthread = ExtractQthread()
        # self.qthread.signal_update_ui.connect(self.update_ui)
        # self.qthread.signal_extracted_files.connect(lambda x: self.accept_files(x))

        # 设置槽函数
        # 标签页
        self.ui.buttonGroup.buttonClicked.connect(self.change_page)
        # 主页
        self.dropped_label.signal_dropped.connect(self.dropped_files)
        # self.ui.button_stop.clicked.connect(self.stop_qthread)
        # 密码
        self.ui.button_update_password.clicked.connect(self.update_password)
        self.ui.button_read_clipboard.clicked.connect(self.read_clipboard)
        self.ui.button_export_password.clicked.connect(lambda: function_password.export_password)
        self.ui.button_export_password.clicked.connect(lambda: self.ui.button_open_password.setEnabled(True))
        self.ui.button_open_password.clicked.connect(lambda: os.startfile(_PASSWORD_EXPORT))
        # 设置页
        self.ui.checkBox_mode_extract.stateChanged.connect(lambda: self.set_checkbox_enable(mode=True))
        self.ui.checkBox_mode_test.stateChanged.connect(lambda: self.set_checkbox_enable(mode=False))
        self.ui.button_ask_folder.clicked.connect(self.choose_output_folder)
        self.ui.lineEdit_output_folder.textChanged.connect(self.check_output_folder)
        self.ui.checkBox_mode_extract.stateChanged.connect(lambda: self.update_config('mode'))
        self.ui.checkBox_mode_test.stateChanged.connect(lambda: self.update_config('mode'))
        self.ui.checkBox_handling_nested_folder.stateChanged.connect(lambda: self.update_config('nested_folder'))
        self.ui.checkBox_handling_nested_archive.stateChanged.connect(lambda: self.update_config('nested_archive'))
        self.ui.checkBox_delete_original_file.stateChanged.connect(lambda: self.update_config('delete_original_file'))
        self.ui.checkBox_check_filetype.stateChanged.connect(lambda: self.update_config('check_filetype'))
        self.ui.lineEdit_exclude_rules.textChanged.connect(lambda: self.update_config('exclude_rules'))
        self.ui.lineEdit_output_folder.textChanged.connect(lambda: self.update_config('output_folder'))

    def load_config(self):
        """读取配置文件，更新选项"""
        # 读取
        config = Config()
        setting_mode = config.mode
        setting_handling_nested_folder = config.handling_nested_folder
        setting_handling_nested_archive = config.handling_nested_archive
        setting_delete_original_file = config.delete_original_file
        setting_check_filetype = config.check_filetype
        setting_exclude_rules = config.exclude_rules
        setting_output_folder = config.output_folder

        # 更新选项
        if setting_mode == 'extract':
            self.ui.checkBox_mode_extract.setChecked(True)
            self.set_checkbox_enable(mode=True)
        elif setting_mode == 'test':
            self.ui.checkBox_mode_test.setChecked(True)
            self.set_checkbox_enable(mode=False)
        self.ui.checkBox_handling_nested_folder.setChecked(setting_handling_nested_folder)
        self.ui.checkBox_handling_nested_archive.setChecked(setting_handling_nested_archive)
        self.ui.checkBox_delete_original_file.setChecked(setting_delete_original_file)
        self.ui.checkBox_check_filetype.setChecked(setting_check_filetype)
        self.ui.lineEdit_exclude_rules.setText(' '.join(setting_exclude_rules))
        self.ui.lineEdit_output_folder.setText(setting_output_folder)

    def set_checkbox_enable(self, mode=True):
        """切换模式后启用/禁用相关设置项"""
        self.ui.checkBox_delete_original_file.setEnabled(mode)
        self.ui.checkBox_check_filetype.setEnabled(mode)
        self.ui.checkBox_handling_nested_folder.setEnabled(mode)
        self.ui.checkBox_handling_nested_archive.setEnabled(mode)
        self.ui.lineEdit_output_folder.setEnabled(mode)
        self.ui.lineEdit_exclude_rules.setEnabled(mode)

    def set_widget_enable(self, mode=True):
        """启动7zip子线程前启用/禁用相关控件"""
        # 主页
        self.dropped_label.setEnabled(mode)
        # 密码页
        self.ui.button_update_password.setEnabled(mode)
        # 设置页
        self.ui.scrollAreaWidgetContents.setEnabled(mode)

    def check_output_folder(self):
        """检查是否指定了解压输出路径，并修改相关ui显示"""
        output_dir = self.ui.lineEdit_output_folder.text()
        if output_dir:
            if not os.path.exists(output_dir) or os.path.isfile(output_dir):
                self.ui.lineEdit_output_folder.setStyleSheet('border: 1px solid red;')
                self.dropped_label.reset_icon(_ICON_DEFAULT)
            else:
                self.ui.lineEdit_output_folder.setStyleSheet('')
                self.dropped_label.reset_icon(_ICON_DEFAULT_WITH_OUTPUT)
        else:
            self.ui.lineEdit_output_folder.setStyleSheet('')
            self.dropped_label.reset_icon(_ICON_DEFAULT)

    def change_page(self, button_id):
        """切换标签页，并高亮被点击的标签页按钮"""
        # 统一为int索引
        if type(button_id) is int:
            buttons_index = button_id
        else:
            buttons_index = self.ui.buttonGroup.id(button_id)

        # 切换标签页
        new_page_number = self.ui.buttonGroup.buttons().index(self.ui.buttonGroup.button(buttons_index))
        self.ui.stackedWidget_main.setCurrentIndex(new_page_number)

        # 高亮被点击的按钮
        original_style = self.ui.button_update_password.styleSheet()
        for button in self.ui.buttonGroup.buttons():
            button.setStyleSheet(original_style)

        clicked_style = r'background-color: rgb(255, 228, 181);'
        clicked_button = self.ui.buttonGroup.button(buttons_index)
        clicked_button.setStyleSheet(clicked_style)

    def dropped_files(self, paths: list):
        """拖入文件后进行测试或解压"""
        file_list = []
        for path in paths:
            path = os.path.normpath(path)
            if os.path.exists(path):
                if os.path.isfile(path):
                    file_list.append(path)
                else:
                    walk_files = module.function_file.get_files_list(path)
                    file_list += walk_files
        file_list = list(set(file_list))

        self.start_7zip_thread(file_list)

    def choose_output_folder(self):
        """弹出对话框，选择文件夹"""
        dirpath = QFileDialog.getExistingDirectory(self, "选择指定解压路径文件夹")
        if dirpath:
            self.ui.lineEdit_output_folder.setText(os.path.normpath(dirpath))

    def update_config(self, setting_item: str):
        """更新配置文件"""
        if setting_item == 'mode':
            mode = 'extract' if self.ui.checkBox_mode_extract.isChecked() else 'test'
            Config.update_config_mode(mode)
        elif setting_item == 'nested_folder':
            handling_nested_folder = self.ui.lineEdit_output_folder.isChecked()
            Config.update_config_handling_nested_folder(handling_nested_folder)
        elif setting_item == 'nested_archive':
            handling_nested_archive = self.ui.checkBox_handling_nested_archive.isChecked()
            Config.update_config_handling_nested_archive(handling_nested_archive)
        elif setting_item == 'delete_original_file':
            delete_original_file = self.ui.checkBox_delete_original_file.isChecked()
            Config.update_config_delete_original_file(delete_original_file)
        elif setting_item == 'check_filetype':
            check_filetype = self.ui.checkBox_check_filetype.isChecked()
            Config.update_config_check_filetype(check_filetype)
        elif setting_item == 'exclude_rules':
            exclude_text = self.ui.lineEdit_exclude_rules.text()
            support_delimiters = ",|，| |;|；"
            exclude_list = set([i for i in re.split(support_delimiters, exclude_text) if i])
            exclude_rule = ' '.join(exclude_list)
            Config.update_exclude_rules(exclude_rule)
        elif setting_item == 'output_folder':
            output_dir = str(self.ui.lineEdit_output_folder.text())
            Config.update_config_output_folder(output_dir)

    def update_password(self):
        """更新密码"""
        add_pw = [n for n in self.ui.text_password.toPlainText().split('\n') if n.strip()]
        add_pw_strip = [n.strip() for n in add_pw]
        pw_list = list(set(add_pw + add_pw_strip))  # 考虑到密码两端的空格，需要添加两种形式的密码
        module.function_password.update_password(pw_list)
        self.ui.text_password.clear()

    def read_clipboard(self):
        """读取剪切板"""
        clipboard = QApplication.clipboard()
        self.ui.text_password.setPlainText(clipboard.text())

    def start_7zip_thread(self, files: list):
        """调用子线程"""
        output_dir = self.ui.lineEdit_output_folder.text()
        # 检查是否存在遗留的临时文件夹
        if function_static.is_temp_folder_exists(files) and function_static.is_temp_folder_exists(output_dir):
            self.update_info_on_ui(StateError.TempFolder)
            return

        # 检查传入文件列表是否为空
        if not files:
            self.update_info_on_ui(StateError.NoArchive)
            return

        # 检查传入文件列表，提取出符合分卷压缩文件规则的文件，转换为{第一个分卷压缩包:(全部分卷)..}格式
        volume_archive_dict = function_archive.find_volume_archives(files)

        # 提取其余非分卷的文件
        other_file_dict = {}  # 保持字典格式的统一，{文件路径:(文件路径)..}
        volume_archives = set()
        for value in volume_archive_dict.values():
            volume_archives.update(value)
        for file in files:
            if file not in volume_archives:
                other_file_dict[file] = set()
                other_file_dict[file].add(file)

        # 合并两个dict
        file_dict = {}
        file_dict.update(volume_archive_dict)
        file_dict.update(other_file_dict)

        # 根据是否仅需要识别压缩文件，分两种情况获取最终需要执行操作的文件dict
        final_file_dict = {}
        if self.ui.checkBox_check_filetype.isChecked():
            for file in file_dict:
                if function_archive.is_archive(file):
                    final_file_dict[file] = file_dict[file]
        else:
            final_file_dict.update(file_dict)

        # 检查
        if not final_file_dict:
            self.update_info_on_ui(StateError.NoArchive)
            return

        # 将dict传递给子线程
        if final_file_dict:
            self.update_info_on_ui(StateSchedule.Running)
            # self.qthread.reset_setting()  # 更新设置
            # self.qthread.set_extract_files_dict(final_file_dict)  # 传递解压文件dict
            # self.qthread.start()

    def update_info_on_ui(self, state_class):
        """
        更新ui
        :param state_class: 自定义State类
        """
        # StateError类，错误信息
        if type(state_class) in StateError.__dict__.values():
            self.dropped_label.setPixmap(state_class.icon)
            self.ui.label_current_file.setText(state_class.current_file)
            self.ui.label_schedule_state.setText(state_class.schedule_state)
        # StateUpdateUI类，更新进度ui
        elif type(state_class) in StateUpdateUI.__dict__.values():
            text = state_class.text
            if type(state_class) is StateUpdateUI.CurrentFile:  # 当前文件
                self.ui.label_current_file.setText(text)
            elif type(state_class) is StateUpdateUI.ScheduleTotal:  # 总文件进度
                self.ui.label_schedule_total.setText(text)
            elif type(state_class) is StateUpdateUI.ScheduleTest:  # 测试密码进度
                self.ui.label_schedule_test.setText(text)
                if self.ui.stackedWidget_schedule.currentIndex() != 1:
                    self.ui.stackedWidget_schedule.setCurrentIndex(1)
            elif type(state_class) is StateUpdateUI.ScheduleExtract:  # 解压进度
                self.ui.progressBar_extract.setValue(text)
                if self.ui.stackedWidget_schedule.currentIndex() != 2:
                    self.ui.stackedWidget_schedule.setCurrentIndex(2)
        elif type(state_class) in StateSchedule.__dict__.values():
            pass


def main():
    app = QApplication()
    app.setStyle('Fusion')
    # 设置白色背景色
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(255, 255, 255))
    app.setPalette(palette)

    show_ui = Main()
    show_ui.setWindowIcon(QIcon(_ICON_MAIN))
    show_ui.setFixedSize(262, 232)
    show_ui.show()
    app.exec()


if __name__ == "__main__":
    main()
