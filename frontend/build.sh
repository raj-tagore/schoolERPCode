#!/usr/bin/env bash

cd frontend
npm i
npm run build
tar -I 'zstd -20 -T0' -caf build.tar.xz dist/
