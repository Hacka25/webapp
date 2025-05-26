<think>
Okay, let's tackle this. The user wants a comprehensive README.md based on the provided source code files. First, I need to understand what each file does and how they interact.

Looking at the files, there's a Terraform project with several resources. The main.tf uses variables.tf and gke.tf to define the Google Kubernetes Engine cluster and a SQL database. The deployment.yaml and service.yaml are Kubernetes manifests for deploying the application.

The project likely involves setting up a Kubernetes cluster with a MySQL database, using Terraform to manage the infrastructure. The key components would be the Terraform variables, the GKE cluster, the SQL instance, and the Kubernetes deployment and service.

I need to outline what the project does: creating a GKE cluster with a MySQL database, deploying an application that connects to it. Then, explain the key components: variables, GKE cluster, SQL instance, Kubernetes deployment, and service.

Installation steps would involve initializing Terraform, applying the variables, and then deploying the Kubernetes resources. Special features might include the use of variables for flexibility, the integration with Google Cloud, and the Kubernetes service type.

I should also mention the sensitive variables like db_password, which are handled via Terraform variables. The deployment.yaml uses a secret for the MySQL credentials, which is managed through the Kubernetes secrets.

Potential insights: the use of the cloudsql-instance-credentials secret, the node configuration in the GKE cluster, and the environment variables in the deployment. Also, the fact that the cluster is removed default node pool to avoid issues.

Make sure to avoid placeholders and provide specific details. Check that all files are covered, and the README is professional and technical.
</think>

# **GKE MySQL Database Infrastructure with Terraform**

---

## 🧩 Overview

This project leverages **Terraform** to provision a **Google Kubernetes Engine (GKE) cluster** with a **MySQL database**, and deploy an application that connects to it. The infrastructure is designed to be scalable, secure, and managed via Terraform's declarative syntax.

---

## 🔧 Key Components

### 1. **Terraform Variables**
The `variables.tf` file defines the infrastructure's configuration, including:
- `project_id`: The Google Cloud project ID.
- `region`: Default region (`us-central1`).
- `gke_cluster_name`: Name of the GKE cluster.
- `db_user`: Username for the MySQL database.
- `db_password`: Sensitive password for the MySQL database.

### 2. **GKE Cluster & Node Pool**
The `gke.tf` file creates:
- A **GKE cluster** (`web-app-cluster`) with:
  - 1 node pool (2 nodes).
  - `e2-medium` machines.
  - `remove_default_node_pool` to avoid accidental deletion.
- A **node pool** with:
  - `initial_node_count = 1` (single node for simplicity).
  - `machine_type = "e2-medium"`.

### 3. **MySQL Database**
The `sql.tf` file creates:
- A **MySQL instance** (`mysql-db`) in the specified region.
- A **SQL user** with the specified credentials.
- The instance is configured with:
  - `db-f1-micro` tier.
  - `private_network` for connectivity.

### 4. **Kubernetes Deployment & Service**
The `k8s/deployment.yaml` defines:
- A **deployment** with 2 replicas of the application (`web-app`).
- **Environment variables** for database connection:
  - `DB_HOST`: `127.0.0.1` (localhost).
  - `DB_USER`: from a Kubernetes secret (`db-credentials`).
  - `DB_PASSWORD`: from the same secret.
- A **service** of type `LoadBalancer` to expose the application.

### 5. **Secret Management**
The `k8s/deployment.yaml` uses a **Kubernetes secret** (`db-credentials`) to store the `db_password` securely. This secret is mounted into the `cloudsql-proxy` container to authenticate with the MySQL instance.

---

## 🛠 Installation & Running

### 1. **Initialize Terraform**
```bash
terraform init
```

### 2. **Apply Configuration**
```bash
terraform apply
```

### 3. **Verify Setup**
- Check the GKE cluster and MySQL instance via:
  ```bash
  gcloud container clusters list
  gcloud sql instances list
  ```
- Confirm the Kubernetes service is exposed:
  ```bash
  kubectl get services
  ```

### 4. **Access Application**
- The application runs as a **Pod** in the `web-app` namespace.
- The `LoadBalancer` service exposes the application at `http://web-app-service:80`.

---

## 📦 Special Features & Configurations

### 1. **Secret Management**
- The `db_password` is stored in a Kubernetes secret (`db-credentials`) and used in the `cloudsql-proxy` container.
- The secret is mounted as a read-only volume to prevent accidental modification.

### 2. **Security & Compliance**
- The GKE cluster uses the `https://www.googleapis.com/auth/cloud-platform` OAuth scope.
- The MySQL instance is configured with a private network for secure connectivity.

### 3. **Environment Variables**
- The deployment includes environment variables for database credentials, which are managed via the Kubernetes secret.

### 4. **Scalability**
- The deployment is designed for horizontal scaling (2 replicas), and the GKE cluster supports node pool expansion.

---

## 📁 File/Function Insights

### `output.tf`
- Outputs the GKE cluster name and MySQL instance connection name for debugging or external use.

### `variables.tf`
- Defines default values for configuration parameters (e.g., `db_user`, `db_password`).
- Sensitive variables like `db_password` are managed via Terraform variables.

### `sql.tf`
- Creates a MySQL instance with specific settings (tier, network, and user permissions).
- The `sql_user` resource grants access to the instance.

### `gke.tf`
- Configures the GKE cluster and node pool with specific machine types and scopes.
- The `remove_default_node_pool` ensures no accidental deletion of nodes.

### `k8s/deployment.yaml`
- Defines the application deployment with:
  - `env` for database credentials.
  - `volumeMounts` for the secret file (`/secrets/service_account.json`).
  - `command` for the `cloudsql-proxy` container.

---

## 📝 Notes

- **Project ID**: Replace `YOUR_PROJECT_ID` in the `cloudsql-proxy` image with your actual project ID.
- **Region**: The default region is `us-central1`, but you can change it via `var.region`.
- **Security**: Ensure the `db_password` is stored securely in the Kubernetes secret.
- **Monitoring**: Consider adding Cloud Monitoring or Cloud Logging for infrastructure health checks.

---

## 📚 References

- [Terraform Provider Documentation](https://www.terraform.io/docs/)
- [Google Cloud SQL Documentation](https://cloud.google.com/sql/docs)
- [Kubernetes Secret Management](https://kubernetes.io/docs/concepts/secret/)

---

This README provides a comprehensive guide to deploying and managing the GKE + MySQL infrastructure using Terraform. Let me know if you'd like additional features like custom images, CI/CD pipelines, or monitoring!