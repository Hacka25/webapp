<think>
Okay, let's tackle this. The user wants me to generate a README.md based on the provided source code files. First, I need to understand what each file does and how they interact.

Looking at the files, there's a Terraform project with several resources. The main.tf, variables.tf, sql.tf, gke.tf, and the Kubernetes deployment and service files. The key components here are the Terraform variables, the GKE cluster, the SQL database instance, and the Kubernetes deployment.

The project seems to be setting up a Kubernetes cluster with a MySQL database. The variables.tf defines project ID, region, cluster name, database user, and password. The SQL.tf creates a Google SQL database instance with specific settings. The gke.tf creates a GKE cluster and a node pool. The deployment.yaml and service.yaml are for Kubernetes, deploying a web app with a MySQL connection.

So, the README needs to explain what the project does, key components, installation steps, special features, and insights into the files.

Starting with the project description: it's a Terraform setup for a GKE cluster with a MySQL database. The main components are the Terraform variables, GKE cluster, SQL instance, and Kubernetes deployment. The installation involves setting up Terraform, variables, applying the Terraform code, and deploying the Kubernetes resources.

Special features might include the use of Google Cloud's resources, the configuration of the GKE cluster and node pools, and the Kubernetes deployment with environment variables. Also, the use of a secret for the database password in the Kubernetes service.

I need to make sure to mention the key components: variables, GKE cluster, SQL instance, Kubernetes deployment. Then, how to install: terraform init, apply, check the cluster, deploy the app. Also, the special configurations like the secret management, the use of the cloudsql-proxy, and the environment variables in the deployment.

Insights into the files: the variables.tf defines default values, the sql.tf sets up the database, the gke.tf creates the cluster and nodes, and the deployment.yaml and service.yaml handle the Kubernetes resources.

I need to structure the README with sections: Project Description, Key Components, Installation/Running, Special Features, File/Function Insights. Make sure it's professional and technical, avoiding markdown but using sections with headings. Use clear language, explain each part, and ensure that the steps are actionable.
</think>

# **GKE + MySQL Deployment with Terraform**  
**Project Overview**  
This project uses Terraform to provision a Google Kubernetes Engine (GKE) cluster with a MySQL database instance, configured to run a web application. It leverages Google Cloud's infrastructure to manage resources such as clusters, nodes, and databases, and integrates with Kubernetes services for deployment and scaling.

---

## **Key Components**  
1. **Terraform Variables**  
   - `project_id`: Specifies the Google Cloud project to use.  
   - `region`: Default region for resources (e.g., `us-central1`).  
   - `gke_cluster_name`: Name of the GKE cluster.  
   - `db_user`: Database user for the MySQL instance.  
   - `db_password`: Secret password for the database user (stored in a secret).  

2. **GKE Cluster & Node Pool**  
   - `google_container_cluster.primary`: Creates a GKE cluster with 1 node.  
   - `google_container_node_pool.primary_nodes`: Configures a node pool with 2 nodes, each running a VM instance.  

3. **MySQL Database Instance**  
   - `google_sql_database_instance.mysql_instance`: Creates a managed MySQL instance with:  
     - Name: `mysql-db`  
     - Region: `var.region`  
     - Tier: `db-f1-micro` (low-cost, micro instance)  
     - IP configuration: Uses a private network for security.  

4. **SQL User & Secret Management**  
   - `google_sql_user.users`: Creates a user with access to the MySQL instance.  
   - `k8s/deployment.yaml`: Uses a Kubernetes secret (`db-credentials`) to manage the database password.  

5. **Kubernetes Deployment**  
   - `k8s/deployment.yaml`: Deploys a web application with:  
     - 2 replicas for redundancy.  
     - Environment variables for database connection (`DB_HOST`, `DB_USER`, `DB_PASSWORD`).  
     - A cloudsql-proxy container to connect to the MySQL instance.  
     - Volume mount for secrets (`sql-creds`) to securely store the password.  

