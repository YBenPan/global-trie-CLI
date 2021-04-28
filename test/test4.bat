set filename=%~n0
set output_file=%filename%.txt
call trie add --keyword=foura > %output_file%
call trie add --keyword=fourb >> %output_file%
call trie add --keyword=fourc >> %output_file%
call trie add --keyword=fourd >> %output_file%
call trie add --keyword=foure >> %output_file%
call trie print >> %output_file%
call trie delete --keyword=foura > %output_file%
call trie delete --keyword=fourb >> %output_file%
call trie delete --keyword=fourc >> %output_file%
call trie delete --keyword=fourd >> %output_file%
call trie delete --keyword=foure >> %output_file%
