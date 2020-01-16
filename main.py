import sys
from gui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QBrush, QPalette
from PyQt5.QtCore import QSize, QTimer, QTime
import pandas as pd
from pandas_model import pandasModel
import itertools as IT
import logging
import multiprocessing as mp
from graph import *


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)
        oImage = QImage("journal-big-data.png")
        sImage = oImage.scaled(QSize(1058, 732))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()
        self.node_csv_files = None
        self.edge_csv_files = None
        self.result = None
        self.actionopen.triggered.connect(self.open_files)
        self.action_save.triggered.connect(self.save)
        self.show_cars.clicked.connect(self.show_car)
        self.show_bank_accounts.clicked.connect(self.show_account)
        self.show_home.clicked.connect(self.show_house)
        self.show_persons.clicked.connect(self.show_people)
        self.show_phones.clicked.connect(self.show_phone)
        self.show_contacts.clicked.connect(self.show_contact)
        self.show_transactios.clicked.connect(self.show_transaction)
        self.show_ownership.clicked.connect(self.show_ownerships)
        self.show_relationship.clicked.connect(self.show_relation)
        self.show_content.clicked.connect(self.show_contents)
        self.from_comboBox.activated[str].connect(self.update_sub_combobox)
        self.to_comboBox.activated[str].connect(self.update_sub_to_combobox)
        self.relation_combobox.activated[str].connect(self.update_sub_relation_combobox)
        self.analyze.clicked.connect(self.analyze_data)

    def displayTime(self):
        self.time_label.setText(QTime.currentTime().toString())

    def open_files(self):
        self.node_csv_files = None
        self.edge_csv_files = None
        filter = "CSV (*.csv)"
        file_name = QFileDialog()
        file_name.setFileMode(QFileDialog.ExistingFiles)
        self.node_csv_files = file_name.getOpenFileNames(self, "Please open node files", "C\\Desktop", filter)
        self.node_csv_files[0].sort()
        self.edge_csv_files = file_name.getOpenFileNames(self, "Please open edge files", "C\\Desktop", filter)
        self.edge_csv_files[0].sort()

    def show_car(self):
        if self.node_csv_files is not None:
            if len(self.node_csv_files[0]) == 5:
                df = pd.read_csv(self.node_csv_files[0][1])
                s = pandasModel(df)
                self.show_content_table.setModel(s)
                self.show_content_table.update()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("You didn't choose files correctly")
                msg.setWindowTitle("Error")
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You didn't choose files")
            msg.setWindowTitle("Error")
            msg.exec_()

    def show_account(self):
        if self.node_csv_files is not None:
            if len(self.node_csv_files[0]) == 5:
                df = pd.read_csv(self.node_csv_files[0][0])
                s = pandasModel(df)
                self.show_content_table.setModel(s)
                self.show_content_table.update()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("You didn't choose files correctly")
                msg.setWindowTitle("Error")
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You didn't choose files")
            msg.setWindowTitle("Error")
            msg.exec_()

    def show_house(self):
        if self.node_csv_files is not None:
            if len(self.node_csv_files[0]) == 5:
                df = pd.read_csv(self.node_csv_files[0][2])
                s = pandasModel(df)
                self.show_content_table.setModel(s)
                self.show_content_table.update()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("You didn't choose files correctly")
                msg.setWindowTitle("Error")
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You didn't choose files")
            msg.setWindowTitle("Error")
            msg.exec_()

    def show_people(self):
        if self.node_csv_files is not None:
            if len(self.node_csv_files[0]) == 5:
                df = pd.read_csv(self.node_csv_files[0][3])
                s = pandasModel(df)
                self.show_content_table.setModel(s)
                self.show_content_table.update()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("You didn't choose files correctly")
                msg.setWindowTitle("Error")
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You didn't choose files")
            msg.setWindowTitle("Error")
            msg.exec_()

    def show_phone(self):
        if self.node_csv_files is not None:
            if len(self.node_csv_files[0]) == 5:
                df = pd.read_csv(self.node_csv_files[0][4])
                s = pandasModel(df)
                self.show_content_table.setModel(s)
                self.show_content_table.update()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("You didn't choose files correctly")
                msg.setWindowTitle("Error")
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You didn't choose files")
            msg.setWindowTitle("Error")
            msg.exec_()

    def show_ownerships(self):
        if self.edge_csv_files is not None:
            if len(self.edge_csv_files[0]) == 4:
                df = pd.read_csv(self.edge_csv_files[0][1])
                s = pandasModel(df)
                self.show_content_table.setModel(s)
                self.show_content_table.update()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("You didn't choose files correctly")
                msg.setWindowTitle("Error")
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You didn't choose files")
            msg.setWindowTitle("Error")
            msg.exec_()

    def show_contact(self):
        if self.edge_csv_files is not None:
            if len(self.edge_csv_files[0]) == 4:
                df = pd.read_csv(self.edge_csv_files[0][0])
                s = pandasModel(df)
                self.show_content_table.setModel(s)
                self.show_content_table.update()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("You didn't choose files correctly")
                msg.setWindowTitle("Error")
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You didn't choose files")
            msg.setWindowTitle("Error")
            msg.exec_()

    def show_transaction(self):
        if self.edge_csv_files is not None:
            if len(self.edge_csv_files[0]) == 4:
                df = pd.read_csv(self.edge_csv_files[0][3])
                s = pandasModel(df)
                self.show_content_table.setModel(s)
                self.show_content_table.update()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("You didn't choose files correctly")
                msg.setWindowTitle("Error")
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You didn't choose files")
            msg.setWindowTitle("Error")
            msg.exec_()

    def show_relation(self):
        if self.edge_csv_files is not None:
            if len(self.edge_csv_files[0]) == 4:
                df = pd.read_csv(self.edge_csv_files[0][2])
                s = pandasModel(df)
                self.show_content_table.setModel(s)
                self.show_content_table.update()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("You didn't choose files correctly")
                msg.setWindowTitle("Error")
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You didn't choose files")
            msg.setWindowTitle("Error")
            msg.exec_()

    def show_contents(self):
        fr = str(self.from_lineEdit.text())
        to = str(self.to_lineEdit.text())
        relation = str(self.relation_lineEdit.text())

        if self.node_csv_files is None or self.edge_csv_files is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You didn't choose files")
            msg.setWindowTitle("Error")
            msg.exec_()

        elif len(self.edge_csv_files[0]) != 4 or len(self.node_csv_files[0]) != 5:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You didn't choose files correctly")
            msg.setWindowTitle("Error")
            msg.exec_()

        elif self.from_lineEdit.text() == "" and self.to_lineEdit.text() == "" and self.relation_lineEdit.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("All line edits are empty")
            msg.setWindowTitle("Error")
            msg.exec_()

        elif fr != "" and to == "" and relation == "":
            from_text = str(self.from_comboBox.currentText())
            from_sub_text = str(self.sub_comboBox.currentText())
            if from_sub_text == "ssn" or from_sub_text == "price" or from_sub_text == 'postal code' \
                    or from_sub_text == "size" or from_sub_text == "account number":
                flag = fr.isdigit()
                if flag:
                    df = pd.read_csv(from_text + ".csv")
                    w = df[df[from_sub_text] == int(fr)]
                    dataframeIsEmpty = w.empty
                    if dataframeIsEmpty:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("No information found")
                        msg.setWindowTitle("Error")
                        msg.exec_()
                    else:
                        s = pandasModel(w)
                        self.show_content_table.setModel(s)
                        self.show_content_table.update()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Your input must be digit")
                    msg.setWindowTitle("Error")
                    msg.exec_()
            else:
                df = pd.read_csv(from_text + ".csv")
                w = df[df[from_sub_text] == str(fr)]
                dataframeIsEmpty = w.empty
                if dataframeIsEmpty:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("No information found")
                    msg.setWindowTitle("Error")
                    msg.exec_()
                else:
                    s = pandasModel(w)
                    self.show_content_table.setModel(s)
                    self.show_content_table.update()

        elif (fr == "" and to == "") or (fr == "" and relation == "") or (to == "" and relation == ""):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Wrong input method")
            msg.setWindowTitle("Error")
            msg.exec_()

        else:
            from_text = str(self.from_comboBox.currentText())
            from_sub_text = str(self.sub_comboBox.currentText())
            to_text = str(self.to_comboBox.currentText())
            to_sub_text = str(self.sub_to_comboBox.currentText())
            relation_text = str(self.relation_combobox.currentText())
            relation_sub_text = str(self.sub_relation_combobox.currentText())
            if relation_text == "relationship":
                if from_text != "person" or from_sub_text != "ssn" or to_text != "person" or to_sub_text != "ssn" \
                        or fr.isdigit() is False or to.isdigit() is False or relation_sub_text == "":
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Wrong input method")
                    msg.setWindowTitle("Error")
                    msg.exec_()
                else:
                    df = pd.read_csv(relation_text + ".csv")
                    df = df[(df['from'] == int(fr)) & (df['to'] == int(to)) & (df[relation_sub_text] == relation)]
                    dataframeIsEmpty = df.empty
                    if dataframeIsEmpty:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("No information found")
                        msg.setWindowTitle("Error")
                        msg.exec_()
                    else:
                        s = pandasModel(df)
                        self.show_content_table.setModel(s)
                        self.show_content_table.update()

            elif relation_text == "transaction":
                if from_text != "account" or from_sub_text != "account_id" or to_text != "account" \
                        or to_sub_text != "account_id" or fr.isdigit() is False \
                        or to.isdigit() is False or relation_sub_text == "":
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Wrong input method")
                    msg.setWindowTitle("Error")
                    msg.exec_()
                else:
                    df = pd.read_csv(relation_text + ".csv")
                    if relation.isdigit():
                        df = df[
                            (df['from'] == int(fr)) & (df['to'] == int(to)) & (df[relation_sub_text] == int(relation))]
                    else:
                        df = df[
                            (df['from'] == int(fr)) & (df['to'] == int(to)) & (df[relation_sub_text] == str(relation))]

                    dataframeIsEmpty = df.empty
                    if dataframeIsEmpty:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("No information found")
                        msg.setWindowTitle("Error")
                        msg.exec_()
                    else:
                        s = pandasModel(df)
                        self.show_content_table.setModel(s)
                        self.show_content_table.update()

            elif relation_text == "ownership":
                if from_text != "person" or from_sub_text != "ssn" \
                        or fr.isdigit() is False or relation_sub_text == "":
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Wrong input method")
                    msg.setWindowTitle("Error")
                    msg.exec_()
                else:
                    df = pd.read_csv(relation_text + ".csv")
                    if to_sub_text == "plate":
                        if relation.isdigit():
                            df = df[
                                (df['from'] == int(fr)) & (df['to'] == to) & (df[relation_sub_text] == int(relation))]
                        else:
                            df = df[(df['from'] == int(fr)) & (df['to'] == to) & (df[relation_sub_text] == relation)]

                    elif to_sub_text == "postal_code":
                        if to.isdigit():
                            if relation.isdigit():
                                df = df[(df['from'] == int(fr)) & (df['to'] == to) & (
                                        df[relation_sub_text] == int(relation))]
                            else:
                                df = df[(df['from'] == int(fr)) & (df['to'] == to) & (
                                        df[relation_sub_text] == relation)]

                        else:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Wrong input method")
                            msg.setWindowTitle("Error")
                            msg.exec_()
                            return
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Wrong input method")
                        msg.setWindowTitle("Error")
                        msg.exec_()
                        return

                    dataframeIsEmpty = df.empty
                    if dataframeIsEmpty:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("No information found")
                        msg.setWindowTitle("Error")
                        msg.exec_()
                    else:
                        s = pandasModel(df)
                        self.show_content_table.setModel(s)
                        self.show_content_table.update()

            elif relation_text == "contact":
                if from_text != "phone" or to_text != "phone" or from_sub_text != "number" or to_sub_text != "number" \
                        or fr.isdigit() is False or to.isdigit() is False:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Wrong input method")
                    msg.setWindowTitle("Error")
                    msg.exec_()
                else:
                    df = pd.read_csv(relation_text + ".csv")
                    if relation.isdigit():
                        df = df[
                            (df['from'] == int(fr)) & (df['to'] == int(to)) & (df[relation_sub_text] == int(relation))]
                    else:
                        df = df[(df['from'] == int(fr)) & (df['to'] == int(to)) & (df[relation_sub_text] == relation)]

                    dataframeIsEmpty = df.empty
                    if dataframeIsEmpty:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("No information found")
                        msg.setWindowTitle("Error")
                        msg.exec_()
                    else:
                        s = pandasModel(df)
                        self.show_content_table.setModel(s)
                        self.show_content_table.update()

    def analyze_data(self):
        if self.node_csv_files is None or self.edge_csv_files is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You didn't choose files")
            msg.setWindowTitle("Error")
            msg.exec_()

        elif len(self.edge_csv_files[0]) != 4 or len(self.node_csv_files[0]) != 5:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("You didn't choose files correctly")
            msg.setWindowTitle("Error")
            msg.exec_()

        else:
            '''phase 2---------------------------------------------------------------------------------'''
            df = pd.read_csv(self.node_csv_files[0][3])
            df = df[(df['work'].str.contains("بندر")) | (df['work'].str.contains('گمرک'))]
            # dataFrame = pd.read_csv("relationship.csv")
            df = df.rename(columns={'ssn': 'from'})
            flag_data_frame = pd.merge(df, pd.read_csv(self.edge_csv_files[0][2]), on=['from'], how='inner')
            # flag_data_frame = flag_data_frame.drop_duplicates()
            dataf = pd.read_csv(self.edge_csv_files[0][1])
            flag_data_frame1 = flag_data_frame.drop(
                ['to', 'relation', 'date', 'first_name', 'last_name', 'birthday', 'work', 'city'], axis=1)
            flag_data_frame1 = pd.merge(flag_data_frame1, dataf, on=['from'], how='inner')
            flag_data_frame1 = flag_data_frame1.drop_duplicates()
            flag_data_frame1.to_csv('noni.csv', index=False)
            # print(flag_data_frame1)
            flag_data_frame2 = flag_data_frame.drop(
                ['from', 'relation', 'date', 'first_name', 'last_name', 'birthday', 'work', 'city'], axis=1)
            flag_data_frame2 = flag_data_frame2.rename(columns={'to': 'from'})
            flag_data_frame2 = pd.merge(flag_data_frame2, dataf, on=['from'], how='inner')
            flag_data_frame2 = flag_data_frame2.drop_duplicates()
            # print(flag_data_frame2)
            flag_data_frame2 = pd.concat([flag_data_frame2, flag_data_frame1], axis=0, sort=False)
            flag_data_frame2 = flag_data_frame2.drop_duplicates()
            print(flag_data_frame2)
            # flag_data_frame2.to_csv('noni.csv', index=False)

            '''--------------------------------------------------------------------------------------'''
            '''phase3--------------------------------------------------------------------------------'''
            logger = mp.log_to_stderr(logging.DEBUG)

            def worker(inqueues, outputs):
                result = []
                count = 0
                for pair in iter(inqueues.get, sentinel):
                    source, target = pair
                    try:
                        y = isPath(tr, source=source, target=target)
                        # r = nx.all_simple_paths(tr, source=source, target=target, cutoff=10)
                        if y:
                            print(source, target)
                            result.append((source, target))
                            count += 1
                            if count % 10 == 0:
                                logger.info('{c}'.format(c=count))
                    except:
                        continue
                outputs.put(result)

            def test_workers():
                result = []
                inqueue = mp.Queue()
                for source, target in IT.product(sources, targets):
                    inqueue.put((source, target))
                procs = [mp.Process(target=worker, args=(inqueue, output))
                         for _ in range(mp.cpu_count()-1)]
                for proc in procs:
                    proc.daemon = True
                    proc.start()
                for proc in procs:
                    inqueue.put(sentinel)
                for proc in procs:
                    result.extend(output.get())
                for proc in procs:
                    proc.join()
                return result

            sentinel = None

            transaction = pd.read_csv(self.edge_csv_files[0][3])
            tr = pandas_to_graph(transaction, 'from', 'to')
            df = pd.read_csv(self.node_csv_files[0][3])
            employees = df[(df['work'].str.contains("بندر")) | (df['work'].str.contains('گمرک'))]
            smugglers = df[df['work'].str.contains('قاچاقچی')]
            smugglers = pd.merge(smugglers, pd.read_csv(self.node_csv_files[0][0]), on=['ssn'], how='inner')
            employees = pd.merge(employees, pd.read_csv(self.node_csv_files[0][0]), on=['ssn'], how='inner')
            sources = list(smugglers['account_id'])
            targets = list(employees['account_id'])
            # print(len(sources), len(targets))
            output = mp.Queue()
            s = test_workers()
            rel = pd.DataFrame(s, columns=['from', 'to'])
            # rel.to_csv('reli.csv', index=False)
            print("finish")
            print(rel)
            '''---------------------------------------------------------------------------------------------'''
            '''phase4---------------------------------------------------------------------------------------'''
            rel = rel.rename(columns={'from': 'account_id'})
            f = pd.merge(rel, pd.read_csv(self.node_csv_files[0][0]), on=['account_id'], how='inner')
            f = f.drop(['to', 'account_id', 'bank_name', 'IBAN'], axis=1)
            rel = rel.rename(columns={'account_id': 'from'})
            rel = rel.rename(columns={'to': 'account_id'})
            t = pd.merge(rel, pd.read_csv(self.node_csv_files[0][0]), on=['account_id'], how='inner')
            t = t.drop(['from', 'account_id', 'bank_name', 'IBAN'], axis=1)
            f = pd.merge(f, pd.read_csv(self.node_csv_files[0][4]), on=['ssn'], how='left')
            t = pd.merge(t, pd.read_csv(self.node_csv_files[0][4]), on=['ssn'], how='left')
            f = f.drop(['ssn', 'operator'], axis=1)
            f = f.rename(columns={'number': 'from'})
            t = t.drop(['ssn', 'operator'], axis=1)
            t = t.rename(columns={'number': 'to'})
            concat = pd.concat([f, t], axis=1, sort=False)
            concat = concat.dropna()
            concat = concat.reset_index(drop=True)
            concat = concat.astype(int)
            concat = concat.drop_duplicates(subset='to')
            print(concat)
            w = pd.merge(concat, pd.read_csv(self.edge_csv_files[0][0]), on=['from', 'to'], how='inner')
            concat = concat.rename(columns={'from': 'to', 'to': 'from'})
            x = pd.merge(concat, pd.read_csv(self.edge_csv_files[0][0]), on=['from', 'to'], how='inner')
            x = x[['from', 'to', 'call_id', 'date', 'duration']]
            print(x)
            # print(concat)
            print(w)
            z = pd.concat([w, x], axis=0)
            self.result = z
            print(z)
            if z.empty:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("We didn't find Embezzler")
                msg.setWindowTitle("info")
                msg.exec_()
            else:
                r = pandasModel(z)
                self.show_content_table.setModel(r)
                self.show_content_table.update()

    def save(self):
        if self.result is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("We didn't have result for save")
            msg.setWindowTitle("Error")
            msg.exec_()

        else:
            file_name = QFileDialog()
            file_name.setFileMode(QFileDialog.ExistingFiles)
            fileName = file_name.getSaveFileName(self, "Please open node files")
            print(fileName)
            print(type(fileName))
            self.result.to_csv(fileName[0], index=False)

    def update_sub_combobox(self):
        self.sub_comboBox.clear()
        if self.from_comboBox.currentIndex() == 0:
            self.sub_comboBox.addItem("first_name")
            self.sub_comboBox.addItem("last_name")
            self.sub_comboBox.addItem("ssn")
            self.sub_comboBox.addItem("birthday")
            self.sub_comboBox.addItem("city")
            self.sub_comboBox.addItem("work")
            self.sub_comboBox.addItem("address")
        elif self.from_comboBox.currentIndex() == 1:
            self.sub_comboBox.addItem("plate")
            self.sub_comboBox.addItem("ssn")
            self.sub_comboBox.addItem("model")
            self.sub_comboBox.addItem("color")
        elif self.from_comboBox.currentIndex() == 2:
            self.sub_comboBox.addItem("ssn")
            self.sub_comboBox.addItem("price")
            self.sub_comboBox.addItem("postal_code")
            self.sub_comboBox.addItem("size")
            self.sub_comboBox.addItem("address")
        elif self.from_comboBox.currentIndex() == 3:
            self.sub_comboBox.addItem("ssn")
            self.sub_comboBox.addItem("number")
            self.sub_comboBox.addItem("operator")
        elif self.from_comboBox.currentIndex() == 4:
            self.sub_comboBox.addItem("ssn")
            self.sub_comboBox.addItem("bank_name")
            self.sub_comboBox.addItem("IBN")
            self.sub_comboBox.addItem("account_id")

    def update_sub_to_combobox(self):
        self.sub_to_comboBox.clear()
        if self.to_comboBox.currentIndex() == 0:
            self.sub_to_comboBox.addItem("first_name")
            self.sub_to_comboBox.addItem("last_name")
            self.sub_to_comboBox.addItem("ssn")
            self.sub_to_comboBox.addItem("birthday")
            self.sub_to_comboBox.addItem("city")
            self.sub_to_comboBox.addItem("work")
            self.sub_to_comboBox.addItem("address")
        elif self.to_comboBox.currentIndex() == 1:
            self.sub_to_comboBox.addItem("plate")
            self.sub_to_comboBox.addItem("ssn")
            self.sub_to_comboBox.addItem("model")
            self.sub_to_comboBox.addItem("color")
        elif self.to_comboBox.currentIndex() == 2:
            self.sub_to_comboBox.addItem("ssn")
            self.sub_to_comboBox.addItem("price")
            self.sub_to_comboBox.addItem("postal_code")
            self.sub_to_comboBox.addItem("size")
            self.sub_to_comboBox.addItem("address")
        elif self.to_comboBox.currentIndex() == 3:
            self.sub_to_comboBox.addItem("ssn")
            self.sub_to_comboBox.addItem("number")
            self.sub_to_comboBox.addItem("operator")
        elif self.to_comboBox.currentIndex() == 4:
            self.sub_to_comboBox.addItem("ssn")
            self.sub_to_comboBox.addItem("bank_name")
            self.sub_to_comboBox.addItem("IBN")
            self.sub_to_comboBox.addItem("account_id")

    def update_sub_relation_combobox(self):
        self.sub_relation_combobox.clear()
        if self.relation_combobox.currentIndex() == 0:
            self.sub_relation_combobox.addItem("relation")
            self.sub_relation_combobox.addItem("date")
        elif self.relation_combobox.currentIndex() == 1:
            self.sub_relation_combobox.addItem("date")
            self.sub_relation_combobox.addItem("transaction_id")
            self.sub_relation_combobox.addItem("amount")
        elif self.relation_combobox.currentIndex() == 2:
            self.sub_relation_combobox.addItem("ownership_id")
            self.sub_relation_combobox.addItem("date")
            self.sub_relation_combobox.addItem("amount")
        elif self.relation_combobox.currentIndex() == 3:
            self.sub_relation_combobox.addItem("call_id")
            self.sub_relation_combobox.addItem("date")
            self.sub_relation_combobox.addItem("duration")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
