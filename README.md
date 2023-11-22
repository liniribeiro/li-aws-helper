# lini-cli
Command line project to facilitate lini's life

## Package Usage for aws commands
- First we must configure your aws credentials:
```bash
li config
```

Then use as commandline to refresh your 2f auth with aws. 
```bash
li refresh --token xxxxxx
```

Install
```
pip3 install -r li-aws-helper
```


## Local Development

- Build the project: `poetry build`
- Install the project: `poetry install`
- install twine: `python3 -m pip install --upgrade twine`


FAQ
- What is a arn?
- Where I can find my AWS key and secret?


