import re
import requests
import subprocess
import sys

try:
    def runSearch(domain):
        host = 'https://crt.sh/?q=%25.'
        site = host+domain

        r = requests.get(site)

        content = str(r.text)

        pattern = '<TD>(.*?)<BR>'
        search = re.findall(pattern, content)

        list = sorted(set(search))

        # clean invalid result
        for i in list:

            # remove @
            review = re.findall('@', i)
            if len(review) == 0:

                # remove wildcard *.
                review2 = re.findall('\*\.', i)
                if len(review2) == 0:
                    ping(i)

    def ping(host):
        import os, platform

        if  platform.system().lower() == "windows":
            #ping_str = "-n 1"
            print('TODO')
        else:
            try:
                args = 'ping -c 1 ' + host
                output = subprocess.check_output(args, shell=True)

                isActive = re.findall('..received', str(output))

                ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", str(output))
                ip = sorted(set(ip))

                if len(isActive[0]) == 10:
                    print('Host',host, ip, 'is active')
                else:
                    return 'erro'
            except:
                pass
except:
    print('Cancelled')

try:
    if len(sys.argv) == 2:
        input = sys.argv[1]

        runSearch(input)

    else:
        print('\nExecute: python3 crtresolve.py <domain>')
except:
    pass
    #print('\nExecute: python3 crtresolve.py <domain>')
