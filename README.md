# example-api-101
An example of API between Python back-end and JS front-end

## How to set up?

There is a usual venv. The instructions below should work fine if you get no errors when open your terminal and type `python3` there. Also I assume that you have Python 3.11+ installed and the command `python` in your terminal in the cloned repo directory refers to it.

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

Now just start a server:

```shell
$ python manage.py runserver
```

Open the link in your browser: [localhost:8000](http://localhost:8000).

Enjoy!


### VSCode set up

You can use VSCode to develop. However you need first to create venv (see above). If venv is set up, just open a folder in the VSCode and it will do the rest.

Venv is activated by default in the VSCode's terminals.

### Taskfile

There is a Taskfile.yml with different useful commands.

**Note**: They all require activated venv.

Refer to [Taskfile.dev docs](https://taskfile.dev/usage/) to understand the syntax and how to use.
Apparently you can just read the YAML syntax of the config and extract commands by hand.
