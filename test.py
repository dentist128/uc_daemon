# -*- coding: utf-8 -*-
# uc_daemon - A set of classes and functions for demonizing a process and related tools..
# It is part of the Unicon project.
# https://unicon.10k.me
#
# Copyright © 2020 Eduard S. Markelov.
# All rights reserved.
# Author: Eduard S. Markelov <markeloveduard@gmail.com>
#
# This program is Free Software; you can redistribute it and/or modify it under
# the terms of version three of the GNU Affero General Public License as
# published by the Free Software Foundation and included in the file LICENSE.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
"""
A test for daemon package.
"""
import os
import sys
import uc_daemon as daemon


pid = daemon.daemonize()

if (pid == 0): # i'm daemon
    print("I'm daemon! My pid is %d" % os.getpid())
else:
    print("Daemon started with pid %d and my pid is %d" % (pid, os.getpid()))

