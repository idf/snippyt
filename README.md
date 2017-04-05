# snippyt {:ledger:}
A command line snippet management for modern developers.

# Usage
```bash
Usage:
  snip <snippet>
  snip <snippet> -c <context>

Examples:
  snip helloworld -c "name=World;"
```

# Install
##
```bash
pip3 install snippyt
```
## Manual
```bash
git clone https://github.com/idf/snippyt.git
cd snippyt
sudo python setup.py install
```

# Add more snippets
The default path where snippets go is `~/.snippyt`. For example:
```
mkdir ~/.snippyt
echo "{{ firstname }} {{ lastname }}'s own snippet" > ~/.snippyt/sample
snip sample -c "firstname=John;lastname=Tenniel"
# John Tenniel's own snippet
```

# Features
* Basic plain text snippet
* kwargs in CLI
* Show for missing entries

# Development
* Python 3.6
```
pip install -r requirements.txt
```
