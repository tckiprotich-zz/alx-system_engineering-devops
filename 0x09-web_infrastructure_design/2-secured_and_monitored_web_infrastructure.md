To address the requirements, we will design a three server web infrastructure that is secure, serves encrypted traffic and is monitored. The infrastructure will consist of:

Load Balancer: The load balancer is added to distribute incoming traffic across the three web servers to ensure high availability and scalability.

Web Servers: The three web servers will host the website and serve incoming traffic. They are added to ensure redundancy and high availability.

Firewall: A firewall is added to protect the servers from external threats and unauthorized access.

HTTPS: HTTPS is added to encrypt the traffic between the web servers and the user's browser, ensuring data confidentiality and integrity.

Monitoring Tool: A monitoring tool is added to monitor the performance and health of the infrastructure.

Logging: Logging is added to track all events and actions on the infrastructure, providing an audit trail for troubleshooting and security purposes.

The load balancer is configured with a round-robin algorithm to distribute incoming traffic evenly across the web servers. This ensures that no server is overloaded and can handle the incoming traffic efficiently.

The load balancer enables an Active-Active setup, where all web servers are active and can receive traffic simultaneously. This ensures high availability and redundancy.

A primary-replica (master-slave) cluster is used for the database. The primary node is responsible for accepting writes, while the replica nodes are responsible for reading data. This ensures data consistency and fault tolerance.

The primary node in the database is responsible for accepting writes from the application server, while the replica nodes are used for read operations.

The issues with this infrastructure are:

Terminating SSL at the load balancer level can be an issue because it increases the risk of man-in-the-middle attacks.

Having only one MySQL server capable of accepting writes can be an issue because it creates a single point of failure.

Having servers with all the same components (database, web server and application server) might be a problem because it increases the risk of all servers being affected by the same vulnerability or bug.

To monitor web server QPS, we can use a monitoring tool that tracks the number of queries per second (QPS) and sends an alert if the threshold is exceeded. We can also monitor the CPU usage and memory usage of the web servers to ensure they are not overloaded.

Overall, this three server web infrastructure provides high availability, scalability, security, and monitoring capabilities.