provider "google" {
  project = var.project_id
  region  = var.region
}
provider "aws" {
  project = var.account_id
  region  = var.region
}

