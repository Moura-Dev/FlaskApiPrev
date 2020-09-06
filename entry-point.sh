#! /bin/bash

until flask db upgrade
  do
      echo "Waiting for mysql ready..."
      sleep 5
      flask db init
      flask db migrate -m 'create initial tables'
  done

flask run --host=0.0.0.0