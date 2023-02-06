# LogUnredactor
### Python Script and a Web Page to un-redact a log file based on a json file. 
The Web app is compiled with flask, it will prompt for redacted log-file and json key file to un-redact it

On a side-note I am a novice with coding and this has been my first python project written with the help of Chat-GPT. 

## Python Script

The Python Script (LogUnredactor.sh) can be run on any unix as a bash script 
it needs python3 and json libraries

```
 $ ./Unredactor.sh > Unredacted_log.txt
Enter the log file path: current_log.txt 
Enter the redaction mapping file path: test.json
```

## Webepage. 
app.py is in flask as long as you have python and flask preoperly configured you will be able to run it 

## Docker Image 
If you are not really bothered with compiling and setting up a web server you can just run the docker container.
https://hub.docker.com/r/vinstech/logunredactor

```
docker pull vinstech/logunredactor
docker run -d -p 8484:5000 vinstech/logunredactor
```
Access the page at http://ip-address:8484

