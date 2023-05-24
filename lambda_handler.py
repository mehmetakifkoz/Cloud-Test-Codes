import json

def lambda_handler(event, context):
    # Parse the input from the Lambda event
    num = int(event['num'])
    fib_num = int(event['fib_num'])

    # Call the logic function
    result = calculate_factorial_and_fibonacci(num, fib_num)

    # Return the result as a JSON response
    response = {
        'statusCode': 200,
        'body': json.dumps(result)
    }

    return response
