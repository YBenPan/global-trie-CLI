import chalk from 'chalk';

const menus = {
    main: `
${chalk.redBright('trie [command] <options>')}

    ${chalk.blueBright('add')} ............... add a keyword to trie
    ${chalk.blueBright('delete')} ............... delete a keyword from trie
    ${chalk.blueBright('search')} ............ search for a keyword in trie (returns True/False)
    ${chalk.blueBright('autocomplete')} ...... return list of autocomplete suggestion based on an input prefix
    ${chalk.blueBright('print')} ............. display the trie

Option: 
    --keyword ......... specify keyword
    `
}

export async function help(args) {
    const subCommand = args._[0] === 'help' ? args._[1] : args._[0]
    console.log(menus[subCommand] || menus.main)
}