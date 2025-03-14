terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.25.0"
    }
  }
}
provider "google" {
    project = "dalinar-kholin"
    region = "us-central1"
    
  
}