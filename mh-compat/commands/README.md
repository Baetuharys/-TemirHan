# MergenHan-inspired command set — implemented

The repository preserves MergenHan's idea → module/master → blueprint → skill → adapter lifecycle, while adding engineering execution commands.

## One entry point

```bash
python scripts/mai.py validate
python scripts/mai.py search "IP65 gasket door overlap"
python scripts/mai.py calc bend --t 2 --r 2 --angle 90 --k 0.40
python scripts/mai.py image-cad reference.png --out out --ref-p1 10 20 --ref-p2 410 20 --ref-mm 200
python scripts/mai.py new-prompt module my-module --category capability
python scripts/mai.py rebuild
```

## Content-maintenance mapping
- `new-prompt master <slug>` → orchestrated master prompt
- `new-prompt module <slug> --category ...` → reusable behavior/domain fragment
- `new-prompt blueprint <slug>` → stabilized skill draft
- package into `skills/<slug>/` when contracts/tests are clear
- provider-specific execution belongs under `adapters/`

The command names above are this repository's compatibility layer; they do not claim to be a byte-for-byte copy of upstream MergenHan commands.
