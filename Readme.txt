
Just run (double click on) thw batch file download_all_from_text_file.bat

it should in general work

If there is any break due to internet connection. you have to manually check till where files have been downloaded and delete everything before that from the list of urls in text file. This should be easy as everything is arranged in increasing order of day.



Technical detail:

wget.exe is gnu free utility to download any thing from web. It can take urls from a text file also and download.

command used here :

wget.exe --no-check-certificate -i url_list.txt

--no-check-certificate option because wget is not able to get the proper certificate for https.

url_list.txt file has all the urls you need to download


printAllLinks.py generate the txt file in proper format.

