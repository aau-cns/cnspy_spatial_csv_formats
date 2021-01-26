#!/usr/bin/env python
# Software License Agreement (GNU GPLv3  License)
#
# Copyright (c) 2020, Roland Jung (roland.jung@aau.at) , AAU, KPK, NAV
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Requirements:
# enum
########################################################################################################################
import os
from enum import Enum


class sTimestamp:
    def __init__(self, vec=None):
        assert (len(vec) == 1)
        self.t = vec[0]


class sTUM:
    def __init__(self, vec=None):
        assert (len(vec) == 8)
        self.t = vec[0]
        self.tx = vec[1]
        self.ty = vec[2]
        self.tz = vec[3]
        self.qx = vec[4]
        self.qy = vec[5]
        self.qz = vec[6]
        self.qw = vec[7]


class sTUM_short:
    def __init__(self, vec=None):
        assert (len(vec) == 4)
        self.t = vec[0]
        self.tx = vec[1]
        self.ty = vec[2]
        self.tz = vec[3]


class sPoseCov:
    def __init__(self, vec=None):
        assert (len(vec) == 13)
        self.t = vec[0]
        self.pxx = vec[1]
        self.pxy = vec[2]
        self.pxz = vec[3]
        self.pyy = vec[4]
        self.pyz = vec[5]
        self.pzz = vec[6]
        self.qrr = vec[7]
        self.qrp = vec[8]
        self.qry = vec[9]
        self.qpp = vec[10]
        self.qpy = vec[11]
        self.qyy = vec[12]


class sPoseWithCov:
    def __init__(self, vec=None):
        assert (len(vec) == 20)
        self.t = vec[0]
        self.tx = vec[1]
        self.ty = vec[2]
        self.tz = vec[3]
        self.qx = vec[4]
        self.qy = vec[5]
        self.qz = vec[6]
        self.qw = vec[7]
        self.pxx = vec[8]
        self.pxy = vec[9]
        self.pxz = vec[10]
        self.pyy = vec[11]
        self.pyz = vec[12]
        self.pzz = vec[13]
        self.qrr = vec[14]
        self.qrp = vec[15]
        self.qry = vec[16]
        self.qpp = vec[17]
        self.qpy = vec[18]
        self.qyy = vec[19]


