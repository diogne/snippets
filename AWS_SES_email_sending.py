from secrets import SES_ACCESS_ID, SES_ACCESS_SECRET_KEY
import boto3



def send_email(subject="sujet du mail", 
               msg="Message du email",
               to_addresses=['jerome.riou@gmail.com']):
    AWS_REGION = "eu-west-3"

    client = boto3.client('ses',
            aws_access_key_id=SES_ACCESS_ID,
            aws_secret_access_key=SES_ACCESS_SECRET_KEY,
            region_name=AWS_REGION)


    response = client.send_email(
        Source='jerome.riou@gmail.com',
        Destination={
            'ToAddresses': [
                'jerome.riou@gmail.com',
                'anagraal.sympa@gmail.com',
            ],
        },
        Message={
            'Subject': {
                'Data': f'{subject}',
            },
            'Body': {
                'Html': {
                    'Data': f'{msg}',
                },
            }
        },
    )
    
    return response
    

if __name__ == '__main__':
    send_notification_email()