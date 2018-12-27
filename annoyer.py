from config import Config
from reader import Reader
from sms_sender import SmsSender

conf = Config("twilio.cfg")
print(conf.get("twilio"))
facts = Reader("facts.txt")
twilio_options = conf.get("twilio")
victim_number = conf.get("victim")['number']
sms = SmsSender(twilio_options['account'], twilio_options['token'], twilio_options['number'])

message = """
Did you know?
%s

Enjoy your #AnnoyMitoDay!""" % facts.getRandomLine()
sms.send(victim_number, message)
