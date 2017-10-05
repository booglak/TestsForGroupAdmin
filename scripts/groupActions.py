import requests
import testdata.whichDataUse as wdu
import _mssql


class GActions (object):

    host = wdu.host
    user = wdu.userAdmin

    dbhost = wdu.dbhost
    dbu = wdu.dbu
    dbp = wdu.dbp
    db = wdu.db

    def create_group(self):
        req = requests.post(self.host + '/GroupService/',
                            headers={'Authorization': self.user,
                                     'Content-Type': 'application/json'},
                            json={"IsNumberTouched": "true", "IsLimitTouched": "true",
                                  "Name": "Группа обучения №14", "OrganizationId": "23",
                                  "CompetenceId": "20", "Limit": "15", "Number": "14",
                                  "StartDate": "01.01.2019", "EndDate": "01.02.2019",
                                  "FileToupload": "{}", "Capacity": "15", "IsArchived": "false",
                                  "TeacherId": "null",
                                  "Organization": "ГАПОУ МО \"Межрегиональный центр компетенций - Техникум им. С.П. Королева\"",
                                  "Address": "ул. Молодежная, д. 7"})
        return req.json()

    def update_group(self, group_id):
        req = requests.put(self.host + '/GroupService/',
                            headers={'Authorization': self.user,
                                     'Content-Type': 'application/json'},
                            json={"Id": group_id, "IsNumberTouched": "true",
                                  "IsLimitTouched": "true",
                                  "Name": "Группа обучения №15", "OrganizationId": "23",
                                  "CompetenceId": "20", "Limit": "20", "Number": "15",
                                  "StartDate": "01.01.2019", "EndDate": "01.02.2019",
                                  "FileToupload": "{}", "Capacity": "20",
                                  "IsArchived": "false", "TeacherId": "null",
                                  "Organization": "ГАПОУ МО \"Межрегиональный центр компетенций - Техникум им. С.П. Королева\"",
                                  "Address": "ул. Молодежная, д. 7"})
        return req.json()

    def close_group(self, group_id):
        req = requests.put(self.host + '/GroupService/',
                            headers={'Authorization': self.user,
                                     'Content-Type': 'application/json'},
                            json={"Id": group_id, "IsNumberTouched": "true",
                                  "IsLimitTouched": "true",
                                  "Name": "Группа обучения №15", "OrganizationId": "23",
                                  "CompetenceId": "20", "Limit": "20", "Number": "15",
                                  "StartDate": "01.01.2019", "EndDate": "01.02.2019",
                                  "FileToupload": "{}", "Capacity": "20",
                                  "IsArchived": "true", "TeacherId": "null",
                                  "Organization": "ГАПОУ МО \"Межрегиональный центр компетенций - Техникум им. С.П. Королева\"",
                                  "Address": "ул. Молодежная, д. 7"})
        return req.json()

    def open_group(self, group_id):
        req = requests.put(self.host + '/GroupService/',
                            headers={'Authorization': self.user,
                                     'Content-Type': 'application/json'},
                            json={"Id": group_id, "IsNumberTouched": "true",
                                  "IsLimitTouched": "true",
                                  "Name": "Группа обучения №15", "OrganizationId": "23",
                                  "CompetenceId": "20", "Limit": "20", "Number": "15",
                                  "StartDate": "01.01.2019", "EndDate": "01.02.2019",
                                  "FileToupload": "{}", "Capacity": "20",
                                  "IsArchived": "false", "TeacherId": "null",
                                  "Organization": "ГАПОУ МО \"Межрегиональный центр компетенций - Техникум им. С.П. Королева\"",
                                  "Address": "ул. Молодежная, д. 7"})
        return req.json()

    def delete_group(self, group_id):
        conn = _mssql.connect(server=self.dbhost, user=self.dbu, password=self.dbp, \
                              database=self.db)
        conn.execute_non_query('DELETE FROM [WorldSkills].[dbo].[Group] WHERE Id=' + str(group_id))

        print("Group " + group_id + " DELETED")



a = GActions()
print(a.delete_group(791))

