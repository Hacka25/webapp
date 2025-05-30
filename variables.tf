variable "project_id" {}
variable "region" {
  default = "us-central1"
}
variable "gke_cluster_name" {
  default = "web-app-cluster"
}
variable "db_user" {
  default = "dadmin"
}
variable "db_password" {
  sensitive = true
}
