#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 10 load values into the pets database"""

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('pets.db')
    c = con.cursor()
    
    c.execute('''DROP TABLE IF EXISTS person;''')
    c.execute('''DROP TABLE IF EXISTS pet;''')
    c.execute('''DROP TABLE IF EXISTS person_pet;''')


    c.execute('''INSERT INTO person VALUES(1,'James','Smith',41);
        INSERT INTO person VALUES(2,'Diana','Greene',23);
        INSERT INTO person VALUES(3,'Sara','White',27);
        INSERT INTO person VALUES(4,'William','Gibson',23);''')
    c.execute('''INSERT INTO pet VALUES(1,'Rusty','Dalmation',4,1);
        INSERT INTO pet VALUES(2,'Bella','AlaskanMalamute',3,0);
        INSERT INTO pet VALUES(3,'Max','CockerSpaniel',1,0);
        INSERT INTO pet VALUES(4,'Rocky','Beagle',7,0);
        INSERT INTO pet VALUES(6,'Spot','Bloodhound',2,1);''')
    c.execute('''INSERT INTO person_pet VALUES(1,1);
        INSERT INTO person_pet VALUES(1,2);
        INSERT INTO person_pet VALUES(2,3);
        INSERT INTO person_pet VALUES(2,4);
        INSERT INTO person_pet VALUES(3,5);
        INSERT INTO person_pet VALUES(4,6);''')
    con.commit()

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()
