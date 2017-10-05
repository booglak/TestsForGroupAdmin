import requests
import testdata.whichDataUse as wdu


class GetData(object):

    host = wdu.host
    user = wdu.userAdmin

    def get_groups(self):
        req = requests.get(self.host + '/GroupService/20?organizationId=23',
                           headers={'Authorization': self.user})
        return req.json()

    def get_admin(self):
        req = requests.get(self.host + '/OrganizationService/Administrator/470',
                           headers={'Authorization': self.user})
        return req.json()

    def get_usersgroup1(self):
        req = requests.get(self.host + '/GroupParticipantService/600?isReserve=false',
                           headers={'Authorization': self.user})
        return req.json()

    def get_usersgroup1_reserve(self):
        req = requests.get(self.host + '/GroupParticipantService/600?isReserve=true',
                           headers={'Authorization': self.user})
        return req.json()


# g = GetData()
# print(g.get_groups())
# print(g.get_admin())
# print(g.get_usersgroup1_reserve())
