## Connecting to the Server

```
$ ssh ashish@52.187.63.154
```

- key: id_rsa

If key doesn't work, try:

```
$ chmod 400 id_rsa
```

## Web App
- 4 Variations inside the mh-annotation repo; details below: 


| Web App       	  				| Screen        	| Port  |
| ----------------------------------|:-----------------:| -----:|
| content_annotation  				| ca_broad 			| 9000  |
| content_annotation_sub_cat    	| ca_sub_cat      	| 10000 |
| content_annotation_new      		| ca_new_broad 		| 11000 |
| content_annotation_sub_cat_new	| ca_new_sub_cat	| 12000 |


For running a web app, cd into the respective folder and then run the following command:

```
$ python manage.py runserver 0.0.0.0:<Port>
```

## Weekly Dumps

Run the following bash script:

```
$ ./weekly-dumps.sh 
```

Prerequisites: [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)

## Accessing the SQL

In the VM:

```
$ sudo /usr/bin/mysql -u ashish -p
```

password: **** (check e-mail)

Note: This might be needed if I want to make any changes to the dataset.
