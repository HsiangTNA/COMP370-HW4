(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ wc -l clean_dialog.csv
36860 clean_dialog.csv
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ ls -lh clean_dialog.csv
-rw-rw-r-- 1 ubuntu ubuntu 4.7M Oct 19  2019 clean_dialog.csv
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ tail -n +2 clean_dialog.csv | cut -d, -f1 | tr -d "" | sort | uniq | wc -l
196
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ Total=$($(wc -l < clean_dialog.csv)-1))
-bash: syntax error near unexpected token `)'
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ Total=$($(wc -l < clean_dialog.csv)-1)
36860-1: command not found
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ Total=$($(wc -l < clean_dialog.csv)-1) )
-bash: syntax error near unexpected token `)'
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ Total=$($(wc -l < clean_dialog.csv) -1 ))
-bash: syntax error near unexpected token `)'
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ Total=$($(wc -l < clean_dialog.csv ) -1 ))
-bash: syntax error near unexpected token `)'
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ Total=$($(wc -l < clean_dialog.csv ) -1)
36860: command not found
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ TOTAL=$(($(wc -l < clean_dialog.csv)-1))
echo "Total lines: $TOTAL"
Total lines: 36859
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ TS=$(grep -c '"Twilight Sparkle"' clean_dialog.csv)
echo "Twilight Sparkle: $TS"
Twilight Sparkle: 4749
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ RAR=$(grep -c '"Rarity"' clean_dialog.csv)
echo "Rarity: $RAR"
Rarity: 2660
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ PP=$(grep -c '"Pinkie Pie"' clean_dialog.csv)
echo "Pinkie Pie: $PP"
Pinkie Pie: 2833
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ RD=$(grep -c '"Rainbow Dash"' clean_dialog.csv)
echo "Rainbow Dash: $RD"
Rainbow Dash: 3073
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ FS=$(grep -c '"Fluttershy"' clean_dialog.csv)
echo "Fluttershy: $FS"
Fluttershy: 2109
(myenv) ubuntu@ip-172-31-19-217:~/COMP370-HW4/pony_data$ echo "scale=2; $TS/$TOTAL*100" | bc
echo "scale=2; $RAR/$TOTAL*100" | bc
echo "scale=2; $PP/$TOTAL*100" | bc
echo "scale=2; $RD/$TOTAL*100" | bc
echo "scale=2; $FS/$TOTAL*100" | bc
12.00
7.00
7.00
8.00
5.00