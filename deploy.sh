#!/bin/sh
# echo "> Building HTML by mddocs..."
# mkdocs build
echo "> Update mac-soft"
cd ./docs/soft/mac-soft && git pull
echo "> Gen mkdocs config"
cd ../../../
pipenv run python main.py
echo "> Push code to git"
read -p "> Please input commit info: " commit_info
git add *
git commit -m "$commit_info"
git push
echo "> Push code to gh-deploy"
mkdocs gh-deploy --clean
echo "> Done!"
