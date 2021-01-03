#!/usr/bin/python3
import os
from git import Repo


from test.lib import TestBase
from test.lib.helper import with_rw_directory

import os.path


bare_repo = Repo.init(os.path.join(rw_dir, 'bare-repo'), bare=True)
assert bare_repo.bare
print("info: bare-repo crée")