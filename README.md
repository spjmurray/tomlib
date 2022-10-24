# Tomlib

It's fucking awesome!

## Installing

```bash
python3 -m venv venv
. venv/bin/activate

pip3 install -r requirements.txt
pip3 install .
```

## Testing

```bash
#!/usr/bin/env python3

from tomlib import PluribusAPI

if __name__ == '__main__':
    api = PluribusAPI('badger.mushroom.snake:8000', 'foo', 'bar')

    api.vlag.create('foo', 12345, 54321, mode='active-standby')
```
