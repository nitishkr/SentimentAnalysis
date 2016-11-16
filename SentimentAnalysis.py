__author__ = 'venky'

import  sys


from training import trainmodel
from testting import gettestvector


reload(sys)
sys.setdefaultencoding('utf8')

#data = list(csv.reader(open("/home/venky/Sem1/Machine Learning/Project/Data/training.csv")))

model = trainmodel()

testvector =gettestvector()

for i in range(len(testvector)):

    print testvector[i]

result = model.predict(testvector)

for i in range(len(result)):

    print result[i]
















