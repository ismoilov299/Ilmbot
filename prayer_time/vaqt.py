import requests


class NamozVaqti():

    def __init__(self, city):
        self.city = city
        self.url = 'https://islomapi.uz/api/present/day?region=' + \
            self.city
        self.response = requests.get(self.url)
        self.data = self.response.json()

    def get_sana(self):
        return self.data['date']

    def get_kun(self):
        return self.data['weekday']

    def get_namoz_vaqt(self):
        return self.data['times']

    def bomdod(self):
        return self.get_namoz_vaqt()['tong_saharlik']

    def quyosh_chiqishi(self):
        return self.get_namoz_vaqt()['quyosh']

    def peshin(self):
        return self.get_namoz_vaqt()['peshin']

    def asr(self):
        return self.get_namoz_vaqt()['asr']

    def shom(self):
        return self.get_namoz_vaqt()['shom_iftor']

    def xufton(self):
        return self.get_namoz_vaqt()['hufton']
