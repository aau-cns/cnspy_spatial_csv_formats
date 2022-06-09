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
import os
from enum import Enum
import cnspy_spatial_csv_formats.PoseStructs as ps
from cnspy_spatial_csv_formats.EstimationErrorType import EstimationErrorType
from cnspy_spatial_csv_formats.RotationErrorRepresentationType import RotationErrorRepresentationType


# TODOs
# - TODO: introduce a new PoseStruct element holding error types

class CSVSpatialFormatType(Enum):
    Timestamp = 'Timestamp'
    TUM = 'TUM'  # TUM-Format stems from: https://vision.in.tum.de/data/datasets/rgbd-dataset/tools#evaluation
    PositionStamped = 'PositionStamped'
    PosOrientCov = 'PosOrientCov'
    #PoseCov = 'PoseCov'
    PosOrientWithCov = 'PosOrientWithCov'
    #PoseWithCov = 'PoseWithCov'
    none = 'none'
    # HINT: if you add an entry here, please also add it to the .list() + .has_uncertainty method!

    def __str__(self):
        return self.value

    def has_uncertainty(self):
        if self == CSVSpatialFormatType.PosOrientCov or self == CSVSpatialFormatType.PosOrientWithCov:
            return True
        return False

    @staticmethod
    def list():
        return list([str(CSVSpatialFormatType.Timestamp), str(CSVSpatialFormatType.TUM), str(CSVSpatialFormatType.PositionStamped),
                     str(CSVSpatialFormatType.PosOrientCov),
                     str(CSVSpatialFormatType.PosOrientWithCov),
                     str(CSVSpatialFormatType.none)])

    @staticmethod
    def get_header(fmt, est_err_type=EstimationErrorType.none, rot_err_rep=RotationErrorRepresentationType.none):
        assert (isinstance(est_err_type, EstimationErrorType))
        assert (isinstance(rot_err_rep, RotationErrorRepresentationType))
        if str(fmt) == 'Timestamp' and est_err_type is EstimationErrorType.none and \
                rot_err_rep is RotationErrorRepresentationType.none:
            return ['#t']
        elif str(fmt) == 'TUM' and est_err_type is EstimationErrorType.none and \
                rot_err_rep is RotationErrorRepresentationType.none:
            return ['#t', 'tx', 'ty', 'tz', 'qx', 'qy', 'qz', 'qw']
        elif str(fmt) == 'PositionStamped' and est_err_type is EstimationErrorType.none and \
                rot_err_rep is RotationErrorRepresentationType.none:
            return ['#t', 'tx', 'ty', 'tz']
        elif str(fmt) == 'PosOrientCov':
            elems = ['#t', 'pxx', 'pxy', 'pxz', 'pyy', 'pyz', 'pzz', 'qrr', 'qrp', 'qry', 'qpp', 'qpy', 'qyy']
            if est_err_type is not EstimationErrorType.none or rot_err_rep is not RotationErrorRepresentationType.none:
                return elems + [str(est_err_type), str(rot_err_rep)]
            else:
                return elems
        elif str(fmt) == 'PosOrientWithCov':
            elems = ['#t', 'tx', 'ty', 'tz', 'qx', 'qy', 'qz', 'qw', 'pxx', 'pxy', 'pxz', 'pyy', 'pyz', 'pzz', 'qrr',
                    'qrp', 'qry', 'qpp', 'qpy', 'qyy']
            if est_err_type is not EstimationErrorType.none or rot_err_rep is not RotationErrorRepresentationType.none:
                return elems + [str(est_err_type), str(rot_err_rep)]
            else:
                return elems

        else:
            return ["# no header "]

    @staticmethod
    def get_format(fmt):
        if str(fmt) == 'Timestamp':
            return ['t']
        elif str(fmt) == 'TUM':
            return ['t', 'tx', 'ty', 'tz', 'qx', 'qy', 'qz', 'qw']
        elif str(fmt) == 'PositionStamped':
            return ['t', 'tx', 'ty', 'tz']
        elif str(fmt) == 'PosOrientCov':
            return ['t', 'pxx', 'pxy', 'pxz', 'pyy', 'pyz', 'pzz', 'qrr', 'qrp', 'qry', 'qpp', 'qpy', 'qyy']
        elif str(fmt) == 'PosOrientWithCov':
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
        elif str(fmt) == 'PositionStamped':
            return 4
        elif str(fmt) == 'PosOrientCov':
            return 13
        elif str(fmt) == 'PosOrientWithCov':
            return 20
        else:
            return None

    @staticmethod
    def parse(line, fmt):
        elems = line.split(",")
        if str(fmt) == 'Timestamp' or len(elems) == 1:
            return ps.sTimestamp(vec=[float(x) for x in elems[0:1]])
        elif str(fmt) == 'TUM' or len(elems) == 8:
            return ps.sTUMPoseStamped(vec=[float(x) for x in elems[0:8]])
        elif str(fmt) == 'PositionStamped' or len(elems) == 4:
            return ps.sPositionStamped(vec=[float(x) for x in elems[0:4]])
        elif str(fmt) == 'PosOrientCov' or len(elems) == 13:
            return ps.sPosOrientCovStamped(vec=[float(x) for x in elems[0:13]])
        elif str(fmt) == 'PosOrientWithCov' or len(elems) == 20:
            return ps.sTUMPosOrientWithCovStamped(vec=[float(x) for x in elems])
        else:
            return None

    @staticmethod
    def identify_format(fn):
        """

        Parameters
        ----------
        fn as str

        Returns
        -------
        CSVSpatialFormatType, EstimationErrorType, RotationErrorRepresentationType
        """
        if os.path.exists(fn):
            assert(isinstance(fn, str))
            with open(fn, "r") as file:
                header = str(file.readline()).rstrip("\n\r")
                for fmt in CSVSpatialFormatType.list():
                    format_type = CSVSpatialFormatType(fmt)

                    # iterate through the error types only if the format contains a covariance
                    if format_type.has_uncertainty():
                        for est_err_str in EstimationErrorType.list():
                            est_err_type = EstimationErrorType(est_err_str)
                            for rot_err_str in RotationErrorRepresentationType.list():
                                rot_err_type = RotationErrorRepresentationType(rot_err_str)
                                h_ = ",".join(CSVSpatialFormatType.get_header(fmt, est_err_type, rot_err_type))
                                if h_.replace(" ", "") == header.replace(" ", ""):
                                    return format_type, est_err_type, rot_err_type
                    else:
                        h_ = ",".join(CSVSpatialFormatType.get_header(fmt, EstimationErrorType.none,
                                                                      RotationErrorRepresentationType.none))
                        if h_.replace(" ", "") == header.replace(" ", ""):
                            return format_type, EstimationErrorType.none, RotationErrorRepresentationType.none

                print("CSVSpatialFormatType.identify_format(): Header unknown!\n\t[" + str(header) + "]")
        else:
            print("CSVSpatialFormatType.identify_format(): File not found!\n\t[" + str(fn) + "]")
        return CSVSpatialFormatType.none, EstimationErrorType.none, RotationErrorRepresentationType.none


