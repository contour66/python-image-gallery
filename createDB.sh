#!/usr/bin/bash

# shellcheck disable=SC2086
psql -d postgresql://$IG_USER:$IG_PASSWD@$PG_HOST:$PG_PORT/$IG_DATABASE -f create_tables.psql