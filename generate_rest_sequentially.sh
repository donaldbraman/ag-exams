#!/bin/bash
# Note: We run the generation workflows sequentially rather than in parallel.
# Starting all workflows at once causes massive worker fan-out which
# chokes the CPU, exhausts API rate limits, and triggers GCP SecretNotFoundError crashes.

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

# Start all scenarios sequentially to avoid worker fan-out choking
for s in "${scenarios[@]}"; do
    echo "Starting workflow for $s"
    /opt/homebrew/bin/uv run python -m ag_exams start --scenario "$s" > "logs_${s}.txt" 2>&1
    echo "Completed $s"
done

echo "All sequential workflows completed."
