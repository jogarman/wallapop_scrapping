REPO_ADDRES="https://github.com/jogarman/wallapop_scrapping.git"
TARGET_DIR="repo"

if [ -d "$TARGET_DIR" ]; then
    cd "$TARGET_DIR"
    git fetch
    if [ $(git status | grep -c 'behind') -ne 0 ]; then
        echo "pulling repository"
        git pull
    else
        echo "Repository up to date"
    fi
else
    echo "TARGET_DIR does not exist. Cloning repo..."
    git clone "$REPO_ADDRES" "$TARGET_DIR"
fi