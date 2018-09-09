import os
import glob
import subprocess

V = "8.3.0"

for path in glob.glob('*.tar.gz'):
    os.unlink(path)

res = []
pwd = os.path.dirname(os.path.abspath(__file__))
for path in os.listdir('.'):
    if path == 'build.py':
        continue
    if path == 'neutrino':
        package = path
    else:
        package = '@neutrino/%s' % path
    af = '%s.%s.tar.gz' % (path, V)
    tar = "tar zcfv %s %s" % (af, path)
    output = subprocess.check_output(['bash', '-c', tar])
    res.append('"%s": "https://github.com/kalekseev/neutrino/releases/download/v8.3.0/%s"' % (package, af))
print(',\n'.join(res))
