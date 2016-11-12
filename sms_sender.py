from twilio.rest import TwilioRestClient

class SmsSender(object):
    def __init__(self, account_sid, auth_token, from_number):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number

    def send(self, to_number, message):
        print "Sending to %s" % to_number
        print message
        # client = TwilioRestClient(self.account_sid, self.auth_token)
        # message = client.messages.create(to=to_number, from_=self.from_number, body=message)
