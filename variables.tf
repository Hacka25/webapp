variable "project_id" {}
variable "region" {
  default = "us-central1"
}
variable "gke_cluster_name" {
  default = "web-app-cluster"
}
variable "db_user" {
  default = "admin"
}
variable "db_password" {
  sensitive = true
}
variable "aws_cluster_name" {
  default = "web-app-cluster"
}
variable "aws_db_user" {
  default = "admin"
}
variable "aws_db_password" {
  sensitive = true
}
