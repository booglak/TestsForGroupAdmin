import testdata.testdata as td

Environment = 'test'

if Environment == 'test':
    host = td.host_test
    userAdmin = td.userAdmin_test
    userAdminWs = td.wsAdmin_test
    dbhost = td.dbHost_test
    dbu = td.dbUser_test
    dbp = td.dbPass_test
    db = td.db_test

elif Environment == 'oleg':
    host = td.host_oleg
    userAdmin = td.userAdmin_oleg
    userAdminWs = td.wsAdmin_oleg
    dbhost = td.dbHost_oleg
    dbu = td.dbUser_oleg
    dbp = td.dbPass_oleg
    db = td.db_oleg

elif Environment == 'prod':
    host = td.host_prod
    userAdmin = td.userAdmin_prod
    userAdminWs = td.wsAdmin_prod
    dbhost = td.dbHost_prod
    dbu = td.dbUser_prod
    dbp = td.dbPass_prod
    db = td.db_prod

else:
    print('!!!!!!!!!!!!!!!! Wrong Environment !!!!!!!!!!!!!!!!!!!!!')