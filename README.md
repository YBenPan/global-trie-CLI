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

## Room for Improvement
I did not have time to implement the following features, but here are my ideas: 
1. Use a queue to process inputs from different clients. Amazon has a feature called Simple Queue Service. We can connect the API Gateway to a SQS First-In-First-Out queue and then from SQS to Lambda. By doing this, we make sure Lambda only processes one request at a time and maintain the integrity of the order of requests.  
2. To optimize the autocomplete feature and make it more realistic, we can keep a hash table in each node that stores the ten most "popular" children. Popularity is determined by the number of times the word has been added. To obtain a list of autocomplete suggestions, we can simply output the contents of the hashtable. 
3. We can group a client's requests together and send them to Lambda together. This reduces the number of times we invoke the Lambda function, thus saving time. 




