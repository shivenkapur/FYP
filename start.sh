#!/bin/sh 
osascript <<END 
tell application "Terminal"
    do script "cd /Users/anujkapur/Documents/GitHub/FYP/WebCrawler;
    python3 main.py;
    exit"
end tell

tell application "Terminal"
    do script "cd /Users/anujkapur/Documents/GitHub/FYP/DocumentStorage;
    npm run dev;
    exit"
end tell

tell application "Terminal"
    do script "cd /Users/anujkapur/Documents/GitHub/FYP/KeywordExtraction;
    python3 start.py;
    exit"
end tell
END


