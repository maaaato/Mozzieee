from credentials import Credentials
from boto3 import Session


class Aschedule(object):
    '''
    AutoScaling Schedule Class
    '''    
    
    def __init__(self, app_code):
        self.credentials = Credentials.load_by_conf(app_code)
        session = Session(aws_access_key_id=self.credentials.aws_access_key_id,
                           aws_secret_access_key=self.credentials.aws_sercret_access_key_id)
        self.client = session.client('autoscaling')

    
    def getSchedule(self):
        schedule = self.client.describe_scheduled_actions()
        
        return schedule["ScheduledUpdateGroupActions"]

        
