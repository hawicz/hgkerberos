import urllib2_kerberos as u2k

import mercurial.url

def reposetup(ui, repo):

    mercurial.url.opener_ = mercurial.url.opener

    def opener(*args, **kwargs):
        urlopener = mercurial.url.opener_(*args, **kwargs)
        urlopener.add_handler(u2k.HTTPKerberosAuthHandler())
        return urlopener

    mercurial.url.opener = opener
