import axios from 'axios';
import chalk from 'chalk';

const api_str = 'https://cjql8lovja.execute-api.us-east-2.amazonaws.com/trie_stage/lambda'

const getSearch = (args) => {
    let arg_str = api_str + '?type=search&keyword=' + args['keyword']
    axios
        .get(arg_str)
        .then(function (response) {
            let tmp = response['data']['body']
            console.log(tmp)
        })
        .catch(error => console.log(error['response']['data']['message'])); 
}

export async function search(args) {
    getSearch(args);
}