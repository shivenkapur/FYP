#!/bin/sh 
osascript <<END 
tell application "Terminal"
    do script "cd /Users/vanshajchadha/Desktop/'my code'/WebCrawler;
    python3 main.py;
    exit"
end tell

tell application "Terminal"
    do script "cd /Users/vanshajchadha/Desktop/'my code'/DocumentStorage;
    npm run dev;
    exit"
end tell

tell application "Terminal"
    do script "cd /Users/vanshajchadha/Desktop/'my code'/Cluster;
    npm run dev;
    exit"
end tell

tell application "Terminal"
    do script "cd /Users/vanshajchadha/Desktop/'my code'/KeywordExtraction;
    python3 start.py;
    exit"
end tell
END


