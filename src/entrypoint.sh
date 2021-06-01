case "$1" in
  test)
    exec python -m pytest -s tests
    ;;
  setup)
	exec python /src/app/init/create_mysql_db.py init-db-scheme
	exec python /src/app/init/create_mysql_db.py upload-data
	;;
  *)
    exec "$@"
    ;;
esac

