class Hotel:
    def __init__(self):
        self._name = ''
        self._details_url = ''
        self._score = 0.0
        self._location = ''
        self._stars = 0
        self._price = 0.0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        self._name = v.replace('\n', '')

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, v):
        score_v = v.replace('\n', '')
        score_v = score_v.replace(',', '.')
        self._score = round(float(score_v), 1)

    @property
    def details_url(self):
        return self._details_url

    @details_url.setter
    def details_url(self, v):
        self._details_url = v

    @property
    def stars_count(self):
        return self._stars

    @stars_count.setter
    def stars_count(self, v):
        self._stars = v

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, v):
        self._price = v

    def __str__(self):
        return f"{self._name} : {self.details_url}"
