import sys
sys.path.append("/home/proycon/work/valkuil-gecco/valkuilwebservice")
import valkuilwebservice
import clam.clamservice
application = clam.clamservice.run_wsgi(valkuilwebservice)