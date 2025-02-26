sleep 1

desktop_loc = "C:\Users\Administrator\Desktop\"
get_repo_loc = "C:\Users\Administrator\Desktop\repo\crear_la_imagen\get_repo.sh"
src_loc = "C:\Users\Administrator\Desktop\repo\src\"

echo "$(date): initiating scrapping" >> "$(desktop_loc)log.txt"
bash "$(get_repo_loc)"

python "$(src_loc)gopro_scrapper.py"
echo "$(date): end gopro_scrapper" >> "$(desktop_loc)log.txt"
python "$(src_loc)iphone_scrapper.py"
cd ../..
echo "$(date): end iphone_scrapper" >> "$(desktop_loc)log.txt"


echo "$(date): closing instance" >> "$(desktop_loc)log.txt"