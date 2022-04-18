# Classic-Optic

# Introduction
An E-commerce, online store created to serve as an interface for a convenience store.

The project includes several functionalities that imitate the workings of real world E-commerce websites.

# Functionality
Currently, our website is deployed using the AWS academy and works best on PC and Laptop.

Features such as registration, adding to cart, checking out, is all well and working.

# Specifications
Classic-Optic uses Java 1.8, Spring Boot version 4, AWS ec2 for Linux machine, AWS RDS, AWS S3 for the storage, and MySQL for the database.

The project uses jsp files, css documents, along with javascript files and java classes to program the website.

# Database Creation
The database for the website is created when the Spring Boot is run. Various tables are created accordingly.

These tables are populated with values using the "eecs4413" file listed in the project documents.

# Running the project
In order to run on AWS, follow these instruction :-

-Login into EC2 instance via ssh connect<br />
-Go to folder classic-optics/GiftShop via command (cd classic-optics/GiftShop)<br />
-Run it via the command (mvn springboot:run &)<br />
-Run the command (disown %1)<br />
-See the website running on Public IPV4 url<br />
