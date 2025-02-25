echo "$(date)-initiating scrapping" >> log.txt
bash get_repo.sh
cd repo/src
python gopro_scrapper.py
python iphone_scrapper.py
echo "$(date)-finished scrapping" >> log.txt