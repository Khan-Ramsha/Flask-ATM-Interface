#creating project structure
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')



list_of_files=[
    'templates/change_pass.html',
    'templates/check_bal.html',
    'templates/deposit.html',
    'templates/withdraw.html',
    'src/utils.py',
    'src/logger.py',
    'src/exception.py',
    'components/withdraw.py',
    'components/deposit.py',
    'components/checkbal.py',
    'components/changepass.py',
    'app.py',
    'requirements.txt',
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating file directory:{filedir} for {filename}')
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'Creating empty file {filepath}')
    else:
        logging.info(f'{filename} already exist')