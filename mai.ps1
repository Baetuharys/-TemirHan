$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
python (Join-Path $Root "scripts/mai.py") @args
