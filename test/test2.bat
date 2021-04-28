set filename=%~n0
set output_file=%filename%.txt
call trie add --keyword=one > %output_file%
call trie add --keyword=two >> %output_file%
call trie search --keyword=two >> %output_file%
call trie add --keyword=three >> %output_file%
call trie delete --keyword=three >> %output_file%
call trie search --keyword=three >> %output_file%
call trie add --keyword=four >> %output_file%
call trie add --keyword=five >> %output_file%
call trie print >> %output_file%
call trie delete --keyword=one >> %output_file%
call trie delete --keyword=two >> %output_file%
call trie delete --keyword=four >> %output_file%
call trie delete --keyword=five >> %output_file%
call FC test2.txt test2_ans.txt
pause