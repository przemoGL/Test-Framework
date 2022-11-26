class BaseBrowser:

    @classmethod
    def get_driver(cls):
        raise NotImplementedError("Not implemented")
