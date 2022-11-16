import logging
import sys

import __main__

# Silence shitty logs in repl
for lib in ("parso.python.diff", "parso.cache", "parso.cache.pickle"):
    logging.getLogger(lib).disabled = True

def _ptpython_configure(repl):
    from ptpython.repl import run_config

    path = _ptpython_conf_dir / "config.py"
    if path.exists():
        run_config(repl, path.as_posix())

# Here try to run ptpython if available 

try:
    from ptpython.repl import embed
except ImportError:
    pass
else:
    # if not run from ipython
    if "get_ipython" not in __main__.__dict__:
        new = embed(
            history_filename=_deduce_history_file().as_posix(),
            configure=_ptpython_configure,
            locals=__main__.__dict__,
            globals=globals(),
            title="Python REPL (ptpython)",
        )
        sys.exit(new)