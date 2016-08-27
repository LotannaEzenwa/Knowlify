import sys
import os

DATA_DIR = './data/'
MPORT = 8000


if not os.path.isdir(DATA_DIR):
    os.mkdir(DATA_DIR)

sys.path.append(DATA_DIR)