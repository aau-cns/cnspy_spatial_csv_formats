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
########################################################################################################################
import unittest
from spatial_csv_format.CSVFormatPose import CSVFormatPose

class CSVFormat_Test(unittest.TestCase):
    def test_header(self):
        print('TUM CSV header:')

        for type in CSVFormatPose.list():
            print(str(CSVFormatPose.get_header(type)))

    def test_get_format(self):
        print('TUM CSV get_format:')

        for type in CSVFormatPose.list():
            print(str(CSVFormatPose.get_format(type)))

    def test_identify(self):
        fmt = CSVFormatPose.identify_format('./sample_data/ID1-pose-err.csv')
        print('identify_format:' + str(fmt))
        self.assertTrue(fmt == CSVFormatPose.TUM)
        fmt = CSVFormatPose.identify_format('./sample_data/ID1-pose-est-cov.csv')
        print('identify_format:' + str(fmt))
        self.assertTrue(fmt == CSVFormatPose.PoseWithCov)
        fmt = CSVFormatPose.identify_format('./sample_data/ID1-pose-gt.csv')
        print('identify_format:' + str(fmt))
        self.assertTrue(fmt == CSVFormatPose.TUM)
        fmt = CSVFormatPose.identify_format('./sample_data/example_eval.csv')
        print('identify_format:' + str(fmt))
        self.assertTrue(fmt == CSVFormatPose.none)
        fmt = CSVFormatPose.identify_format('./sample_data/212341234.csv')
        print('identify_format:' + str(fmt))
        self.assertTrue(fmt == CSVFormatPose.none)
        fmt = CSVFormatPose.identify_format('./sample_data/t_est.csv')
        print('identify_format:' + str(fmt))
        self.assertTrue(fmt == CSVFormatPose.Timestamp)


if __name__ == '__main__':
    unittest.main()
