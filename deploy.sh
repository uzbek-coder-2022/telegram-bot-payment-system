#!/bin/bash

# Loyihaning joylashgan papkasiga o'tish
cd /home/user/aiogram-bot

# Virtual environment yaratish yoki yangilash
python3 -m venv venv

# Virtual environmentni faollashtirish
source venv/bin/activate

# Yangi paketlarni o'rnatish
pip install -r requirements.txt

# Log fayllarni yaratib olish
touch logfile.log
touch logfile_err.log

# .conf faylini joylashtirish
sudo cp bot.conf /etc/supervisor/conf.d/bot.conf

# Supervisorctl konfiguratsiyasini yangilash
sudo supervisorctl reread
sudo supervisorctl update

# Dasturni qayta ishga tushirish
sudo supervisorctl stop bot_nomi
sudo supervisorctl start bot_nomi
