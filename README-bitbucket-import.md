
This repository was converted on 2023/06/17 from the Bitbucket archive at
https://bitbucket-archive.softwareheritage.org/projects/to/tolsen/hgkerberos.html
with git-remote-hg and these commands:

```
BBID=3fa0800a-78ab-4de4-817a-39040c0e0015
URL=https://bitbucket-archive.softwareheritage.org/new-static/${BBID:0:2}/${BBID}/${BBID}-repository.tar.gz
curl -O "$URL"
tar xzf $BBID-repository.tar.gz 
mkdir -p bin
curl -o bin/git-remote-hg https://github.com/felipec/git-remote-hg/raw/master/git-remote-hg -L
sed -ei 's/env python/env python3/' bin/git-remote-hg
chmod +x bin/git-remote-hg
git clone hg::file://$(pwd)/${BBID}-repo hgkerb

cd hgkerb
git remote set-url origin https://github.com/hawicz/hgkerberos
git fetch origin
git checkout -b main
git branch -d master
git push -f origin main
git push origin refs/notes/hg refs/hg/origin/bookmarks/master refs/hg/origin/branches/default
```
