build:
	docker build -t ubuntu-java8-base ./base
	docker build -t hadoop ./hadoop
	docker build -t mysql ./mysql
	docker build -t hive ./hive
	docker build -t airflow ./airflow
	docker build -t superset ./superset