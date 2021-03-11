from twilio.rest import Client


#add in Twilio_sid and auth_token from Twilio account 

def msg_friends(event=None, context=None):

    # get your sid and auth token from twilio
    twilio_sid = 'TwilioSSIDgoesHere'
    auth_token = 'TwilioAuthgoesHere'

    whatsapp_client = Client(twilio_sid, auth_token)

    # Add in names and numbers in list. Multiple names and numbers can be added.
    contact_directory = {'Name Goes Here' : 'Number goes here',}

    # for each key - contact in the contact_directory, send the following message.
    for key, value in contact_directory.items():
        msg_the_friends = whatsapp_client.messages.create(
                body = 'Beep beep {} ! Skeptics Subscription WhatsApp Group welcomes you once again. '.format(key),
                from_= 'whatsapp:+14155238886',
                to= 'whatsapp:' + value,

            )

        print(msg_the_friends.sid)
