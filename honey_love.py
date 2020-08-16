from twilio.rest import Client 
 
account_sid = 'ACe5327a6dc0dd98685ad7b7eace68107a' 
auth_token = '8b7fbf0c5557b88e6b5b76f3fd7a46qw' 
client = Client(account_sid, auth_token) 
def send_love: 
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='hiii good morning',      
                              to='whatsapp:+91xxxxxxxxxx' 
                                ) 
 
    print(message.sid)
