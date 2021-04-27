import minimist from 'minimist';
import chalk from 'chalk';
import { help } from './help';
import { add } from './add'; 
import { del } from './del';
import { search } from './search';
import { autocomplete } from './autocomplete';
import { print_trie } from './print_trie';
import { init } from './init';

// This function checks if the "keyword" option is missing. 
const validate = (argsObj, cmd) => {    
    if (cmd == 'print' || cmd == 'help') return false;
    if (!('keyword' in argsObj)) {
        console.error(`\nMissing keyword. Please use \n"trie ${cmd} --keyword=${chalk.blueBright('keyword')}"\n`);
        return true;
    }
    return false;
}

export async function cli(args) {
    const argsObj = minimist(args.slice(2));    // minimist parses the argument
    let cmd = argsObj._[0] || 'help'; 
    let res = validate(argsObj, cmd); 
    if (res == true) return; 
    switch (cmd) {

        case 'add': 
            add(argsObj);
            break;

        case 'delete': 
            del(argsObj);
            break;

        case 'help': 
            help(argsObj); 
            break;

        case 'search': 
            search(argsObj);
            break;
        
        case 'autocomplete': 
            autocomplete(argsObj);
            break;

        case 'print': 
            print_trie(argsObj); 
            break;

        case 'init': 
            init(argsObj); 
            break;
        
        default: 
            console.error(`"${cmd}" is not a command! Use ${chalk.blueBright('trie help')} to see a list of commands`)
    }
}