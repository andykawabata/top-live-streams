# Lofi Stream Ranking
Ranks Youtube Lofi Hip Hop streams by number of people currently watching
### Hosted at 
https://lofi-stream-ranking.herokuapp.com/

## Run locally

### Method 1:

Clone
```
$ git clone "https://github.com/hvrc/Lofi_Stream_Ranking_v1.git"
$ cd Lofi_Stream_Ranking_v1
```

Run the shell script on a Mac...
```
$ bash run.sh
```

...or run the batch file on Windows...
```
$ start run.bat
```
...and refresh the page

### Method 2:

Clone
```
$ git clone "https://github.com/hvrc/Lofi_Stream_Ranking_v1.git"
$ cd Lofi_Stream_Ranking_v1
```

Create a virtualenv & activate it
```
$ python3 -m venv venv
$ . venv/bin/activate
```

On Windows:
```
$ py -3 -m venv venv
$ . venv/Scripts/activate

```
On Windows cmd:
```
> py -3 -m venv venv
> venv\Scripts\activate.bat
```

Install requirements
```
$ pip install -r requirements.txt
```

Run
```
$ export FLASK_APP=toplofi
$ export FLASK_ENV=development
$ flask run
```

On Windows cmd:
```
> set FLASK_APP=toplofi
> set FLASK_ENV=development
> flask run
```

Open [localhost:5000](http://127.0.0.1:5000) in a browser
