import json
import keywords
import time
def lambda_handler(event, context):
    start = time.time()
    if ("sandbox" not in event) or (type(event["sandbox"]) != bool):
        return {
        'statusCode': 400,
            'body': json.dumps({"error":"No sandbox presend"})
        } 
    
    sandbox = event["sandbox"]
    if sandbox == True:
        f = open('masterJson.json')
        masterJson = json.load(f)
        print(json.dumps(masterJson))
        return {
            'statusCode': 201,
            'body': json.dumps(masterJson)
        } 



    #error handle if event has no field "page"
    if "page" not in event:
        return {
        'statusCode': 400,
            'body': json.dumps({"error":"Page not present in event object"})
        } 
    
    try:
        if event["page"] == "keywords-analyze-volume-history":
            keyAPI = keywords.keywordsAPI(sandbox=sandbox)
            result = keyAPI.Volume_History(event["args"]["keyword"], 
                                            event["args"]["location_code"], 
                                            event["args"]["language_code"])    
        elif event["page"] == "keywords-analyze-search-intent":
            keyAPI = keywords.keywordsAPI(sandbox=sandbox)
            result = keyAPI.Search_Intent(event["args"]["keyword"], 
                                            event["args"]["location_code"], 
                                            event["args"]["language_code"])    
        elif event["page"] == "keywords-analyze-trends-data":
            keyAPI = keywords.keywordsAPI(sandbox=sandbox)
            result = keyAPI.Trends_Data(event["args"]["keyword"])                         
        elif event["page"] == "keywords-analyze-related-keywords":
            keyAPI = keywords.keywordsAPI(sandbox=sandbox)
            result = keyAPI.Related_Keywords(event["args"]["keyword"], 
                                            event["args"]["location_code"], 
                                            event["args"]["language_code"])  
        else:
            return {
            'statusCode': 400,
                'body': json.dumps({"error":"No match for event[page] = " + str(event["page"])})
            } 
        result["time"] = time.time() - start
        print(json.dumps(result))
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
    except:
        return {
            'statusCode': 500,
            'body': json.dumps("Error")
        }
