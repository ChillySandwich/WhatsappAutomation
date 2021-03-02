from twilio.rest import Client

def msg_friends(event=None, context=None):

    # get your sid and auth token from twilio
    twilio_sid = 'TwilioSSIDgoesHere'
    auth_token = 'TwilioAuthgoesHere'

    whatsapp_client = Client(twilio_sid, auth_token)

    # keep adding contacts to this dict to send
    # them the message
    contact_directory = {'Name Goes Here' : 'Number goes here',}


    for key, value in contact_directory.items():
        msg_the_friends = whatsapp_client.messages.create(
                body = 'Beep beep {} ! Skeptics Subscription WhatsApp Group welcomes you once again. '.format(key),
                from_= 'whatsapp:+14155238886',
                to= 'whatsapp:' + value,

            )

        print(msg_the_friends.sid)