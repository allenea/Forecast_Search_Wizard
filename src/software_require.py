# Copyright (C) 2018-2019 Eric Allen - All Rights Reserved
# Modified from my PyDatPicture code governed by the same 
# GNU Public License v3.0
#
# You may use, distribute and modify this code under the
# terms of the GNU General Public License v3.0 license.
#
# You should have received a copy of the GNU General Public
# License v3.0 packaged with the Forecast Search Wizard.
# If not vist https://www.gnu.org/licenses/gpl-3.0.en.html
#
# Please properly cite code, derivative code, and outputs
# of the Forecast Search Wizard in all scholarly work and
# publications.
#
# ONCE SETUP.PY WORKS GET RID OF THIS....

def setup_FSW():
    """ See if require software is available. If not ATTEMPT to download/install it."""
    try:
        import os
        import sys
        import re
        import glob
        import time
        import getpass
        import shutil
        #import pathlib ## Not pre 3.4
        import signal
        import subprocess

    except:
        print("One or more (expected) pre-installed python modules are not installed: ",\
              "os, sys, re, glob, time, getpass, shutil, signal, subprocess")#,\
              #flush = True)
        sys.stdout.flush()
        return False
    
    #USER_ID = getpass.getuser()
    #OS_SYSTEM = sys.platform
    #APPS_DIR = os.path.join("/","Users", USER_ID, "Desktop")  #macos
    #APPS_DIR = os.path.join( "C:", "Users", USER_ID,"Desktop")  #macos    
    
    #Anaconda Environment
    if 'Anaconda' in sys.version:
        try:
            import conda.cli
        except:
            print("FAILED IMPORT OF  conda.cli")#, flush = True)
            sys.stdout.flush()
        try:
            import datetime
        except:        
            if 'datetime' in sys.modules:    pass
            else:   conda.cli.main('conda', 'install',  '-y',  '-c',\
                                   'anaconda', 'dateutil'); 
                                   
        try:
            import pytz
        except:
            if 'pytz' in sys.modules:    pass
            else:   conda.cli.main('conda', 'install',  '-y', '-c',\
                                   'anaconda','pytz')

        # MAKE SURE THEY CAN BE IMPORTED AFTER THE INSTALL
        try:
            import pytz
            import datetime
            
        except:
            print("Could not import one or more of the modules - "\
                  "Anaconda.\nTry restarting Anaconda and re-run the ",\
                  "program otherwise follow the documentation to download ",\
                  "the necessary modules.")#, flush = True)
            sys.stdout.flush()
            return False
            
    else: # Not Anaconda environment
        try:
            import datetime
        except:
            if 'datetime' in sys.modules:    pass
            else: subprocess.call([sys.executable, "-m", "pip", "install", 'python-dateutil'])
        try:
            import pytz
        except:
            if 'pytz' in sys.modules:  pass 
            else: subprocess.call([sys.executable, "-m", "pip", "install", 'pytz'])
            
        # MAKE SURE THEY CAN BE IMPORTED AFTER THE INSTALL
        try:
            import pytz
            import datetime
            
        except:
            print("Could not import one or more of the modules - "\
                  "Non-Anaconda.\nTry installing/upgrading pip or download/use Anaconda and re-run the ",\
                  "program otherwise follow the documentation to download ",\
                  "the necessary modules.")#, flush = True)
            sys.stdout.flush()
            return False
        
    return True