class CSVFormat(Enum):
    Timestamp = 'Timestamp'
    # TUM-Format stems from: https://vision.in.tum.de/data/datasets/rgbd-dataset/tools#evaluation
    TUM = 'TUM'
    TUM_short = 'TUM_short'
    PoseCov = 'PoseCov'
    PoseWithCov = 'PoseWithCov'
    none = 'none'

    # HINT: if you add an entry here, please also add it to the .list() method!

    def __str__(self):
        return self.value

    @staticmethod
    def list():
        return list([str(CSVFormat.Timestamp), str(CSVFormat.TUM), str(CSVFormat.TUM_short), str(CSVFormat.PoseCov),
                     str(CSVFormat.PoseWithCov),
                     str(CSVFormat.none)])

    @staticmethod
    def get_header(fmt):
        if str(fmt) == 'Timestamp':
            return ['#t']
        elif str(fmt) == 'TUM':
            return ['#t', 'tx', 'ty', 'tz', 'qx', 'qy', 'qz', 'qw']
        elif str(fmt) == 'TUM_short':
            return ['#t', 'tx', 'ty', 'tz']
        elif str(fmt) == 'PoseCov':
            return ['#t', 'pxx', 'pxy', 'pxz', 'pyy', 'pyz', 'pzz', 'qrr', 'qrp', 'qry', 'qpp', 'qpy', 'qyy']
        elif str(fmt) == 'PoseWithCov':
            return ['#t', 'tx', 'ty', 'tz', 'qx', 'qy', 'qz', 'qw', 'pxx', 'pxy', 'pxz', 'pyy', 'pyz', 'pzz', 'qrr',
                    'qrp', 'qry', 'qpp', 'qpy', 'qyy']

        else:
            return ["# no header "]

    @staticmethod
    def get_format(fmt):
        if str(fmt) == 'Timestamp':
            return ['t']
        elif str(fmt) == 'TUM':
            return ['t', 'tx', 'ty', 'tz', 'qx', 'qy', 'qz', 'qw']
        elif str(fmt) == 'TUM_short':
            return ['t', 'tx', 'ty', 'tz']
        elif str(fmt) == 'PoseCov':
            return ['t', 'pxx', 'pxy', 'pxz', 'pyy', 'pyz', 'pzz', 'qrr', 'qrp', 'qry', 'qpp', 'qpy', 'qyy']
        elif str(fmt) == 'PoseWithCov':
            return ['t', 'tx', 'ty', 'tz', 'qx', 'qy', 'qz', 'qw', 'pxx', 'pxy', 'pxz', 'pyy', 'pyz', 'pzz', 'qrr',
                    'qrp', 'qry', 'qpp', 'qpy', 'qyy']
        else:
            return ['no format']

    @staticmethod
    def get_num_elem(fmt):

        if str(fmt) == 'Timestamp':
            return 1
        elif str(fmt) == 'TUM':
            return 8
        elif str(fmt) == 'TUM_short':
            return 4
        elif str(fmt) == 'PoseCov':
            return 13
        elif str(fmt) == 'PoseWithCov':
            return 20
        else:
            return None

    @staticmethod
    def parse(line, fmt):
        elems = line.split(",")
        if str(fmt) == 'Timestamp' or len(elems) == 1:
            return sTimestamp(vec=[float(x) for x in elems[0:1]])
        elif str(fmt) == 'TUM' or len(elems) == 8:
            return sTUM(vec=[float(x) for x in elems[0:8]])
        elif str(fmt) == 'TUM_short' or len(elems) == 4:
            return sTUM_short(vec=[float(x) for x in elems[0:4]])
        elif str(fmt) == 'PoseCov' or len(elems) == 13:
            return sPoseCov(vec=[float(x) for x in elems[0:13]])
        elif str(fmt) == 'PoseWithCov' or len(elems) == 20:
            return sPoseWithCov(vec=[float(x) for x in elems])
        else:
            return None

    @staticmethod
    def identify_format(fn):
        if os.path.exists(fn):
            with open(fn, "r") as file:
                header = str(file.readline()).rstrip("\n\r")
                for fmt in CSVFormat.list():
                    h_ = ",".join(CSVFormat.get_header(fmt))
                    if h_.replace(" ", "") == header.replace(" ", ""):
                        return CSVFormat(fmt)
                print("CSVFormat.identify_format(): Header unknown!\n\t[" + str(header) + "]")
        else:
            print("CSVFormat.identify_format(): File not found!\n\t[" + str(fn) + "]")
        return CSVFormat.none


########################################################################################################################
#################################################### T E S T ###########################################################
########################################################################################################################
import unittest


class CSVFormat_Test(unittest.TestCase):
    def test_header(self):
        print('TUM CSV header:')

        for type in CSVFormat.list():
            print(str(CSVFormat.get_header(type)))

    def test_get_format(self):
        print('TUM CSV get_format:')

        for type in CSVFormat.list():
            print(str(CSVFormat.get_format(type)))

    def test_identify(self):
        fmt = CSVFormat.identify_format('../sample_data/ID1-pose-err.csv')
        print('identify_format:' + str(fmt))
        self.assertTrue(fmt == CSVFormat.TUM)
        fmt = CSVFormat.identify_format('../sample_data/ID1-pose-est-cov.csv')
        print('identify_format:' + str(fmt))
        self.assertTrue(fmt == CSVFormat.PoseWithCov)
        fmt = CSVFormat.identify_format('../sample_data/ID1-pose-gt.csv')
        print('identify_format:' + str(fmt))
        self.assertTrue(fmt == CSVFormat.TUM)
        fmt = CSVFormat.identify_format('../sample_data/example_eval.csv')
        print('identify_format:' + str(fmt))
        self.assertTrue(fmt == CSVFormat.none)
        fmt = CSVFormat.identify_format('../sample_data/212341234.csv')
        print('identify_format:' + str(fmt))
        self.assertTrue(fmt == CSVFormat.none)
        fmt = CSVFormat.identify_format('../sample_data/t_est.csv')
        print('identify_format:' + str(fmt))
        self.assertTrue(fmt == CSVFormat.Timestamp)


if __name__ == '__main__':
    unittest.main()
