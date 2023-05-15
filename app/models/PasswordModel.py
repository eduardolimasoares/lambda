from dataclasses import dataclass

@dataclass
class Password:
    email: str
    password: str
    views: int
    time_views: int
    url: str
    expire: bool
    date_free: str
    last_updated: str
    use_symbols: bool
    use_numbers: bool
    use_words: bool
    pass_size: bool
