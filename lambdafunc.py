
import boto3
import os 
import json

#Function is used to get current count in dynamoDB table 
#followed by adding 1 to the current visitor count & updating the table. 
def lambda_handler(event, context): 
    visit_count = 0
    
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ["TABLE_NAME"]
    table = dynamodb.Table(table_name)
    
    #get curr count 
    response = table.get_item(
        Key = {
            "Visit_Count": "First_Item"
        }
    )
    
    if "Item" in response:
        visit_count = response["Item"]["count"] 
        #Increment Visit Count
        visit_count +=1 


    #Updated visit count in table 
    table.put_item(
        Item = {
            "Visit_Count": "First_Item",
            "count": visit_count
        }
    )
    message = f'You are the {visit_count} visitor"'

    return {
            'statusCode': 200,
            'body': json.dumps(message)
            
    }



