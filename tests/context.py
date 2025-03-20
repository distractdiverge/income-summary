import os
import sys
# Path Modification to allow tests access to the source module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import income_summarizer