import requests
import testdata.testdata as td


class Files(object):

    host = td.host_oleg
    user = td.userAdmin_oleg

    def upload_timetable(self):
        req = requests.post(self.host + '/FileService/Timetable/600',
                            headers={'Authorization': self.user,
                                     'Content-Type':'multipart/form-data'},
                            data={'file': open('timetable.jpg', 'rb')})
        return req.json()

    def upload_certificate(self):
        req = requests.post(self.host + '/FileService/Certificate/5596',
                            headers={'Authorization': self.user,
                                     'Content-Type':'multipart/form-data'},
                            data={'file': open('sertificate.jpg', 'rb')})
        return req.json()


f = Files()
print(f.upload_timetable())
print(f.upload_certificate())