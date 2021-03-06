# -*- coding: utf-8 -*-

#############################################################################
##
## Copyright (C) 2016 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of the test suite of Qt for Python.
##
## $QT_BEGIN_LICENSE:GPL-EXCEPT$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3 as published by the Free Software
## Foundation with exceptions as appearing in the file LICENSE.GPL3-EXCEPT
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from init_paths import init_test_paths
init_test_paths(False)

from PySide6.QtCore import *
from PySide6.QtWidgets import *

class MyObject(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self._method_called = False

    @Slot()
    def on_button_clicked(self):
        self._method_called = True


class AutoConnectionTest(unittest.TestCase):

    def testConnection(self):
        app = QApplication([])

        win = MyObject()
        btn = QPushButton("click", win)
        btn.setObjectName("button")
        QMetaObject.connectSlotsByName(win)
        btn.click()
        self.assertTrue(win._method_called)

if __name__ == '__main__':
    unittest.main()
