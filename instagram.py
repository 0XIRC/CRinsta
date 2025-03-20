#! /usr/bin/python3.13
#    This module is maintained by Marc-Andre Lemburg <mal@github.com>.
#    If you find problems, please submit bug reports/patches via the
#    Python issue tracker (https://github.com/) and
#    mention "@".
#
__copyright__ = """
    Copyright (c) 1999-2000, Marc-Andre Lemburg; mailto:mal@lemburg.com
    Copyright (c) 2000-2010, eGenix.com Software GmbH; mailto:info@egenix.com

    Permission to use, copy, modify, and distribute this software and its
    documentation for any purpose and without fee or royalty is hereby granted,
    provided that the above copyright notice appear in all copies and that
    both that copyright notice and this permission notice appear in
    supporting documentation or portions thereof, including modifications,
    that you make.
"""

__version__ = '1.0.0'

import sourc.ortime, sourc.veryfy
if sourc.veryfy.is_virtual_machine() == False:
    def main(): 
        # SHOW intro 
        print('''

    ▗▄▄▖▗▄▄▖ ▗▄▄▄▖▗▖  ▗▖ ▗▄▄▖▗▄▄▄▖ ▗▄▖ 
    ▐▌   ▐▌ ▐▌  █  ▐▛▚▖▐▌▐▌     █  ▐▌ ▐▌
    ▐▌   ▐▛▀▚▖  █  ▐▌ ▝▜▌ ▝▀▚▖  █  ▐▛▀▜▌ 
    ▝▚▄▄▖▐▌ ▐▌▗▄█▄▖▐▌  ▐▌▗▄▄▞▘  █  ▐▌ ▐▌ v0.1 
                                        
                                        
    \033[33mCRINSTA v1.0 (c) 2025 by 0XIRC/THC & David IRCS - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway). 
    \33[37m
    1-Instagram crack with ID and password list entry
    2- Crack Instagram with (default) password list
            ''')
        
        def inputclass(): 
            malborn = int(input("\033[32m[number] : Enter the number you want to crack:‌")) 
            
            if malborn == 1: 
                usernaME = str(input("\033[32m[string] : Enter the ID of the person you want to hack without the @:"))
                print(f"""\033[31mhttps://www.instagram.com/@{usernaME} """) 
                sourc.ortime.overtimeorg()

            elif malborn == 2: 
                passwordlist = str(input("enter passwordlist: "))
                sourc.ortime.overtimeorg() 

        inputclass() 
    main()

    
else:
    exit()