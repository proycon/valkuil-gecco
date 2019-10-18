import sys
from valkuilwebservice import valkuilwebservice
import clam.clamservice
application = clam.clamservice.run_wsgi(valkuilwebservice)
