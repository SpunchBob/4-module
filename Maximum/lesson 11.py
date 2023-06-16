class Windows:
    def __init__(self, version, country):
        self.__version = version
        self._country = country

windows11 = Windows(11, "Russian Federation")
print(windows11._country)
windows11._country = "China"
print(windows11._country)

print(windows11.__version)
windows11.__version = "China"
print(windows11.__version)