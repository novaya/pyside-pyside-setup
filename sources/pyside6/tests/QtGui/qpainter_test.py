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

from PySide6.QtGui import QPainter, QLinearGradient
from PySide6.QtCore import QLine, QLineF, QPoint, QPointF, QRect, QRectF, Qt

class QPainterDrawText(unittest.TestCase):

    def setUp(self):
        self.painter = QPainter()
        self.text = 'teste!'

    def tearDown(self):
        del self.text
        del self.painter

    def testDrawText(self):
        # bug #254
        rect = self.painter.drawText(100, 100, 100, 100,
                                     Qt.AlignCenter | Qt.TextWordWrap,
                                     self.text)
        self.assertTrue(isinstance(rect, QRect))

    def testDrawTextWithRect(self):
        # bug #225
        rect = QRect(100, 100, 100, 100)
        newRect = self.painter.drawText(rect, Qt.AlignCenter | Qt.TextWordWrap,
                                        self.text)

        self.assertTrue(isinstance(newRect, QRect))

    def testDrawTextWithRectF(self):
        '''QPainter.drawText(QRectF, ... ,QRectF*) inject code'''
        rect = QRectF(100, 52.3, 100, 100)
        newRect = self.painter.drawText(rect, Qt.AlignCenter | Qt.TextWordWrap,
                                        self.text)

        self.assertTrue(isinstance(newRect, QRectF))

    def testDrawOverloads(self):
        '''Calls QPainter.drawLines overloads, if something is
           wrong Exception and chaos ensues. Bug #395'''
        self.painter.drawLines([QLine(QPoint(0,0), QPoint(1,1))])
        self.painter.drawLines([QPoint(0,0), QPoint(1,1)])
        self.painter.drawLines([QPointF(0,0), QPointF(1,1)])
        self.painter.drawLines([QLineF(QPointF(0,0), QPointF(1,1))])
        self.painter.drawPoints([QPoint(0,0), QPoint(1,1)])
        self.painter.drawPoints([QPointF(0,0), QPointF(1,1)])
        self.painter.drawConvexPolygon([QPointF(10.0, 80.0),
                                        QPointF(20.0, 10.0),
                                        QPointF(80.0, 30.0),
                                        QPointF(90.0, 70.0)])
        self.painter.drawConvexPolygon([QPoint(10.0, 80.0),
                                        QPoint(20.0, 10.0),
                                        QPoint(80.0, 30.0),
                                        QPoint(90.0, 70.0)])
        self.painter.drawPolygon([QPointF(10.0, 80.0),
                                  QPointF(20.0, 10.0),
                                  QPointF(80.0, 30.0),
                                  QPointF(90.0, 70.0)])
        self.painter.drawPolygon([QPoint(10.0, 80.0),
                                  QPoint(20.0, 10.0),
                                  QPoint(80.0, 30.0),
                                  QPoint(90.0, 70.0)])
        self.painter.drawPolyline([QPointF(10.0, 80.0),
                                   QPointF(20.0, 10.0),
                                   QPointF(80.0, 30.0),
                                   QPointF(90.0, 70.0)])
        self.painter.drawPolyline([QPoint(10.0, 80.0),
                                   QPoint(20.0, 10.0),
                                   QPoint(80.0, 30.0),
                                   QPoint(90.0, 70.0)])

class SetBrushWithOtherArgs(unittest.TestCase):
    '''Using qpainter.setBrush with args other than QBrush'''

    def testSetBrushGradient(self):
        painter = QPainter()
        gradient = QLinearGradient(0, 0, 0, 0)
        painter.setBrush(gradient)

if __name__ == '__main__':
    unittest.main()

