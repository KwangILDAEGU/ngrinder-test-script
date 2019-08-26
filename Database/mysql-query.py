# -*- coding:utf-8 -*-
# mysql Database test.
#
from java.sql import DriverManager
from com.mysql.jdbc import Driver
from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from java.util import Random
from java.lang import System
 
DB_SERVER_IP = "<>:3306"
DATABASE	 = ""
# Parameters
DB_connect = "jdbc:mysql://" + DB_SERVER_IP + "/" + DATABASE
DB_user = "root"
DB_password = ""
 
   
test1 = Test(1, "Database select")
random = Random(long(System.nanoTime()))
   
# Load the JDBC driver.
DriverManager.registerDriver(Driver())
 
   
def getConnection():
    return DriverManager.getConnection(DB_connect, DB_user, DB_password)
   
def ensureClosed(object):
    try: object.close()
    except: pass
       
class TestRunner:
    def __init__(self):
        test1.record(TestRunner.__call__)
        grinder.statistics.delayReports=True
        pass
 
    def __call__(self):
        connection = None
        selectStatement = None
        try:
            # in this test, we will create connection and statement in every test transaction.
            connection = getConnection()
            selectStatement = connection.createStatement()
            selectStatement.execute("QUERY")
             
        finally:
            ensureClosed(selectStatement)