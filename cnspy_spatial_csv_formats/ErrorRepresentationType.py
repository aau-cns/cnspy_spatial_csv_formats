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
from enum import Enum


# Please refer to "Error definitions and filter credibility evaluation", Jung and Weiss, 2022
class ErrorRepresentationType(Enum):
    R_small_theta = 'R_small_theta'  # R ~ eye(3) + skew(theta_R); if pose: R(3) x SO(3)
    q_small_theta = 'q_small_theta'  # q ~ [1; 0.5 theta_q]; if pose: R(3) x H
    so3_theta = 'so3_theta'          # R = exp(skew(theta)); if pose: R(3) x SO(3)
    se3_tau = 'se3_tau'              # P = exp(skew(tau)); tau = [v;theta]; if pose: SE(3)
    rpy_degree = 'rpy_degree'        # R = Rz(y)*Ry(p)*Rx(r); roll(r),pitch(p),yaw(y) in [deg]; if pose: R(3) x SO(3)
    rpy_rad = 'rpy_rad'              # R = Rz(y)*Ry(p)*Rx(r); roll(r),pitch(p),yaw(y) in [rad]; if pose: R(3) x SO(3)
    none = 'none'
    # HINT: if you add an entry here, please also add it to the .list() method!

    def __str__(self):
        return self.value

    @staticmethod
    def list():
        return list([str(ErrorRepresentationType.R_small_theta),
                     str(ErrorRepresentationType.q_small_theta),
                     str(ErrorRepresentationType.so3_theta),
                     str(ErrorRepresentationType.se3_tau),
                     str(ErrorRepresentationType.rpy_degree),
                     str(ErrorRepresentationType.rpy_rad),
                     str(ErrorRepresentationType.none)])
