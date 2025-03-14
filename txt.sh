#!/bin/bash

# Get the Cloud Run URL
CLOUD_RUN_URL=$(gcloud run services describe my-function --region us-central1 --format=json | jq -r ".status.address.url")

# Get an Identity Token
IDENTITY_TOKEN=$(gcloud auth print-identity-token)

# Test GET Request
echo "Testing GET Request..."
curl -H "Authorization: Bearer $IDENTITY_TOKEN" "$CLOUD_RUN_URL?name=Ryan"
echo -e "\n"

# Test POST Request
echo "Testing POST Request..."
curl -X POST "$CLOUD_RUN_URL" \
     -H "Authorization: Bearer $IDENTITY_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"name": "Ryan", "age": 30}'
echo -e "\n"

# Test PUT Request (Corrected)
echo "Testing PUT Request..."
curl -X PUT "$CLOUD_RUN_URL" \
     -H "Authorization: Bearer $IDENTITY_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"status": "updated", "message": "This is a PUT request"}'
echo -e "\n"

# Test DELETE Request
echo "Testing DELETE Request..."
curl -X DELETE "$CLOUD_RUN_URL" \
     -H "Authorization: Bearer $IDENTITY_TOKEN"
echo -e "\n"