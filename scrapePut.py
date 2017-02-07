#sudo pip install requests
#sudo pip install python-firebase
import urllib2
from firebase import firebase

#get jackpot lump sums
html = urllib2.urlopen('http://www.walottery.com/JackpotGames/').read()

x = []
x = html.split('<p>Cash Option <strong>')
tmpPower = x[1].split(' Million*</strong></p>')
tmpMega = x[2].split(' Million*</strong></p>')

power = tmpPower[0].strip('$')
mega = tmpMega[0].strip('$')

powerAfterTax = float(power) * .604
megaAfterTax = float(mega) * .604

print '\033[95m'
print '\033[92m' + "Power: "+ str(powerAfterTax)
print '\033[94m' + "Mega: "+str(megaAfterTax)
print '\033[0m'


#post to firebase
firebase = firebase.FirebaseApplication('https://lotto-5ff57.firebaseio.com', None)
result = firebase.get('/data', None)
print result