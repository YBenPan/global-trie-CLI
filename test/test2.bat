set filename=%~n0
set output_file=%filename%.txt
call trie add --keyword=freq > %output_file%
call trie print > %output_file%