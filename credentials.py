import ConfigParser
import boto3


class Credentials(object):
    '''
    Aws Credential Class
    '''

    @classmethod
    def load_by_conf(cls, app_code):
        config = ConfigParser.SafeConfigParser()        
        config.read('aws.conf')
        access_key_id = config.get(app_code, 'aws_access_key_id')
        sercret_key_id = config.get(app_code, 'aws_sercret_access_key_id')
        return cls(app_code, access_key_id, sercret_key_id)

        
    def __init__(self, app_code, aws_access_key, aws_secret_access_key):    
        self.app_code = app_code
        self.aws_access_key_id = aws_access_key
        self.aws_sercret_access_key_id = aws_secret_access_key
