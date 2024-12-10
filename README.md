python3 -m venv venv
source venv/bin/activate





 pip install hypothesis
 python3 -m unittest discover
 coverage run -m unittest discover  
 coverage html            
 mutmut run
 mutmut results
 mutmut show <result_file_name>
 mutmut results --all true 
