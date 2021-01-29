#!/bin/sh
ARCHS="armv7hl aarch64 i486"

for x in $ARCHS; do
	if [ $x = "armv7hl" ]
        then
		sed "s/@ARCH@/$x/g;s/@ABI@/gnueabi/g" cross-as-template.spec > cross-$x-as.spec
        else
                sed "s/@ARCH@/$x/g;s/@ABI@/gnu/g" cross-as-template.spec > cross-$x-as.spec
        fi
done
