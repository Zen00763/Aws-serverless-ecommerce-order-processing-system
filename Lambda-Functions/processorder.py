import json
import boto3

sns = boto3.client('sns')

TOPIC_ARN = "arn:aws:sns:us-east-1:857876979780:OrderNotifications"

def lambda_handler(event, context):

    try:

        for record in event['Records']:

            order = json.loads(record['body'])

            sns.publish(
                TopicArn="arn:aws:sns:us-east-1:857876979780:OrderNotifications",
                Subject='New Order Processed',
                Message=f"""
ORDER RECEIVED

Order ID: {order['orderId']}

Customer Name: {order['customerName']}

Customer Email: {order['customerEmail']}

Product: {order['productName']}

Quantity: {order['quantity']}

Status: PROCESSED
"""
            )

        return {
            'statusCode': 200,
            'body': json.dumps('Success')
        }

    except Exception as e:

        print(str(e))
        raise e