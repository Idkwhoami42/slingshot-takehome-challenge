
# Slingshot Take Home Challenge

A Trie system that is hosted online with a global state that supports multiple concurrent clients.
Note: my digital ocean expired, so you will have to run it locally



## Deployment on server

- First clone the project
- To run on localhost, in `server/main.py` change
    ```python
    if __name__ == '__main__':    
        app.run("0.0.0.0")
    ```
    to
    ```python
    if __name__ == '__main__':    
        app.run()
    ```

### Deployment
#### Windows
```bash
    cd server
    pip install -r requirements.txt
    python main.py
```
#### Linux/MacOS
```bash
    cd server
    pip install -r requirements.txt
    python3 main.py
```

#### Note
Server is running at the time of submission on digital ocean.

  
## Command Line Tool usage

- in `cli/api.py` change 
    ```python
    serverip = '139.59.46.128:5000'
    ```
    according to your server ip (`localhost:5000`, if running locally)
- On starting, there is a default trie with `name = default` and `password = slingshot`
- However you can create new tries
- run the following command to start 
    #### Windows
    ```bash
    cd cli
    pip install -r requirements.txt
    python cli.py
    ```

    #### Linux/MacOS
    ```bash
    cd cli
    pip install -r requirements.txt
    python3 cli.py
    ```

### Commands

- **insert:** insert a new keyword
- **delete:** delete a keyword from trie
- **delete all:** deletes all keywords from the trie
- **search:** search whether the given keyword is in the trie or not
- **prefix:** list of keywords starting with prefix
- **keywords:** returns all keywords in the trie


## Documentation

### Server Side
- Hosted on Digital Ocean
- A global trie is running
- With the help of flask, CLI tool connects to the server via REST API
- APIs can be found in `CLI/api.py`
- You can test the APIs with postman


## Command Line Side
- PyInquirer is used for the CLI inteferance
- With the help of RESTful API, it interacts with global trie
  
## Tools/Resources Used

- VPS: Digital Ocean
- Made with python and flask
- Command line tool made with the help of [PyInquirer](https://github.com/CITGuru/PyInquirer)
- Stackoverflow for errors
  
## Screenshots

[Demo](https://imgur.com/a/cGcCf3c)


  
