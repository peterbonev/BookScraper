# -*- coding: utf-8 -*-
import Tkinter
import json
import ttk
from Tkconstants import END, TOP, LEFT, VERTICAL, RIGHT, BOTH, HORIZONTAL


class OutputFrameConstructor(object):

    def __init__(self, root):
        self.__output_frame = Tkinter.Toplevel(root)
        self.__output_frame.wm_minsize(400, 400)


    def constructor(self, text):
        """
            Constructor for output frame
        :param text:
        :return:
        """
        self.__scrolly = Tkinter.Scrollbar(self.__output_frame, orient=VERTICAL)
        self.__scrollx = Tkinter.Scrollbar(self.__output_frame, orient=HORIZONTAL)
        self.__output = Tkinter.Listbox(self.__output_frame,width=60, yscrollcommand=self.__scrolly.set, xscrollcommand=self.__scrollx.set)
        self.__scrolly.config(command=self.__output.yview)
        self.__scrollx.config(command=self.__output.xview)
        i = 0
        for x in text:
            output_list = ["{} :{}".format(k, v) for k, v in x.items()]
            for element in output_list:
                self.__output.insert(i, json.dumps(element, indent=4))
                i += 1
            self.__output.insert(i, '\n')
            i += 1
        self.__scrolly.grid(row=0,column=2, ipadx=1, ipady=200)
        self.__scrollx.grid(column=1, ipadx=350, ipady=1)
        self.__output.grid(row=0,column=1, ipadx=120, ipady=100)