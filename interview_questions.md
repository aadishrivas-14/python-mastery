# Interview Questions - DevOps/Cloud Engineer Role

## Python Programming (20 questions)

1. What are Python decorators and how do you implement them?
2. Explain the difference between `__str__` and `__repr__` methods.
3. What is the GIL (Global Interpreter Lock) and how does it affect multithreading?
4. How do you handle exceptions in Python? Explain try-except-finally.
5. What are context managers and how do you create custom ones?
6. Explain list comprehensions vs generator expressions. When would you use each?
7. What is the difference between `deepcopy` and `shallow copy`?
8. How do you manage dependencies in Python projects?
9. Explain Python's memory management and garbage collection.
10. What are metaclasses in Python?
11. How would you optimize a slow Python script?
12. Explain the difference between `@staticmethod` and `@classmethod`.
13. What are Python's built-in data structures and their time complexities?
14. How do you handle concurrent operations in Python (threading vs multiprocessing vs asyncio)?
15. What is monkey patching and when would you use it?
16. Explain Python's import system and how to avoid circular imports.
17. How do you write unit tests in Python? What frameworks do you use?
18. What are Python type hints and how do they improve code quality?
19. Explain the difference between `is` and `==` operators.
20. How would you parse and process large JSON/XML files efficiently in Python?

## Golang Programming (15 questions)

21. What are goroutines and how do they differ from threads?
22. Explain channels in Go and their use cases.
23. What is the difference between buffered and unbuffered channels?
24. How does Go handle memory management and garbage collection?
25. Explain interfaces in Go and how they differ from other languages.
26. What are defer, panic, and recover in Go?
27. How do you handle errors in Go? Why doesn't Go have exceptions?
28. Explain Go's struct embedding vs inheritance.
29. What is the select statement used for in Go?
30. How do you prevent race conditions in Go?
31. What are Go modules and how do you manage dependencies?
32. Explain the difference between value receivers and pointer receivers.
33. How does Go's scheduler work?
34. What are some common concurrency patterns in Go?
35. How would you profile and optimize a Go application?

## Shell Scripting (10 questions)

36. Write a bash script to monitor disk usage and send alerts when it exceeds 80%.
37. How do you handle command-line arguments in bash scripts?
38. Explain the difference between `$@` and `$*` in bash.
39. How do you debug bash scripts?
40. Write a script to find and kill processes by name.
41. How do you handle errors in bash scripts? What is `set -e`?
42. Explain pipes, redirections, and file descriptors in bash.
43. How would you parse JSON in a bash script?
44. Write a script to automate log rotation.
45. What are bash functions and how do you use them?

## Virtualization (8 questions)

46. Explain the difference between Type 1 and Type 2 hypervisors.
47. What is a Software Defined Network (SDN) and how does it work?
48. How do VMs differ from containers in terms of architecture?
49. What is KVM and how does it work?
50. Explain virtual switches and how they enable VM networking.
51. What is live migration and how does it work?
52. How do you optimize VM performance?
53. What are the security considerations when working with VMs?

## Containers & Kubernetes (15 questions)

54. Explain the difference between Docker images and containers.
55. What is a Dockerfile and what are best practices for writing one?
56. How do you optimize Docker image sizes?
57. Explain Kubernetes architecture (control plane, worker nodes, etcd).
58. What are Pods, Deployments, Services, and Ingress in Kubernetes?
59. How does Kubernetes handle service discovery?
60. Explain ConfigMaps and Secrets in Kubernetes.
61. What are StatefulSets and when would you use them?
62. How do you implement rolling updates and rollbacks in Kubernetes?
63. Explain Kubernetes networking (CNI, pod-to-pod communication).
64. What are DaemonSets and when are they used?
65. How do you handle persistent storage in Kubernetes?
66. Explain Kubernetes resource limits and requests.
67. What are Helm charts and why are they useful?
68. How do you troubleshoot a failing pod in Kubernetes?

## CI/CD (10 questions)

69. Explain the difference between Continuous Integration, Continuous Delivery, and Continuous Deployment.
70. How would you design a CI/CD pipeline for a microservices application?
71. What are GitLab CI/CD pipelines and how do you configure them?
72. Explain Jenkins pipelines (declarative vs scripted).
73. How do you implement blue-green deployments?
74. What is canary deployment and when would you use it?
75. How do you handle secrets in CI/CD pipelines?
76. Explain artifact management in CI/CD.
77. How do you implement automated testing in CI/CD pipelines?
78. What are pipeline stages, jobs, and artifacts in GitLab CI?

## Cloud Platforms - AWS/GCP/Azure (12 questions)

