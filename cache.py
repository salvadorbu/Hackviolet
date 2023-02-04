import pickle

class Cache:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.cache = {}
        try:
            with open(filename, "rb") as file:
                self.cache = pickle.load(file)
        except FileNotFoundError:
            pass

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value
        with open(self.filename, "wb") as file:
            pickle.dump(self.cache, file)