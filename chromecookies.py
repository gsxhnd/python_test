import subprocess
from sqlite3.dbapi2 import *
from _sqlite3 import *
import sqlite3
import re,os
import requests
import win32crypt


def get_chrome_cookie(domain_name):
    dist_cookie_name = 'python_chrome_cookies'
    sour_cookie_name = os.path.join(os.environ['LOCALAPPDATA'],r'Google\Chrome\User Data\Default\Cookies')
    if not os.path.exists(sour_cookie_name):
        raise Exception('cookie not exist')
    subprocess.call(['copy',sour_cookie_name,dist_cookie_name],shell=True)
    conn =sqlite3.connect(dist_cookie_name)
    ret_dict={}
    for row in conn.execute("SELECT host_key, name, path, value, encrypted_value FROM cookies"):
        if row[0] != domain_name:
            continue
        ret = win32crypt.CryptUnprotectData(row[4], None, None, None, 0)
        ret_dict[row[1]] = ret[1].decode()
    conn.close()
    subprocess.call(['del',dist_cookie_name],shell=True)
    return ret_dict