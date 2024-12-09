#!/bin/bash
echo "Running unit tests..."
coverage run -m unittest discover
echo "Generating coverage report..."
coverage html
echo "Running mutation tests..."
mutmut run
echo "Mutation testing results:"
mutmut results
