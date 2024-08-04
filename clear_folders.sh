#!/bin/bash

# Define the directories
INPUT_DIR="input"
OUTPUT_FORMATTED_DIR="output/formatted_transcripts"
OUTPUT_RAW_DIR="output/raw_transcripts"
OUTPUT_NOTES_DIR="output/transcript_notes"

# Function to clear a directory
clear_directory() {
    local dir=$1
    if [ -d "$dir" ]; then
        rm -rf "$dir"/*
        echo "Cleared all files in $dir"
    else
        echo "Directory $dir does not exist"
    fi
}

# Clear the directories
clear_directory "$INPUT_DIR"
clear_directory "$OUTPUT_FORMATTED_DIR"
clear_directory "$OUTPUT_RAW_DIR"
clear_directory "$OUTPUT_NOTES_DIR"

echo "All specified directories have been cleared."