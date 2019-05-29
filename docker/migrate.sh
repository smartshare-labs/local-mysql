#!/bin/bash

while ! mysqladmin ping -h"localhost" -u root -p"password" --silent; do
    echo "Waiting for mysql server to start..."
    sleep 1
done

cd ~/

for d in * ; do
  if [ "$d" = 'init' ] ; then
      continue
  else
    cd ${d}
    alembic upgrade head
    cd ../
  fi
done
