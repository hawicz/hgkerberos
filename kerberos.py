####################################################################
# Copyright (c) 2008 Lime Labs LLC
# Copyright (c) 2023 Eric Hawicz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
# limitations under the License.
#
####################################################################

"""
To install this extension (mostly rootless), do:

    sudo apt-get install python3-kerberos  # Debian only, installs Kerberos libs too
    pip3 install --user urllib_kerberos    # no Debian package (yet?)
    mkdir -p ~/.hgext
    cp kerberos.py ~/.hgext/.

    # Update your .hgrc config:
    grep -q '^kerberos=' ~/.hgrc || sed -i -e"/\[extensions\]/a\
kerberos=${HOME}/.hgext/kerberos.py" ~/.hgrc

"""

# See https://github.com/willthames/urllib_kerberos
# aka https://pypi.org/project/urllib_kerberos
import urllib_kerberos as u2k

import mercurial.url

def uisetup(ui):

    mercurial.url.opener_ = mercurial.url.opener

    def opener(*args, **kwargs):
        urlopener = mercurial.url.opener_(*args, **kwargs)
        urlopener.add_handler(u2k.HTTPKerberosAuthHandler())
        return urlopener

    mercurial.url.opener = opener
