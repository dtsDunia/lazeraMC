import os
import subprocess
import yagmail
import requests

TELEGRAM_TOKEN = 'YOURTELEGRAMTOKEN'
TELEGRAM_CHAT_ID = 'CHATIDDESTINATION'

def sendTele(message):
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }
        return requests.post("https://api.telegram.org/bot{token}/sendMessage".format(token=TELEGRAM_TOKEN),
                             data=payload).content

yagmail.register('YOURMAIL@gmail.com', 'YOURPASSWORD')
yag = yagmail.SMTP('YOURMAIL@gmail.com','YOURPASSWORD')

def mailer(data,uname):
    yag.send(to = "RECEIVEREMAIL@gmail.com", subject = uname+" masuk dunia Lazera", contents = data[3].strip())

proses = subprocess.Popen(["/etc/init.d/minecraft_server", "log"],shell=False,stdout=subprocess.PIPE)

def kirimEmail(data,uname):
#    print "wkt :"+data[0]+":"+data[1]+":"+data[2]
    print "action : "+data[3].strip()
    print "uname :-"+uname+"-"
    if uname == "aurora_gmn" or uname == "langit_kuat" or uname == "ZEA_althauf" :
      print "gak kirim email"
    else :
      sendTele(uname+" masuk dunia Lazera -->"+data[3].strip())
      mailer(data,uname)
      print "kirim email"

while True:
  output = proses.stdout.readline()
  if proses.poll() is not None:
    break
  if output:
    theData = output.strip()
    last = theData.split(":")
    if isinstance(last, list) :
      if len(last) == 1 :
         print "mulai"
      elif len(last) > 1 :
         try :
          if len(last[3].strip().split()) != 1 :
            kata = last[3].strip().split()
#            print kata 
            if kata[0] == "UUID" :
               kirimEmail(last,kata[3])
        except Exception, e:
          print e
      else:
         print "error nih "
         print last
    else :
      print last
