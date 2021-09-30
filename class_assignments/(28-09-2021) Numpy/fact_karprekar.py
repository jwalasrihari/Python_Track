import numpy as np
import json
from flask import jsonify
def create_json(data):
    with open("fact_karprekar.json", "w") as file:
        return json.dump(data, file)


#factorial
fact=[1]
for i in range(1,10):
    fact.append(fact[i-1]*i)

fact=list(map(str,fact))
print(fact)
#karperkar
lst=np.arange(1,10000)
kar=['1']
for i in lst:
    j=str(i*i)
    for k in range(1,len(j)):
        x=int(j[:k])+int(j[k:])
        if x==i and x%10!=0:
            kar.append(str(i))
            break
print(kar)
kar=list(kar)
both={"fact":fact,"karperkar":kar}
create_json(both)