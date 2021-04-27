import json
import boto3
import botocore
import pickle

s3_resource = boto3.resource('s3')


class TrieNode:

    def __init__(self, char):
        self.char = char
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode("ROOT")

    def add(self, keyword):
        node = self.root
        for char in keyword:

            if char in node.children:  # found
                node = node.children[char]

            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

    def remove(self, node, keyword):

        if not node.children:  # We have reached the end of the word
            return 1
        if keyword == '': 
            return 2
        char = keyword[0]
        keyword = keyword[1:]
        if char not in node.children:  # We did not find the word
            return 2    # Error Code

        # the function returns True if the child is to be removed
        res = self.remove(node.children[char], keyword)
        if res == 2:    # Return error code
            return 2
        if res == 0:  # We did not delete the child node, so we will not delete current node either
            return 0
        del node.children[char]
        if not node.children:  # After deletion, the current node is a leaf. Mark it for removal
            return 1
        return 0

    def search(self, keyword):
        node = self.root
        for i in range(len(keyword)):
            char = keyword[i]
            if char in node.children:
                node = node.children[char]
            else:
                return False
            if (i == len(keyword) - 1) and node.children:   # If we iterated through keyword and there are still children, then our keyword is a prefix. Invalid
                return False
        return True

    def autocomplete_helper(self, cur_string, node):  # DFS starting at prefix node
        cur_string += node.char
        ans = []
        if not node.children:
            ans.append(cur_string)
        for child in node.children.values():
            ans += self.autocomplete_helper(cur_string, child)
        return ans

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return 'Prefix not found!'
        prefix = prefix[:-1]  # Prevent adding extra characters
        return self.autocomplete_helper(prefix, node)

    def print_trie(self, node, keyword_prefix="", print_prefix=""):
        next_print_prefix = print_prefix + '  '
        ans = ""
        for child in node.children:
            output_str = print_prefix + '+-' + keyword_prefix + child + '\n'
            print(output_str)
            ans = ans + output_str
            child_node = node.children[child]
            ans += self.print_trie(child_node, keyword_prefix + child, next_print_prefix)
        return ans


def decision(event_type, keyword, trie_obj):
    # print(event_type, keyword)
    json_return = ''
    if event_type == 'add':
        trie_obj.add(keyword)
        json_return = 'Addition Successful!'
    elif event_type == 'delete':
        result = trie_obj.remove(trie_obj.root, keyword)
        if result == 2:
            json_return  = 'ERROR: Keyword not found!'
        else:
            json_return  = 'Deletion Successful!'
    elif event_type == 'search':
        result = trie_obj.search(keyword)
        if result:
            json_return = 'True'
        else:
            json_return = 'False'
    elif event_type == 'autocomplete':
        result = trie_obj.autocomplete(keyword)
        json_return = result
    elif event_type == 'print':
        result = trie_obj.print_trie(trie_obj.root)
        json_return = result
    return json_return


def lambda_handler(event, context):
    # Get parameters
    event_type = event['type']
    keyword = event['keyword']

    # Bucket names in S3
    bucket = 'trie-storage'
    file_name = 'tries.pickle'

    # Download from S3
    s3client = boto3.client('s3')
    try:
        s3_resource.Object(bucket, file_name).load()
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            print('INITIALIZING TRIE')
            trie_obj = Trie()
    else:
        download_file = s3client.get_object(Bucket=bucket, Key=file_name)
        content = download_file['Body']
        trie_obj = pickle.loads(content.read())
        print('DOWNLOAD SUCCESSFUL')

    json_return = decision(event_type, keyword, trie_obj)

    # Upload
    pickle_obj = pickle.dumps(trie_obj)
    s3_resource.Object(bucket, file_name).put(Body=pickle_obj)
    print('UPLOAD SUCCESSFUL')
    
    return {
        'statusCode': 200,
        'body': json_return
    }
