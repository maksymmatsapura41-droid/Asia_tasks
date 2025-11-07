# Class AppConfig Class variable: settings = {}
# Class method: load_from_dict(cls, data_dict) updates shared config
# Static method: is_valid_key(key) → alphanumeric only
# Raise error if invalid config key write this task


class AppConfig:
    settings = {}

    @staticmethod
    def is_valid_key(key):
        return key.isalnum()

    @classmethod
    def load_from_dict(cls, data_dict):
        for key, value in data_dict.items():
            if not cls.is_valid_key(key):
                raise ValueError(f"Invalid config key: {key}")
        cls.settings.update(data_dict)


AppConfig.load_from_dict({"theme": "dark", "volume": 70})
print(AppConfig.settings)  # {'theme': 'dark', 'volume': 70}

try:
    AppConfig.load_from_dict({"invalid-key": True})
except ValueError as e:
    print(e)
