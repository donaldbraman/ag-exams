#!/bin/bash
export PYTHONPATH=src
export GCP_PROJECT_ID=cite-assist-pipeline

scenarios=(
    "final_the_genesis"
    "final_the_blowback"
    "final_the_distribution_ring"
    "final_hamsterdam"
    "final_the_empire_business"
    "final_procedural_block"
)

# Start all scenarios in parallel
for s in "${scenarios[@]}"; do
    echo "Starting workflow for $s"
    /opt/homebrew/bin/uv run python -m ag_exams start --scenario "$s" > "logs_${s}.txt" 2>&1 &
done

echo "All workflows started in background."
