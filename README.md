# sennder-ghibli-test
Serve a page with the films produced by the Ghibli studio. 

## Usage 
1. Clone the repository from github. 
2. install the requirements
```shell script
pip install -r requirements.txt
```
3. Launch the application
```shell script
python src/app.py run 
```
4. Access the application from your favorite browser on http://localhost:8000/movies

## Test
This project is using **pytest** as the tests runner. Use the command below to execute the tests on the application. 
```shell script
pytest -v src/tests
```
> Verbose mode is prefered to follow test execution during developments.

## Benchmark
This project is using **pytest-bechmark** as the benchmark runner. Use the command below to execute the benchmarks on the application. 
```shell script
pytest -v src/benchmark
```

> Verbose mode is prefered to follow benchmark execution during developments.

## Pycharm settings 
Set the **src** directory as the root directory.

## Remarks
### Features
The application display the list of the movies produced by the Ghibli Studio. For each movie, the list of characters is displayed. 

### Additional features
The application expose an API and uses it to load the movies covers and display them on the web page.
