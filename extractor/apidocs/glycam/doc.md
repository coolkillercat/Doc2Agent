# USAGE

## Overview
The JSON API provides an interface to the services made available by GEMS and GMML.

We make html requests to the API's urls, often providing json-formatted input. GEMS
then interprets requests, determines which service(s) are appropriate to provide,
and the api returns json-formatted responses.

A typical pattern might involve:
1. Evaluate some sequence to determine if it can be built, and if any options are
    available for that sequence.
2. Request that a 3D structure be generated for a sequence, possibly with options for which conformers (shapes) to generate.
3. Poll for the build status of either a default shape for the 3D structure, or of a specific conformer.
4. When the desired 3D structure file exists, request the file as an attachment in a response.

An in-depth walkthrough of one way this might happen is provided in the
[Appendix: Walkthrough](#walkthrough)

Note: Throughout this documentation, we refer to pUUID. The pUUID is just a hash we use for a project ID.
It is found in our json responses.

## Submitting requests to the API
The sample script we provide, [api-https.bash](api-https.bash), makes a curl request
for you, attaching the json input file that you indicate and submitting that to the
json api.

	`bash api-https.bash <json-input-file> <website-url>`

### Example:

	`bash api-https.bash build-sequence.json glycam.org`

(Note that variations like www.glycam.org do not work.)
### Sample input files
Our sample input files demonstrate the json input format for making requests to
services that GEMS provides:

* [marco.json](marco.json)
* [evaluate-sequence.json](evaluate-sequence.json)
* [build-sequence.json](build-sequence.json)

# Sequence Services
## Marco
[marco.json](marco.json) is for testing your ability to connect. If you receive a response that says
"polo", you have connected successfully.

## Evaluate
The Evaluate service returns json-formatted information about options that are available for a
requested structure. If you just want to know if we can build a sequence, this might
be the service you prefer. As of Jan 2024, Evaluate also creates and minimizes a default structure. If you do not require a 
specific conformer, you can skip the additional Build3DStructure request and move to the Polling or Download structure sections below.

## Build3DStructure
The Build3DStructure service returns very similar data, along with the information you need to poll for statuses
and download files. These requests can optionally define build options, if desired. If you only wish to retrieve 
the default 3D structure, you can ignore the build options. 
### Warning
As of Jan 2024, requesting a Build3DStructure without first running an Evaluate will cause problems. Until this is fixed and this warning removed, make sure you run Evaluate first.

Requests to build a PDB file generate responses with these features:
* A download url for a project. 
* IDs for each available conformer in that project.
* Information about options available for this structure.
* Values needed to poll the status of any files you plan to download.

### Sample output json:
* [Example-OUTPUT.marco.json.Response.json](Example-OUTPUT.marco.json.Response.json)
* [Example-OUTPUT.evaluate-sequence.Response.json](Example-OUTPUT.evaluate-sequence.Response.json)
* [Example-OUTPUT.build-sequence.json.Response.json](Example-OUTPUT.build-sequence.json.Response.json)
* [Example-OUTPUT.build-sequence-with-options.json](Example-OUTPUT.build-sequence-with-options.json)

## Using the output
Responses contain entities. Entities reflect the request (inputs), and provide
any responses (outputs):

### Inputs
```python
response['entity']['inputs']
```

### Outputs
```python
response['entity']['outputs']
```

### Evaluate service output
The evaluate response provides sequence evaluation, e.g. whether or not our
tools can build it (sequenceIsValid), sequence variants, buildOptions etc...

For a detailed example, see:
* [Example-OUTPUT.evaluate-sequence.Response.json](Example-OUTPUT.evaluate-sequence.Response.json)

### Build3DStructure service output
If you need to download a pdb file for a sequence, start with Build3DStructure.
The Build3DStructure service can be used both with and without build options
defined. In the case where no options are provided in the request, responses
will provide:
* a full evaluation,
* structureBuildInfo for accessing PDB files for specific conformations.

#### Build without setting options
The example json-formatted request in [build-sequence.json](build-sequence.json) does not set any options.
The example response in [Example-OUTPUT.build-sequence.json.Response.json](Example-OUTPUT.build-sequence.json.Response.json) 
includes the same evaluation data present in the evaluate request, but also provides downloadUrlPath values 
for downloading the structures available for that sequence.

For a detailed example of a build request with no user options, see:
* [build-sequence.json](build-sequence.json)
* [Example-OUTPUT.build-sequence.json.Response.json](Example-OUTPUT.build-sequence.json.Response.json)

#### Note about default structures
We do assign a default conformer for each sequence. There is nothing special about
the conformer we select to be the default, we just give one conformer a value of
isDefaultStructure : true in the response's individualBuildDetails.

This means:
* If you don't care which conformer you use, grabbing any is valid, it need not
be the default structure to be consistent, just continue using the same conformer ID.
* If you desire to specifically find the default structure, we provide a url that only requires that you
use the pUUID from a Build3DResponse in order to poll for a build status, and another to download it.


#### Build with options
One can set many options, and request up to 64 conformers (shapes) of a structure.
This involves:
1. Submitting an original request to retrieve the possible options
for your sequence, (as demonstrated, evaluate, or build requests suffice for this)
2. Submitting a second request, with options set, following the patterns in the
build response,
3. Polling the Build_Status url for the status of your builds,
4. Downloading some or all via the downloadUrl provided in the response.

For a detailed example of a build request with user options specified, see:
* [build-sequence-with-options.json](build-sequence-with-options.json)
* [Example-OUTPUT.build-sequence-with-options.json](Example-OUTPUT.build-sequence-with-options.json)

## Polling for the status of the default structure
All you need to check the status of the default structure is the pUUID returned in the response
to your Build3DStructure request. 
Using the following url:
```
https://glycam.org/json/project_status/sequence/<str:pUUID>/

```
We can receive a json object like the following:
```python
{
    "status": "All complete"
}

```
You might also see other statuses such as:
* minimizing
* submitted

## Polling for the status of a specific build
Given a pUUID and a conformer ID, we can check the status of a specific build.
Using the following url:
```
https://glycam.org/json/build_status/<str:pUUID>/<str:conformerID>/
```
We can receive a json object like the following:
```python
{
    "minExists" : True,
    "tip3pExists" : True,
    "tip5pExists" : False,
    "conformerID" : "1ogg",
    "status" : "2 of 3 complete"
}
```
The status field reflects the status of the overall work for a given conformer. These are the possible
statuses:
* queued
* minimizing
* 1 of 3 complete
* 2 of 3 complete
* All complete

Each file gives true or false to indicate whether it exists or not.

## Downloading Files
To retrieve your file(s), you can:

* Enter the downloadUrl into a browser window.
* Use curl in a scripting language.

Depending on whether you want the default structure, or a specific conformer, you will look for different
data in the response to your Build3DStructure request.

If you are looking for the default structure, the same pUUID that you used to poll for the project status
is all you need.

In the [Curl Example below](Curl_Example), you would edit [URL] to be:
```

https://glycam.org/json/download/sequence/cb/<pUUID>/
```
This downloads the minimized pdb file for the default structure.

To download a specific conformer, we provide a url in each individualBuildDetails object.

Look in the file containing [Example-OUTPUT.build-sequence-with-options.json](Example-OUTPUT.build-sequence-with-options.json). 
You will find a section like this:

```
{
    "structureBuildInfo": {
        "incomingSequence": "DManpa1-6DManpa1-OH",
        "indexOrderedSequence": "DManpa1-6DManpa1-OH",
        "seqID": "8f89c814-df0f-5867-a9d4-fc393bfea61b",
        "individualBuildDetails": [{
            "date": "2021-06-07T10:09:05.908645",
            "status": "new",
            "payload": "",
            "pUUID": "3c368bf2-ad73-43f3-a18d-d7d2dc11cf28",
            "entity_id": "sequence",
            "service_id": "cb",
            "incomingSequence": "",
            "indexOrderedSequence": "DManpa1-6DManpa1-OH",
            "seqID": "",
            "conformerID": "1ogg",
            "conformerLabel": "1ogg",
            "sequenceConformation": ["1", "o", "gg"],
            "isDefaultStructure": true,
            "isNewBuild": false,
            "structureDirectoryName": "1ogg",
            "filesystem_path": "/website/userdata/",
            "host_url_base_path": "https://glycam.org",
            "conformer_path": "/website/userdata/sequence/cb/Builds/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/Requested_Builds/1ogg",
            "absolute_conformer_path": "/website/userdata/sequence/cb/Builds/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/Existing_Builds/1ogg",
>>>>>>>>>>> "downloadUrlPath": "https://glycam.org/json/download/sequence/cb/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/1ogg/",
            "forceField": "See Build Directory Files"
        },
        ...  
```

The downloadUrlPath above is used in the following example.


### Curl Example
Curl submits requests to urls for you, and returns whatever response it receives from us. There are certain
circumstances beyond our control here. Specifically, you want to know that if you submit a poorly-formed 
json input file to curl, it returns raw html responses. It is best to validate your requests before submitting 
them to the api. This can be done in many languages. One way might include using Python: 
[Python doc for using json data.](https://docs.python.org/3/library/json.html)

#### Using curl on the command line

For detailed doc on how to use curl: 
[https://curl.se/docs/](https://curl.se/docs/)

To save a file with filename min-gas.pdb, set by the website, use:

`curl -L -o min-gas.pdb [URL]`

for example, to download a specific conformer:

`curl -L -o min-gas.pdb https://glycam.org/json/download/sequence/cb/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/1ogg/`

Do be certain that there is not already a file with the same name in your directory.


# Appendix

## Walkthrough
### Default Structure
*Key concept:* Default structure is a value we use to ensure we always show the same
file when no specific conformer is needed. If don't require a specific conformer, 
you can simply be concerned with finding the pUUID in a Build3DStructure response.


1. Create a folder to work in somewhere. We will use this, for example:
`
 test/
`
2. Create a new file. You can name it what you like. It will be the command we run to
start our process. We will use this, for example:
`
testTheAPI.sh.
`
3. Copy the contents of this [api-https.bash](api-https.bash) script into your test script. If you run the script with no arguments, you will get a helpful usage message.

> The script you just created accepts an argument for JSON input, and a host. We have
sample json files that demonstrate the format needed for for requests. Feel free
to use these and edit the input as needed.

> We will demonstrate using [build-sequence.json](build-sequence.json),
which requests DManpa1-6DManpa1-OH. You can simply edit the sequence contained in 
this file and it can be used as input to request the default structure for any valid 
sequence.

4. In the same folder as your test script, create a new file to contain the json
input. We will use [build-sequence.json](build-sequence.json).

5. Copy the contents of [build-sequence.json](build-sequence.json) into your new
file. Because the script and its input are in the same path in our example, we
just use the filename with no path. If you need to add paths, and if you use
different file names, remember to edit the following to reflect your needs. Run
the following command to submit your request:
```bash
$ bash testTheAPI.sh build-sequence.json glycam.org
```
> You can expect some chatty logs on your console, followed by a printout
of your response object. This is also written to file, by the test script we just
called in the command above. You can edit that if you want different filenames or
output locations.
There is a lot of data in the output. These responses serve more purposes than ours, 
but we are only interested in one piece of data:
* pUUID - A key to find the project that your request created. Needed for
    polling file status.

For example:
```python
pUUID = responseDict['project']['pUUID']
```

6. Poll for the status of the default structure's project files.

An example curl request for checking the build status of the default structure is here:
[checkDefaultStatus.sh](#checkDefaultStatus.sh)

A request made to
```
http://glycam.org/json/project_status/sequence/<str:pUUID>/

```

Receives a response with a json object like the following:
```python
{
    "status": "All complete"
}

```
You might also see other statuses such as:
* minimizing
* submitted

You want to be sure the status is "All complete" in order to ensure your pdb file
represents a minimized molecule.

7. Download the default structure (Or any structure you choose.)
Just as the checkStatus script is simply a curl request sent to the appropriate url,
downloads are the same. We can make curl requests, or place the download url in
a browser, etc...

The downloadUrlPath for the conformer you need is provided in responses to
Build3DStructure requests. If you desire the default structure, use the ID of the
individualBuildDetails object who's isDefaultStructure field is true.

Several curl examples have been provided so far. The only new thing here is the
content of the url.

A request made to
```
https://glycam.org/json/download/sequence/cb/<pUUID>/
```
will return a minimized PDB file for that structure if it exists. The values in
responses' downloadUrlPath all follow this pattern, and may be all you need.



#### Specific Conformers:
If you need a specific conformer, you can use the project ID and conformer ID to 
poll for the build status. 

Using the following url:
```
http://glycam.org/json/build_status/<str:pUUID>/<str:conformerID>/
```
We can receive a json object like the following:
```python
{
    "minExists" : True,
    "tip3pExists" : True,
    "tip5pExists" : False,
    "conformerID" : "1ogg",
    "status" : "2 of 3 complete"
}
```

Each conformer also knows its downloadUrlPath, which can be used to retrieve the
minimized pdb for that conformer.

Regardless of whether you are looking for the default structure, or have less
specific needs, examining the output of a build response shows structureBuildInfo
which contains a list of individual build details. Here, the reasonable values for
conformerIDs can be found, as well as a boolean to determine the default structure.


```"structureBuildInfo": {
    "incomingSequence": "DManpa1-6DManpa1-OH",
    "indexOrderedSequence": "DManpa1-6DManpa1-OH",
    "seqID": "8f89c814-df0f-5867-a9d4-fc393bfea61b",
    "individualBuildDetails": [{
        "date": "2021-06-07T10:09:05.908645",
        "status": "new",
        "payload": "",
        "pUUID": "3c368bf2-ad73-43f3-a18d-d7d2dc11cf28",
        "entity_id": "sequence",
        "service_id": "cb",
        "incomingSequence": "",
        "indexOrderedSequence": "DManpa1-6DManpa1-OH",
        "seqID": "",
>>>>>>>>"conformerID": "1ogg",
        "conformerLabel": "1ogg",
        "sequenceConformation": ["1", "o", "gg"],
>>>>>>>>"isDefaultStructure": true,
        "isNewBuild": false,
        "structureDirectoryName": "1ogg",
        "filesystem_path": "/website/userdata/",
        "host_url_base_path": "https://glycam.org",
        "conformer_path": "/website/userdata/sequence/cb/Builds/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/Requested_Builds/1ogg",
        "absolute_conformer_path": "/website/userdata/sequence/cb/Builds/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/Existing_Builds/1ogg",
>>>>>>>>"downloadUrlPath": "https://glycam.org/json/download/sequence/cb/3c368bf2-ad73-43f3-a18d-d7d2dc11cf28/1ogg/",
        "forceField": "See Build Directory Files"
    },
```
The above snippet shows how responses offer conformerIDs, downloadUrlPath,
and pUUID, each indicated by '>>>>>>>>'.

We provide a sample script that you can use to poll for the status of the
file you requested. Create a new file. We will use this, for example:
`
checkStatus.sh
`
1. Copy the content of [checkStatus.sh](checkStatus.sh) into your new script.
2. In the response to your original request, find the pUUID for your project, and
grab an appropriate conformerID. (Remember any are valid, but only default has
'isDefaultStructure' : true)
3. Run the script with your selected args. The example script will echo out the status
response, and also writes it out to file.
```bash
$ bash checkStatus.sh <pUUID> <conformerID>
```
Our example would be:
```bash
$ bash checkStatus.sh a997768f-6097-4aa6-9789-c756252358df 1ogg
```
4. Examine the response to find the status. This example status response
indicates that all files are complete. If you need verification that it has
been minimized, 'minExists' will only return true when minimization is finished.
#### Example Status Response
```
{
    "minExists": true,
    "tip3pExists": true,
    "tip5pExists": true,
    "conformerID": "1ogg",
    "status": "All complete"
}
```

5. The downloadUrlPath shown in the response above is all you need to download a pdb for your conformer. 
Do wait until the status response is "All complete" for your structure.