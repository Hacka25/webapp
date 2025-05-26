output "gke_cluster_name" {
  value = google_container_cluster.primary.name
}

output "sql_instance_connection_name" {
  value = google_sql_database_instance.mysql_instance.connection_name
}