79. Explain the shared responsibility model in cloud computing.
80. What are the core compute services in AWS (EC2, Lambda, ECS, EKS)?
81. How do you design a highly available architecture in AWS?
82. Explain VPC, subnets, route tables, and security groups in AWS.
83. What is IAM and how do you implement least privilege access?
84. How do you implement auto-scaling in cloud environments?
85. Explain S3 storage classes and when to use each.
86. What are managed database services (RDS, DynamoDB) and their benefits?
87. How do you implement disaster recovery in the cloud?
88. Explain CloudFormation/Terraform for infrastructure as code.
89. What are cloud cost optimization strategies?
90. How do you monitor and log cloud resources?

## Platform Tools (10 questions)

91. What is Kafka and how does it work? Explain topics, partitions, and consumer groups.
92. Explain the difference between SQL and NoSQL databases. When would you use each?
93. What is Prometheus and how does it collect metrics?
94. How do you design a monitoring and alerting strategy?
95. Explain Redis data structures and common use cases.
96. What are the differences between PostgreSQL and MongoDB?
97. How do you design REST APIs? What are best practices?
98. Explain API versioning strategies.
99. How do you handle API authentication and authorization?
100. What is rate limiting and how do you implement it?

## Networking (12 questions)

101. Explain the OSI model and TCP/IP model.
102. How does TCP three-way handshake work?
103. What is the difference between TCP and UDP?
104. Explain DNS resolution process in detail.
105. How does DHCP work?
106. What is IPSec and how does it provide security?
107. Explain network namespaces in Linux.
108. How does routing work? Explain static vs dynamic routing.
109. What is NAT and why is it used?
110. Explain VLANs and their purpose.
111. How do you troubleshoot network connectivity issues?
112. What are common network security best practices?

## Linux Systems Administration (15 questions)

113. Explain the Linux boot process.
114. How do you troubleshoot high CPU usage on a Linux system?
115. What are systemd and systemctl? How do you manage services?
116. Explain Linux file permissions and ownership.
117. How do you monitor system performance (top, htop, vmstat, iostat)?
118. What are inodes and how do they work?
119. Explain process states in Linux.
120. How do you troubleshoot disk space issues?
121. What are cgroups and namespaces in Linux?
122. How do you configure and manage firewalls (iptables/firewalld)?
123. Explain Linux networking commands (netstat, ss, ip, tcpdump).
124. How do you handle log management in Linux?
125. What are hard links vs soft links?
126. How do you troubleshoot memory issues in Linux?
127. Explain SELinux/AppArmor and their purpose.

## Scenario-Based Questions (10 questions)

128. A production service is down. Walk me through your troubleshooting process.
129. How would you migrate a monolithic application to microservices?
130. Design a highly available, scalable web application architecture.
131. A Kubernetes pod keeps crashing. How do you debug it?
132. How would you implement zero-downtime deployments?
133. Design a disaster recovery strategy for a critical application.
134. How would you handle a security breach in your infrastructure?
135. A database is running slow. How do you identify and fix the issue?
136. How would you implement multi-region deployment for global users?
137. Design a monitoring and alerting system for 100+ microservices.

## Behavioral & Soft Skills (8 questions)

138. Describe a time when you had to learn a new technology quickly.
139. How do you stay updated with new technologies and best practices?
140. Tell me about a challenging technical problem you solved.
141. How do you handle disagreements with team members?
142. Describe your experience working in an Agile environment.
143. How do you prioritize tasks when everything is urgent?
144. Tell me about a time you made a mistake. How did you handle it?
145. How do you approach documentation and knowledge sharing?

---

## Coding Challenges (5 practical exercises)

### Challenge 1: Python Script
Write a Python script that:
- Monitors multiple log files for ERROR patterns
- Sends alerts when error rate exceeds threshold
- Implements retry logic with exponential backoff
- Uses asyncio for concurrent file monitoring

### Challenge 2: Bash Automation
Write a bash script that:
- Backs up specified directories to S3
- Implements rotation (keep last 7 days)
- Sends notifications on success/failure
- Handles errors gracefully

### Challenge 3: Kubernetes Deployment
Create Kubernetes manifests for:
- A web application with 3 replicas
- ConfigMap for configuration
- Secret for database credentials
- Service and Ingress for external access
- HorizontalPodAutoscaler

### Challenge 4: CI/CD Pipeline
Design a GitLab CI/CD pipeline that:
- Runs unit tests and linting
- Builds Docker image
- Pushes to container registry
- Deploys to staging automatically
- Requires manual approval for production

### Challenge 5: Infrastructure as Code
Write Terraform/CloudFormation to provision:
- VPC with public and private subnets
- EKS/GKE cluster
- RDS database in private subnet
- Application Load Balancer
- Proper security groups and IAM roles

---

**Total Questions: 145 (100+ technical + 5 coding challenges)**
