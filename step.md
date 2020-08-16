
Create a new virtual environment with the following Python 3 command:
~~~
python3 -m venv pywhatsapp
~~~
If you are running Python 2, first install the virtualenv package then run the following command:
~~~
virtualenv pywhatsapp
~~~

~~~
source ./pywhatsapp/bin/activate
~~~
Install the Twilio Python helper library into the virtualenv:

~~~
pip install twilio
~~~
Create a file named whatsapp.py and write or paste in the following code:
~~from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client()

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+15005550006'

client.messages.create(body='Ahoy, world!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)~

~~~
