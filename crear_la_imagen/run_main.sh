#!/bin/bash
# Definir rutas
# Los programas de python deben ejecutarse con el pwd en src, en la misma direccion que el programa
# FUNCIONA! 0227

python_log_stdout="C:/Users/Administrator/Desktop/python_log_stdout.txt"
python_log_stderr="C:/Users/Administrator/Desktop/python_log_stderr.txt"
main_log_loc="C:/Users/Administrator/Desktop/main_log.txt"

get_repo_loc="C:/Users/Administrator/Desktop/get_repo.sh"
src_loc="C:/Users/Administrator/Desktop/repo/src"


echo "$(date): init   instance" >> "$main_log_loc"
bash "$get_repo_loc"

echo "$(date): init   gopro_scrapper" >> "$python_log_stdout" 
echo "$(date): init   gopro_scrapper" >> "$python_log_stderr" 
cd "$src_loc" # muy importante!
python "$src_loc/gopro_scrapper.py" >> "$python_log_stdout" 2>> "$python_log_stderr"
echo "$(date): end    gopro_scrapper" >> "$main_log_loc"


echo "$(date): init   iphone_scrapper" >> "$python_log_stdout"
echo "$(date): init   iphone_scrapper" >> "$python_log_stderr" 
python "$src_loc/iphone_scrapper.py" >> "$python_log_stdout" 2>> "$python_log_stderr"

echo "$(date): end    iphone_scrapper" >> "$main_log_loc"
echo "$(date): finish instance" >> "$main_log_loc"
