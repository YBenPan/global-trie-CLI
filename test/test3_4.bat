:: Run this script to test for global state
:: If both test scripts yield the same tree, then there is a global state. 

start test3.bat
start test4.bat

timeout /t 20
call FC test3.txt test4.txt
pause
