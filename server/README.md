



### Setup

Install dependencies:
`pip install -r requirements.txt`

Run server:
`python server.py`

`upload.py` is a script that tests the server's upload functionality


### Description

* *Folders*:
  - `samples`: folder that will continue the samples we want to analyze
  - `uploads`: folder that will store the analysis results for each machine.
    + Each machine will have a folder that will contain analysis results in zip format
  - `test`: folder that will contain anything related to testing
* *Methods*:
  - Add and initialize the new machine in db
  - Download the next malware sample
  - Upload the malware analysis results

### API

| HTTP Method | URI                                   | Action                               |
|-------------|---------------------------------------|--------------------------------------|
| PUT/GET     | http://[hostname]/create/[string:machine_id] | Adds a new machine to the DB         |
| GET         | http://[hostname]/[string:machine_id] | Downloads the next sample to process |
| PUT/POST    | http://[hostname]/[string:machine_id] | Uploads the result of the analysis (only .zip)   |
