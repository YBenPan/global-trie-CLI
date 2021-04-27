set filename=%~n0
set output_file=%filename%.txt
call trie add --keyword=look > %output_file%
call trie add --keyword=small >> %output_file%
call trie add --keyword=smell >> %output_file%
call trie delete --keyword=sm >> %output_file%
call trie delete --keyword=small >> %output_file%
call trie print >> %output_file%
call trie delete --keyword=look >> %output_file%
call trie delete --keyword=smell >> %output_file%
pause