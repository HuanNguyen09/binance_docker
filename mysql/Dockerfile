# Sử dụng ảnh MySQL có sẵn trên Docker Hub
FROM mysql:latest

# Thiết lập biến môi trường
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=metastore_db
ENV MYSQL_USER=hive1
ENV MYSQL_PASSWORD=password

# Sao chép các tệp SQL vào thư mục docker-entrypoint-initdb.d để tự động thực hiện khi container khởi chạy
# COPY ./conf/hive-schema-0.14.0.mysql.sql /home/
COPY init.sql /docker-entrypoint-initdb.d/

# Mở cổng MySQL
EXPOSE 3306
