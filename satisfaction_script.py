from SatisfactionManager import SatisfactionManager
import json
import numpy as np
import matplotlib.pyplot as plt 

APPLICATION_ID = "8xgkmfNMWhCI2hfE5qwU6Rchto9gpQbwLBc0v4nB"
REST_API_KEY = "1IsdRK3mZnRY4xKMHpwOS3IfvJIm4l1aliyhambD"

activeUsers = {
	'mario.polino': None,
	'pierfreeman': None,
	'Leonerd': None,
	'rolando': None,
	'rpressiani': None,
	'kirves': None,				# Frossi
	'amedeo.asnaghi': None,
	'matteo.ferroni': None,
	# 'LucaCerina': None,
	# 'GuidoL': None,
	# 'giuliacore': None,
	'mpogliani': None,
	'andreatello': None,
	'andreaciri': None,


}

# GetUsers
import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('GET', '/1/classes/_User', '', {
       "X-Parse-Application-Id": "8xgkmfNMWhCI2hfE5qwU6Rchto9gpQbwLBc0v4nB",
       "X-Parse-REST-API-Key": "1IsdRK3mZnRY4xKMHpwOS3IfvJIm4l1aliyhambD"
     })
results = json.loads(connection.getresponse().read())['results']

for u in results:
	username = u['username']
	if username in activeUsers.keys():
		user = {} 
		user['ideal']= int(u['tempIdeal'])
		user['sigma1']= int(u['tempMin'])
		user['sigma2']= int(u['tempMax'])
		user['priority'] = 1
		activeUsers[username] = user

# Satisfaction
satisfactionManager = SatisfactionManager()
values = satisfactionManager.zero()

for user, data in activeUsers.iteritems():
	if data != None:
	    ideal = data['ideal']
	    sigma1 = data['sigma1']
	    sigma2 = data['sigma2']
	    priority = data['priority']

	    print user, ideal, sigma1, sigma2
	    curve = priority*satisfactionManager.agauss(ideal,sigma1,sigma2)
	    plt.plot(satisfactionManager.x, curve, '-')
	    values += curve

plt.plot(satisfactionManager.x, values, '-')

finalValue = satisfactionManager.getMax(values)
finalPriority = satisfactionManager.getMaxPriority(values)
print finalValue
plt.show()