---

## **How to Install and Run**  
### **1. Set Up Terraform**  
- Install Terraform and ensure the `google` provider is configured.  
- Set environment variables:  
  ```bash
  export PROJECT_ID="your-project-id"
  export REGION="us-central1"
  ```

### **2. Initialize and Apply**  
- Create the Terraform workspace:  
  ```bash
  terraform init
  ```
- Apply the configuration:  
  ```bash
  terraform apply
  ```

### **3. Verify Resources**  
- Check the GKE cluster and node pool:  
  ```bash
  gcloud container clusters get-credentials web-app-cluster --project ${PROJECT_ID}
  ```
- Confirm the MySQL instance and user:  
  ```bash
  gcloud sql instances describe mysql-db --project ${PROJECT_ID}
  ```

### **4. Deploy the Web Application**  
- Create a Kubernetes cluster (if not already created):  
  ```bash
  kubectl apply -f k8s/deployment.yaml
  ```
- Verify the deployment:  
  ```bash
  kubectl get pods -l app=web
  ```

---

## **Special Features & Configurations**  
- **Secret Management**:  
  - The `db_password` is stored in a Kubernetes secret (`db-credentials`) and used in the deployment.  
  - The `sql-creds` volume mounts to securely store the password.  
- **Security**:  
  - The GKE cluster uses a private network for node pools.  
  - The cloudsql-proxy connects to the MySQL instance via TCP/3306.  
- **Auto-scaling**:  
  - The deployment supports horizontal scaling via Kubernetes.  
- **Environment Variables**:  
  - The web app uses `DB_HOST`, `DB_USER`, and `DB_PASSWORD` from the Kubernetes environment.  

---

## **File/Function Insights**  
### **`variables.tf`**  
- Default values are used for `gke_cluster_name` and `db_user` to ensure flexibility.  
- The `db_password` is marked as `sensitive` to prevent it from being exposed in logs or outputs.  

### **`sql.tf`**  
- The `settings` block configures the MySQL instance with a low-cost `db-f1-micro` tier.  
- The `ip_configuration` uses a private network for isolation and security.  

### **`gke.tf`**  
- The `remove_default_node_pool` flag ensures no default nodes are retained.  
- The `initial_node_count` is set to 1, with `node_count` = 2 for the node pool.  

### **`k8s/deployment.yaml`**  
- The `cloudsql-proxy` container uses a credential file (`/secrets/service_account.json`) for secure access to the MySQL instance.  
- The `env` block dynamically injects environment variables from the Kubernetes secret.  

---

## **Troubleshooting Tips**  
- Ensure the `project_id` and `region` are correctly set in the Terraform configuration.  
- Verify that the Kubernetes secret `db-credentials` is created and accessible in the deployment.  
- Use `kubectl get pods` to check if the deployment is running and logs are visible.  

---

## **Conclusion**  
This project provides a scalable, secure, and manageable infrastructure for deploying a web application with a MySQL database on Google Cloud. It leverages Terraform for infrastructure as code, Kubernetes for deployment, and Google Cloud services for managed resources. The configuration is modular, with clear separation of concerns between Terraform, Kubernetes, and cloud service resources.

