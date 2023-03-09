#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Plant Care"
    database_url: str
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()
