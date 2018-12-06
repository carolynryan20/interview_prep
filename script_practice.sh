#!/bin/bash

# To run: source script.sh <PATH_TO_DAT_FOLDER> <MAX_CPU_PERCENT_INT>
# Will run transmogrify in parallel on every .dat file in given path
# Will not exceed 36 jobs
# Will not exceed %CPU specified 


# Function to get the current number of jobs running on the system
# Uses the process status and search for running bash commands
get_cur_num_jobs() {
	cur_num_jobs=$(ps | grep -c bash)
}


# Function to get the current percentage of CPU usage
# Uses ps to get cpu usage
get_cur_cpu() {
	cur_cpu_list=($(ps -o %cpu))
	
	# First line of usage is '% CPU', want to remove that line
	firstitem=$1
	shift;
	
	# Loop over every line, which is CPU for given job
	cur_cpu="0"
	for item in "${cur_cpu_list[@]:1}" ; do
  		# %CPU is given as float, bash doesn't support float addition
  		# Use python for float addition
  		cur_cpu=$(python -c "print($cur_cpu+$item)")
	done
	
	# Round the CPU to an int for ease of comparison later
	# Use python's round method
	cur_cpu=$(python -c "print(round($cur_cpu))")
}

# Pretend to be a function that takes a while to run to check parallelization 
# Takes in input_file output_file in same form as real transmogrify
pretend_transmogrify() {
	sleep $(($RANDOM % 5))
	echo $1 $2
}

# Function to actually process files in parallel 
main() {
	# Hard code max jobs for comparison, get max cpu from user 
	MAX_JOBS="36"
	DOC_PATH="$1*.dat"
	MAX_CPU=$2
	
	echo "Will not exceed $MAX_CPU % CPU or $MAX_JOBS jobs"

	# Get list of files, loop until all processed in background
	files_processed=-1 # Want output files to start at 0000, start counter at -1

	# Loop over all given files
	for filename in $DOC_PATH; do
		# Get list of jobs before start to establish cur_num_jobs and cur_cpu for while loop
		get_cur_num_jobs
		get_cur_cpu
		
		# Waste time if we are above the limit of either jobs or cpu
		while [  $cur_num_jobs -gt $MAX_JOBS -o $cur_cpu -gt $MAX_CPU ]; do
			get_cur_num_jobs
			get_cur_cpu
		done
		
		# Increase files processed by 1
		files_processed=$(( $files_processed + 1 ))
		
		# Zero pad files processed for output.dat
		# Have to introduce new variable otherwise interpreted as octal, causes base error
		printf -v files_processed_zero_padded "%04d" $files_processed
		
		# Run the transmogrify, currently faked
		# & runs the process in the background
		transmogrify $filename $files_processed_zero_padded.dat &
	done
}

# Call main function to apply parallel transmogrify
# $1 is path to directory containing .dat files to run on
# $2 is max % cpu desired by user
main $1 $2

