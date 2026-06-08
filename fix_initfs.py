with open('/tmp/pmb/pmb/chroot/initfs.py') as f:
    c = f.read()
t = 'pmb.chroot.root(["mkinitfs"], chroot)'
x = 'pmb.chroot.root(["sh","-c","truncate -s 0 /usr/share/mkinitfs/modules/00-default.modules"],chroot)'
c = c.replace(t, x + '\n    ' + t, 1)
with open('/tmp/pmb/pmb/chroot/initfs.py', 'w') as f:
    f.write(c)
print('Patched!')
