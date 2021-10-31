import requests
import json
 #Old version
userid = str('Eliza')
apikey = '#########'
 
# Create post function
def robot(content):
    # Amber api
    api = r'#########' 
    # Create post submitted data
    data = {
        "perception": {
            "inputText": {
                "text": content
                         }
                      },
        "userInfo": {
                    "apiKey": apikey,
                    "userId": userid,
                    }
    }
    # Convert to json format
    jsondata = json.dumps(data)
    # Initiate a post request
    response = requests.post(api, data = jsondata)
    # Decode the returned json data
    robot_res = json.loads(response.content)
    # Extract conversation data
    print(robot_res["results"][0]['values']['text'])
 
for x in range(100):
    content = input("talk:")
    # Enter the content of the conversation 
    robot(content)
    if x == 100:
        break 
 
while True:
    content = input("talk:")
    # Enter the content of the conversation 
    robot(content)
    if content == 'bye':
    # Set stopwords
        break
 
# # Create an endless loop of dialogue
# while True:
# # Enter the content of the conversation
# content = input("talk:")
