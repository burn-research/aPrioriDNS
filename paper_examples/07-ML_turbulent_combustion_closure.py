#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 15:37:17 2025

@author: lorenzo piu
"""

import numpy as np
import aPrioriDNS as ap
import os
import shutil

tmp_data_folder = 'tmp'
os.mkdir(tmp_data_folder)
ap.download(dataset='h2_premixed', dest_folder=tmp_data_folder)