## 🧭 Architecture Diagram
```mermaid
graph TD
<think>
Okay, let's tackle this problem. The user wants a Mermaid graph diagram based on the provided source code. The key here is to visualize the architecture, service flow, or component interactions. 

First, I need to understand the components in the source code. The files mentioned are output.tf, variables.tf, sql.tf, main.tf, gke.tf, and k8s/deployment.yaml and k8s/service.yaml. 

Looking at the output.tf, there are two outputs: gke_cluster_name and sql_instance_connection_name. These are values from the Google provider variables. The variables.tf has variables like project_id, region, gke_cluster_name, db_user, and db_password. The sql.tf defines a Google SQL database instance with specific settings, and the google_sql_user resource creates a user for that instance. 

The main.tf uses the variables, and the gke.tf creates a Google Container Cluster and a node pool. The k8s/deployment.yaml shows a Kubernetes Deployment with a web app, and the service.yaml is a LoadBalancer service for that deployment.

So the components here are the variables, resources (like the SQL database, GKE cluster, Kubernetes deployment), and the services. The Mermaid graph should connect these components. 

I need to map out the flow. The variables are set in variables.tf, which are used in the resources. The SQL database is created in sql.tf, and the GKE cluster is in gke.tf. The Kubernetes deployment uses the SQL instance's connection name, which is output from the SQL.tf. The service.yaml is a LoadBalancer service for the deployment.

So the diagram should have nodes for each of these components. The variables.tf variables are inputs to the resources. The SQL database is created, then the user is added. The GKE cluster is created, and the node pool is set up. The Kubernetes deployment uses the SQL instance's connection name and the GKE cluster's name. The service is a LoadBalancer service for the deployment.

I need to make sure the Mermaid graph starts with graph TD and connects the nodes properly. The variables are on the left, then the resources, then the Kubernetes components. The flow would be from variables to resources, then to the Kubernetes deployment and service.

Wait, the user wants a diagram that shows the architecture, service flow, or component interaction. So maybe the flow is from variables to resources, then to the Kubernetes deployment, and the service. The diagram should show how the variables are used in the resources, which then interact with the Kubernetes deployment and service.

So the nodes would be:

- Variables (project_id, region, gke_cluster_name, db_user, db_password)
- Resources: SQL database instance, user, GKE cluster, node pool
- Kubernetes Deployment and Service

The connections would be from variables to resources, then resources to the deployment and service. The service is a LoadBalancer, so maybe a line from the deployment to the service.

I need to make sure the Mermaid syntax is correct. The graph should start with graph TD, then define the nodes and edges. The variables are on the left, then the resources, then the deployment and service.

Let me structure it step by step:

1. Variables: project_id, region, gke_cluster_name, db_user, db_password.
2. Resources: SQL database instance (with settings), user, GKE cluster, node pool.
3. Kubernetes Deployment: uses the SQL instance's connection name, GKE cluster name, and environment variables from the variables.
4. Kubernetes Service: LoadBalancer type, selector for the deployment.

So the edges would be:

- Variables → Resources (SQL, user, GKE, node pool)
- Resources → Kubernetes Deployment (using SQL connection, GKE cluster name)
- Kubernetes Deployment → Kubernetes Service (LoadBalancer)

But I need to make sure the nodes are properly connected. Also, the service is a LoadBalancer, so maybe a line from the deployment to the service.

I should also include the outputs from the variables, like gke_cluster_name and sql_instance_connection_name, which are used in the resources and deployment.

So the diagram would have:

- Variables (project_id, region, gke_cluster_name, db_user, db_password)
- Resources (SQL instance, user, GKE cluster, node pool)
- Deployment (web-app)
- Service (web-app-service)

Edges from variables to resources, resources to deployment, deployment to service.

I need to check if the Mermaid syntax is correct. The graph should start with graph TD, then the nodes and edges. The nodes should be in the correct order, and the edges should connect them appropriately.

Also, the user mentioned to use only valid Mermaid syntax, starting with graph TD. So no extra lines.

Now, putting it all together.
</think>

graph TD
    A[Variables] --> B[SQL Database Instance]
    A --> C[User]
    A --> D[GKE Cluster]
    A --> E[Node Pool]
    B --> F[SQL Instance]
    C --> G[SQL User]
    D --> H[GKE Cluster]
    E --> I[GKE Node Pool]
    F --> J[Deployment]
    G --> J
    H --> J
    I --> J
    J --> K[Kubernetes Deployment]
    K --> L[Kubernetes Service]
    L --> M[LoadBalancer Service]
```