1.Navigate to this folder: cd MySQL_Docker

2.Create the custom image:
	docker build -t custom_mysql_image .
<br><br>
3. Create a new file named .env (only if the nr. 4 prompt doesn't want to work)

4.Create container from image:
	docker run --name vote_system -p 3306:3306 --env-file ./.env -d custom_mysql_image

5.The database can be accessed through docker terminal using the following codes, but it can be acces through the 3306 port via Python.

docker exec -it vote_system bash
mysql -u root -p
