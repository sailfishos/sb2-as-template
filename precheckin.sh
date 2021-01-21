#!/bin/sh
ARCHS="armv7hl aarch64 i486"

for x in $ARCHS; do
	sed "s/@ARCH@/$x/g" cross-as-template.spec > cross-$x-as.spec
done
