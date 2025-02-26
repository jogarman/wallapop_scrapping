# 0226 parece que funciona

log_loc="C:/Users/Administrator/Desktop/log.txt"

src_loc="C:/Users/Administrator/Desktop/repo/src/"
get_repo_loc="C:/Users/Administrator/Desktop/repo/crear_la_imagen/get_repo.sh"


echo "$(date): initiating instance" >> "$log_loc"
bash "$get_repo.sh"

echo "$(date): init gopro_scrapper" >> "$log_loc"
python "$(src_loc)gopro_scrapper.py"
echo "$(date): end gopro_scrapper" >> "$log_loc"

echo "$(date): init iphone_scrapper" >> "$log_loc"
python "$(src_loc)iphone_scrapper.py"
echo "$(date): end iphone_scrapper" >> "$log_loc"

echo "$(date): finishing instance" >> "$log_loc"