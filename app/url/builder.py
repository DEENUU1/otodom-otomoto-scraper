from abc import ABC, abstractmethod


class URLBuilder(ABC):
    @abstractmethod
    def build_base_url(self):
        pass

    @abstractmethod
    def add_parameter(self, key, value):
        pass

    @abstractmethod
    def get_url(self):
        pass


class WebScraperURLBuilder(URLBuilder):
    def __init__(self, base_url):
        self.base_url = base_url
        self.parameters = {}

    def build_base_url(self):
        return self.base_url

    def add_parameter(self, key, value):
        self.parameters[key] = value

    def get_url(self):
        url = self.base_url + "?"
        url += "&".join([f"{key}={value}" for key, value in self.parameters.items()])
        return url


class URLDirector:
    def __init__(self, builder: WebScraperURLBuilder):
        self.builder = builder

    def construct_url(self):
        self.builder.build_base_url()


# builder = WebScraperURLBuilder("https://example.com")
# director = URLDirector(builder)
# director.construct_url()
# builder.add_parameter("location", "example_location")
# builder.add_parameter("price", "example_price")
# real_estate_url = builder.get_url()
# print(real_estate_url)