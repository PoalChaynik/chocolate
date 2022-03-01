import datetime as time
import json

print(time.datetime.now())

print(time.datetime(2005,12,12))

"""
%A - diena
%d - menesa diena
%j - diena gada
%B - menesis
"""

a = time.datetime.now()
parv_laiks = a.isoformat()
json_a = json.dumps(parv_laiks)
print(json_a)