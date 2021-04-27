# global-trie-cli

Online trie system created with AWS Lambda


## Installation
To install the program, `npm` is required: https://www.npmjs.com/get-npm \
Command: ```npm install -g global-trie-cli```

## Usage

trie [command] <options>

    add                 add a keyword to trie
    delete              delete a keyword from trie
    search              search for a keyword in trie (returns True/False)
    autocomplete        return list of autocomplete suggestion based on an input prefix
    print               display the trie

Options: 

    --keyword:          specify keyword

## Technologies
1. Amazon Web Service Lambda: Serverless online platform that handles input, updates the tree, and returns an output. 
   To see the details of the Lambda code, see `lambda_code.py` in the Github repository. 
2. Amazon S3: Stores the serialized `trie` object in a bucket. 
3. REST API Gateway: Sends client requests to Lambda and returns a response back to the client. 

## Client-Lambda Interaction

A REST API Gateway is used to send and receive data to/from Lambda. The URL is `https://cjql8lovja.execute-api.us-east-2.amazonaws.com/trie_stage/lambda`. The parameters `type` and `keyword` are required when invoking the API. \
To invoke the API, use the `curl` command. Note that the output is raw and not parsed yet. \
Example: \
Add: `curl -X GET "https://cjql8lovja.execute-api.us-east-2.amazonaws.com/trie_stage/lambda?type=add&keyword=apple"` \
Print: `curl -X GET "https://cjql8lovja.execute-api.us-east-2.amazonaws.com/trie_stage/lambda?type=print&keyword=null"`

## Lambda
Lambda receives the arguments `type` and `keyword` from the API Gateway. Then it retrieves the `trie` pickle object from `trie-storage` bucket in Amazon S3 and "unpickles" it. (If the object does not exist, then Lambda will initialize one). \
Based on the `type` argument, Lambda handles the input and updates the tree if necessary through the `decision` function. Finally, Lambda "pickles" the `trie` object and stores it in the S3 bucket. It returns the output message to REST API which then sends it to the client. 





