import numpy as np

class SatisfactionManager:

    def __init__(self):
        self.TEMP_MIN = 5
        self.TEMP_MAX = 40
        self.STEP = 0.1

        self._zero = np.vectorize(self._zero)
        self._tri = np.vectorize(self._tri)
        self._sat_tri = np.vectorize(self._sat_tri)
        self._trap = np.vectorize(self._trap)
        self._sat_trap = np.vectorize(self._sat_trap)
        self._gaussian = np.vectorize(self._gaussian)
        self._normal_gaussian = np.vectorize(self._normal_gaussian)
        self._agauss = np.vectorize(self._asym_gaussian)
        self.x = np.linspace(self.TEMP_MIN, self.TEMP_MAX, float(self.TEMP_MAX-self.TEMP_MIN)/self.STEP + 1)

    def _zero(self, x):
        return 0.0

    def _tri(self, a,m,b, x):
        if x < a:
            return 0.0
        elif x < m:
            return float(x - a)/(m-a)
        elif x < b:
            return -(float(x - b)/(b-m))
        else:
            return 0.0

    def _sat_tri(self, a,m,b, x):
        if x < a:
            return 0.0
        elif x < m:
            return float(x - a)/(m-a) * 5.0/10 + 5.0/10
        elif x < b:
            return -(float(x - b)/(b-m)) * 5.0/10 + 5.0/10
        else:
            return 0.0

    def _trap(self, a,m1,m2,b, x):
        if x < a:
            return 0.0
        elif x < m1:
            return float(x - a)/(m1-a)
        elif x < m2:
            return 1.0
        elif x < b:
            return -(float(x - b)/(b-m2))
        else:
            return 0.0

    def _sat_trap(self, a,m1,m2,b, x):
        if x < a:
            return 0.0
        elif x < m1:
            return float(x - a)/(m1-a) * 5.0/10 + 5.0/10
        elif x < m2:
            return 1.0
        elif x < b:
            return -(float(x - b)/(b-m2)) * 5.0/10 + 5.0/10
        else:
            return 0.0

    def _gaussian(self, mu, sigma, x):
        return np.e**(-(x-mu)**2/(2 * sigma**2))/(np.sqrt(2 * np.pi) * sigma)

    def _normal_gaussian(self, mu, sigma, x):
        return self._gaussian(mu, sigma, x)/self._gaussian(mu,sigma,mu)

    def _asym_gaussian(self, mu, sigma1, sigma2, x):
        if x <= mu:
            return self._normal_gaussian(mu, sigma1, x)
        else:
            return self._normal_gaussian(mu, sigma2, x)

    def zero(self):
        return self._zero(self.x)

    def agauss(self, mu, sigma1, sigma2):
        return self._agauss(mu, sigma1, sigma2, self.x)

    def gauss(self, mu, sigma,):
        return self._gauss(mu, sigma, self.x)

    def getMax(self, values):
        return values.argmax() * self.STEP + self.TEMP_MIN

    def getMaxPriority(self, values):
        return values.max()

