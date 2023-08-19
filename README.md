
Current maintainer: Eric Hawicz
Original Author: Tim Olsen <tim AT jux DOT com>

Download site: https://github.com/hawicz/hgkerberos


Overview
--------

hgkerberos provides support for kerberos authentication
(Negotiate/SPNEGO) over HTTP.

hgkerberos has been successfully tested against Apache's mod_auth_kerb.


Install prerequisites
---------------------
* Kerberos libraries (as root)
    * Will probably happen automatically in the next step
    * If installing pykerberos from source, you will need dev headers

```
apt-get install libkrb5-dev
```

* pykerberos (as root)
    * In debian, the package is python3-kerberos, which uses https://pypi.org/project/pykerberos

    ```
    apt-get install python3-kerberos
    ```

    * Optionally, install newer code as maintained by apple, see https://pypi.org/project/kerberos and https://github.com/apple/ccs-pykerberos

    ```
    pip install --user kerberos
    ```

    * On Windows, https://pypi.org/project/winkerberos might work (untested)

* urllib_kerberos (optionally as root)

```
pip3 install --user urllib_kerberos    # Drop --user to install system-wide
```


Install hgkerberos extension
----------------------------

* Install kerberos.py into a hgext directory
    * The system-wide directory is likely something like /usr/lib/python3/dist-packages/hgext
    * Alternately, copy into a per-user ~/.hgext/ directory:

```
mkdir -p ~/.hgext
cp kerberos.py ~/.hgext/.
```

* Configure your .hgrc to enable the extension by adding following lines:

    ```
    [extensions]
    hgext.kerberos=
    # or, if kerberos.py is not in the system hgext dir:
    # kerberos=/home/youruserid/.hgext/hgkerberos.py
    ```
   
    * Command to update .hgrc:

    ```
    # Update your .hgrc config:
    grep -q '^kerberos=' ~/.hgrc || sed -i -e"/\[extensions\]/a\
    kerberos=${HOME}/.hgext/kerberos.py" ~/.hgrc
    ```

