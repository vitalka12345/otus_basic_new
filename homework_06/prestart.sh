#!/usr/bin/env bash
# не проходят миграции на prod-posts
echo Apply migrations...

flask db upgrade

echo migrations ok

exec "$@"
