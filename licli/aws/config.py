import json
from pathlib import Path

from exceptions import handle_exception, AWSCredentialsNotFound


class AWSConfig:
    _credentials = {}
    _credentials_file_name = 'credentials.json'
    region_name: str
    access_key: str
    secret_key: str
    session_token: str
    mfa_arn: str

    def __init__(self, load_config=None):
        if load_config:
            self.load_config()

    def check_configuration(self):
        file_exists = Path(self._credentials_file_name).exists()
        if not file_exists:
            raise AWSCredentialsNotFound()

    @handle_exception
    def load_config(self):
        self.check_configuration()
        with open(self._credentials_file_name, 'r') as file:
            credentials = json.load(file)
            self.region_name = credentials.get('region_name')
            self.access_key = credentials.get('access_key')
            self.secret_key = credentials.get('secret_key')
            self.session_token = credentials.get('session_token')
            self.mfa_arn = credentials.get('mfa_arn')

    def write_local_config(self):
        with open(self._credentials_file_name, 'w+') as file:
            file.write(json.dumps(self._credentials))

    def configure(self, region_name, access_key, secret_key, mfa_arn, session_token=None):
        self._credentials = {'region_name': region_name,
                             'access_key': access_key,
                             'secret_key': secret_key,
                             'mfa_arn': mfa_arn,
                             'session_token': session_token}
        self.write_local_config()
