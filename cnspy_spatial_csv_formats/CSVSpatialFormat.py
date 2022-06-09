#!/usr/bin/env python
# Software License Agreement (GNU GPLv3  License)
#
# Copyright (c) 2022, Roland Jung (roland.jung@aau.at) , AAU, KPK, NAV
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
import os
from enum import Enum
from cnspy_spatial_csv_formats.CSVFormatPose import CSVFormatPose
from cnspy_spatial_csv_formats.EstimationErrorType import EstimationErrorType
from cnspy_spatial_csv_formats.RotationErrorRepresentationType import RotationErrorRepresentationType


class CSVSpatialFormat:
    csv_format = CSVFormatPose.none
    estimation_error_type = EstimationErrorType.none
    rotation_error_representation = RotationErrorRepresentationType.none

    def __init__(self, fmt=None, est_err_type=None, rot_err_type= None):
        if fmt is not None:
            self.csv_format = fmt
        if est_err_type is not None:
            self.estimation_error_type = est_err_type
        if rot_err_type is not None:
            self.rotation_error_representation = rot_err_type

    def get_header(self):
        return CSVFormatPose.get_header(self.csv_format, self.estimation_error_type, self.rotation_error_representation)

    @staticmethod
    def identify_format(fn):
        fmt, est_err, rot_err = CSVFormatPose.identify_format(fn=fn)
        return CSVSpatialFormat(fmt, est_err_type=est_err, rot_err_type=rot_err)