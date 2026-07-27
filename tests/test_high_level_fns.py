#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:16:32 2026

@author: badal.mondal
"""

import numpy as np
import pickle
from pathlib import Path
import banduppy
print(f'- BandUPpy version: {banduppy.__version__}')

#==============================================================================
# Path to test data
SimulationParentFolder = Path(__file__).parents[0] / "data"
print(f'- Parent test data folder: {SimulationParentFolder}')

#==============================================================================
class TestKpointsMerge: 
    def test_zero_wight_kp_file_merge_Vasp(self):
        vasp_files_path = SimulationParentFolder / 'vasp/SiGe_8atom/'
        print("- Generating merged zero-weight KPOINTS file...")
        prop_cal_hl = banduppy.HighLevelProperties(print_log=None)
        merge_kpts = prop_cal_hl.merge_zero_weight_2_sc_kpoint_file(vasp_files_path / 'VaspSimulations/IBZKPT', 
                                                                    vasp_files_path / 'BandUPpyKpointsGen/KPOINTS_SC', 
                                                                    save_dir=None, file_format= 'vasp')  
        ref_zero_weight_kpts = np.genfromtxt(vasp_files_path / 'BandUPpyKpointsGen/KPOINTS_zero_weight_test', skip_header=3, comments='#')
        np.testing.assert_allclose(ref_zero_weight_kpts, merge_kpts, rtol=1e-8,atol=1e-4)
        print("- Generating merged zero-weight KPOINTS file - Done")