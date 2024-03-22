from dotenv import dotenv_values

env = dotenv_values("./.env")


def get_env_value(key: str, to_type, default=None):
    value = env.get(key)
    if value is None:
        return default

    try:
        return to_type(value)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid value for {key}: {value}") from e


api_id = get_env_value("API_ID", int)
api_hash = get_env_value("API_HASH", str)

db_name = get_env_value("DB_NAME", str)
stses = get_env_value("SESSION", str)
