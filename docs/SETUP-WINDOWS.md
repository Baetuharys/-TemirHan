# Windows Setup (SolidWorks users)

## Minimum
Install Python 3.11+ and make sure `python --version` works in PowerShell/CMD.

From the repository folder:
```powershell
.\mai.ps1 validate
.\mai.ps1 search "IP65 gasket"
.\mai.ps1 calc bend --t 2 --r 2 --angle 90 --k 0.40
```
Or CMD:
```bat
mai.bat validate
```

## Optional Image→CAD dependencies
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r engines\image_to_cad\requirements.txt
.\mai.ps1 image-cad path\to\image.png --out output
```

## SolidWorks macros
VBA examples are reference scaffolds. Verify API calls against the API Help of **your installed SolidWorks version**, save the CAD file first, and test on a copy. The repository does not execute SolidWorks itself during CI.
