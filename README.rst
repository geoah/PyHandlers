Python Handlers
===============

Description
-----------

Creates a demo HTTP server to create and manage payloads. Each payload is a process to be executed on the server. 

A new payload is created with a POST request to the /payloads web app, a uuid is generated and returned so it can be used to identify the process.

A GET request to the /payloads request will return a list of all payloads. A GET request to /payloads/uuid will return information on a specific payload.

All payloads are stored in memory and thus are not persistent.


Installation
------------

Create And Activate A Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ virtualenv ~/ve/pericles
    $ source ~/ve/pericles/bin/activate


Install Dependencies
~~~~~~~~~~~~~~~~~~~~
::

    pip install -r requirements.txt

Install
~~~~~~~
::

    pip install -e .

    
Run Web-Platform for Development/Demo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    handler-serve


Usage
-----

Create payload - POST /payloads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* sample request:

::

    curl -X POST -d '{ "cmd": "/bin/sleep", "params": ["30"] }' http://localhost:8000/payloads

* response:

::

    {
        "status": "pending",
        "cmd": "/bin/sleep",
        "params": [
            "30"
        ],
        "id": "0d111286d6fb4f7ebd7464082bada101"
    }

* sample request:

::

    curl -X POST -d '{ "cmd": "/bin/ping", "params": ["-c", "5", "google.com"] }' http://localhost:8000/payloads

* response:

::

    {
        "status": "pending",
        "cmd": "/bin/ping",
        "params": [
            "-c",
            "5",
            "google.com"
        ],
        "id": "b51547fe3ff7409cb75f4ab13f764d8e"
    }


Get all payloads - GET /payloads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* sample request:

::

    curl -X GET http://localhost:8000/payloads

* response:

::

    [
        {
            "status": "error:start('/sbin/ping':No such file or directory",
            "cmd": "/sbin/ping",
            "params": [
                "-c",
                "5",
                "google.com"
            ],
            "id": "9b771f621eef49e696eb75cadfc0537b"
        },
        {
            "status": "finished",
            "cmd": "/bin/sleep",
            "params": [
                "30"
            ],
            "id": "0d111286d6fb4f7ebd7464082bada101"
        },        
        {
            "status": "working",
            "cmd": "/bin/ping",
            "params": [
                "-c",
                "5",
                "google.com"
            ],
            "id": "e92f4a7546af45f49f27f07588ecb2b5"
        },
    
    
    ]

Get a specific payload - GET /payloads/uuid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* sample request:

::

    curl -X GET http://localhost:8000/payloads/e92f4a7546af45f49f27f07588ecb2b5

* response:

::

    {
        "status": "finished",
        "cmd": "/bin/ping",
        "params": [
            "-c",
            "5",
            "google.com"
        ],
        "id": "e92f4a7546af45f49f27f07588ecb2b5"
    }

