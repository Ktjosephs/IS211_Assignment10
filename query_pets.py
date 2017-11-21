#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week 10."""


import sqlite3 as lite
import sys

con = None 

try:
    con = lite.connect('pets.db') 
    con.row_factory = lite.Row 

    while True:
        choice = raw_input('Enter ID number: ')

        if choice == '-1':
            sys.exit() 
        
        else:
            try:
                choice = int(choice)

            except:
                print "Invalid ID: Enter a valid id"
                continue

        cur = con.cursor()
        cur.execute("SELECT * FROM person WHERE id =?", [(choice)]) 
        row = cur.fetchone() 

        if row == None:
            print 'Invalid ID number. Choose another id.'
            continue

        print row['first_name'] + ' ' + row['last_name'] + ' is ' + str(
            row['age']) + ' yrs old.'


        for row in con.execute(
            "SELECT * FROM person_pet WHERE person_id =?", [(choice)]):

            for name in con.execute(
                "SELECT * FROM person WHERE id =?", [(choice)]):
                pet_owner = name['first_name'] + ' ' + name['last_name']


            for row_pet in con.execute(
                "SELECT * FROM pet WHERE id =?", [(row['pet_id'])]):

                if row_pet['dead'] == 0:
                    print (pet_owner + ' owned ' + row_pet[
                    'name'] + ', a ' + row_pet['breed'] + ' who was ' + str(
                        row_pet['age']) + ' years old.')
            else:
                if row_pet['dead'] != 0:
                    print (pet_owner + ' owns ' + row_pet[
                        'name'] + ', a ' + row_pet['breed'] + ' who is ' + str(
                            row_pet['age']) + ' years old.')

except lite.Error as e:
    print "Error: %s " % e.args[0]
    sys.exit(1)

finally:
    if con:
        con.close()
