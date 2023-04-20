# check if the database exists
if [ -f comicData.db ]; then
    echo "Database exists. Deleting..."
    rm -rf comicData.db
fi
sqlite3 comicData.db < schema.sql
sqlite3 comicData.db < startingData.sql