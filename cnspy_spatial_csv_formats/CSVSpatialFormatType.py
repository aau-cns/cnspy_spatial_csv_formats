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
from cnspy_spatial_csv_formats.ErrorRepresentationType import ErrorRepresentationType


class CSVSpatialFormatType(Enum):
    Timestamp = 'Timestamp'
    TUM = 'TUM'  # TUM-Format stems from: https://vision.in.tum.de/data/datasets/rgbd-dataset/tools#evaluation
    PositionStamped = 'PositionStamped'
    PosOrientCov = 'PosOrientCov'
    PosOrientWithCov = 'PosOrientWithCov'
    PoseCov = 'PoseCov'
    PoseWithCov = 'PoseWithCov'
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
        return list([str(CSVSpatialFormatType.Timestamp),
                     str(CSVSpatialFormatType.TUM),
                     str(CSVSpatialFormatType.PositionStamped),
                     str(CSVSpatialFormatType.PosOrientCov),
                     str(CSVSpatialFormatType.PosOrientWithCov),
                     str(CSVSpatialFormatType.PoseCov),
                     str(CSVSpatialFormatType.PoseWithCov),
                     str(CSVSpatialFormatType.none)])

    @staticmethod
    def get_header(fmt, est_err_type=EstimationErrorType.none, err_rep=ErrorRepresentationType.none):
        assert (isinstance(est_err_type, EstimationErrorType))
        assert (isinstance(err_rep, ErrorRepresentationType))
        if str(fmt) == 'Timestamp' and est_err_type is EstimationErrorType.none and \
                err_rep is ErrorRepresentationType.none:
            return ['#t']
        elif str(fmt) == 'TUM' and est_err_type is EstimationErrorType.none and \
                err_rep is ErrorRepresentationType.none:
            return ['#t', 'tx', 'ty', 'tz', 'qx', 'qy', 'qz', 'qw']
        elif str(fmt) == 'PositionStamped' and est_err_type is EstimationErrorType.none and \
                err_rep is ErrorRepresentationType.none:
            return ['#t', 'tx', 'ty', 'tz']
        elif str(fmt) == 'PosOrientCov':
            elems = ['#t', 'pxx', 'pxy', 'pxz', 'pyy', 'pyz', 'pzz', 'qrr', 'qrp', 'qry', 'qpp', 'qpy', 'qyy']
            if est_err_type is not EstimationErrorType.none or err_rep is not ErrorRepresentationType.none:
                return elems + [str(est_err_type), str(err_rep)]
            else:
                return elems
        elif str(fmt) == 'PosOrientWithCov':
            elems = ['#t', 'tx', 'ty', 'tz', 'qx', 'qy', 'qz', 'qw', 'pxx', 'pxy', 'pxz', 'pyy', 'pyz', 'pzz', 'qrr',
                    'qrp', 'qry', 'qpp', 'qpy', 'qyy']
            if est_err_type is not EstimationErrorType.none or err_rep is not ErrorRepresentationType.none:
                return elems + [str(est_err_type), str(err_rep)]
            else:
                return elems
        elif str(fmt) == 'PoseCov':
            # R = Rz(y/c)Ry(b/p)Rx(r/a)
            # a  for roll (r)
            # b  for pitch (p)
            # c  for yaw (y - is already used for y-position of the frame)
            elems = ['#t', 'Txx', 'Txy', 'Txz', 'Txa', 'Txb', 'Txc',
                     'Tyy', 'Tyz', 'Tya', 'Tyb', 'Tyc',
                     'Tzz', 'Tza', 'Tzb', 'Tzc',
                     'Taa', 'Tab', 'Tac',
                     'Tbb', 'Tbc',
                     'Tcc']
            if est_err_type is not EstimationErrorType.none or err_rep is not ErrorRepresentationType.none:
                return elems + [str(est_err_type), str(err_rep)]
            else:
                return elems
        elif str(fmt) == 'PoseWithCov':
            # R = Rz(y/c)Ry(b/p)Rx(r/a)
            # a  for roll (r)
            # b  for pitch (p)
            # c  for yaw (y - is already used for y-position of the frame)
            elems = ['#t', 'tx', 'ty', 'tz', 'qx', 'qy', 'qz', 'qw',
                     'Txx', 'Txy', 'Txz', 'Txa', 'Txb', 'Txc',
                     'Tyy', 'Tyz', 'Tya', 'Tyb', 'Tyc',
                     'Tzz', 'Tza', 'Tzb', 'Tzc',
                     'Taa', 'Tab', 'Tac',
                     'Tbb', 'Tbc',
                     'Tcc']
            if est_err_type is not EstimationErrorType.none or err_rep is not ErrorRepresentationType.none:
                return elems + [str(est_err_type), str(err_rep)]
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
        elif str(fmt) == 'PoseCov':
            return ['t', 'Txx', 'Txy', 'Txz', 'Txa', 'Txb', 'Txc',
                    'Tyy', 'Tyz', 'Tya', 'Tyb', 'Tyc',
                    'Tzz', 'Tza', 'Tzb', 'Tzc',
                    'Taa', 'Tab', 'Tac',
                    'Tbb', 'Tbc',
                    'Tcc']
        elif str(fmt) == 'PoseWithCov':
            return ['t', 'tx', 'ty', 'tz', 'qx', 'qy', 'qz', 'qw',
                    'Txx', 'Txy', 'Txz', 'Txa', 'Txb', 'Txc',
                    'Tyy', 'Tyz', 'Tya', 'Tyb', 'Tyc',
                    'Tzz', 'Tza', 'Tzb', 'Tzc',
                    'Taa', 'Tab', 'Tac',
                    'Tbb', 'Tbc',
                    'Tcc']

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
        elif str(fmt) == 'PoseCov':
            return 22
        elif str(fmt) == 'PoseWithCov':
            return 29
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
        elif str(fmt) == 'PoseCov' or len(elems) == 22:
            return ps.sPoseCovStamped(vec=[float(x) for x in elems[0:13]])
        elif str(fmt) == 'PoseWithCov' or len(elems) == 29:
            return ps.sTUMPoseWithCovStamped(vec=[float(x) for x in elems])
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
        CSVSpatialFormatType, EstimationErrorType, ErrorRepresentationType
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
                            for err_str in ErrorRepresentationType.list():
                                err_type = ErrorRepresentationType(err_str)
                                h_ = ",".join(CSVSpatialFormatType.get_header(fmt, est_err_type, err_type))

                                # ignore white-spaces and header indicators '#'
                                if h_.replace(" ", "").replace("#", "") == header.replace(" ", "").replace("#", ""):
                                    return format_type, est_err_type, err_type
                    else:
                        h_ = ",".join(CSVSpatialFormatType.get_header(fmt, EstimationErrorType.none,
                                                                      ErrorRepresentationType.none))
                        # ignore white-spaces and header indicators '#'
                        if h_.replace(" ", "").replace("#", "") == header.replace(" ", "").replace("#", ""):
                            return format_type, EstimationErrorType.none, ErrorRepresentationType.none

                print("CSVSpatialFormatType.identify_format(): Header unknown!\n\t[" + str(header) + "]")
        else:
            print("CSVSpatialFormatType.identify_format(): File not found!\n\t[" + str(fn) + "]")
        return CSVSpatialFormatType.none, EstimationErrorType.none, ErrorRepresentationType.none


