# log_config.py

import os

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

