## Simple config

Philosophy: Use python files to manage your config.

At the root level, add a config.py file, all the variables in it (functions too) will be available anywhere
in your project through the cnfgr module.

Private variables can be placed in private_config.py (create this file at the root leve ltoo). This file is inteded to never be committed.

Variables can also be injected into the environment and used from there. To add an env variable for cnfgr, use the format:

`CNFGR__KEY="value1"`
`CNFGR__NESTED__KEY="value2"`

## Precedence

Precedence: private_config.py > environment variables > config.py

In config.py:

```
private_key1: 'xxxxx'
private_key2: { "nested_key": "xxxxx" }
private_key3: 'xxxxx'

```

Set your environment variables:

```
CNFGR__PRIVATE_KEY2__NESTED_KEY: 'yyyyy'
CNFGR__PRIVATE_KEY3: 'yyyyy'
```

private_config.py

```
private_key3: 'zzzzz'
```

Will result in a cnfgr object of:
{
private_key1: 'xxxxx',
private_key2: { "nested_key": "yyyyy"},
private_key3: 'zzzzz',
}

## Usage

```
import cnfgr
# your app code

pvt_key1 = cfngr.get('private_key') # pvt_key = 'xxxxx'
pvt_key2 = cfngr.get('private_key2')['nested_key'] # pvt_key2 = 'yyyyy'

```
