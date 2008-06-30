import urllib2 as u2

import urllib2_kerberos as u2k

def reposetup(ui, repo):
    if u2._opener is not None:
        u2._opener.add_handler(u2k.HTTPKerberosAuthHandler())
