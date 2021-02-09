class Config:
    pass


class Devlopment(Config):
    pass


class Production(Config):
    pass


config = {
    'dev': Devlopment,
    'prod': Production,
}
