set filename=%~n0
set output_file=%filename%.txt
call trie add --keyword=threea > %output_file%
call trie add --keyword=threeb >> %output_file%
call trie add --keyword=threec >> %output_file%
call trie add --keyword=threed >> %output_file%
call trie add --keyword=threee >> %output_file%
call trie print >> %output_file%
call trie delete --keyword=threea > %output_file%
call trie delete --keyword=threeb >> %output_file%
call trie delete --keyword=threec >> %output_file%
call trie delete --keyword=threed >> %output_file%
call trie delete --keyword=threee >> %output_file%
