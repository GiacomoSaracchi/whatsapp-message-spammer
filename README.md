# whatsapp-message-spammer
A single file containing the MessageSpammer class used to send or spam different kinds of text on Whatsapp Web

The code uses Selenium to access and navigate Whatsapp.
It will need authentication (through scanning a QR code with your phone) upon accessing the web page as Whatsapp isn't necessarily compliant with automation.
The class enables you to send texts efforlessly, while voice messages and other forms of messages are a little tricker and currently undergoing improvements.

### INSTRUCTIONS FOR USE

First class 'argument' in Whatsapp Web Html (_3FRCZ in my case) is not the same across all devices.
Go on your Whatsapp Web page and inspect the message input box or the contact input box.
Look at Html to find your own class code.
This is relevant across all xpaths searches.

1. Call MessageSpammer
2. Use contact function to access any chat
3. Send messages
4. Quit driver using close function
