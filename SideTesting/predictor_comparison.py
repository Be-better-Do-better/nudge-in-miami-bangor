import time

def compare_predictors(predictors, test_data):
  for predictor in predictors:
    start_time = time.time()
    accuracy = predictor.evaluate(test_data)
    end_time = time.time()
    print(f'{predictor.name} predictor took {end_time - start_time:.2f} seconds and had an accuracy of {accuracy:.2f}')

# Example usage
test_data = ... # Load your test data
predictor_1 = ... # Initialize your first predictor
predictor_2 = ... # Initialize your second predictor
predictors = [predictor_1, predictor_2]
compare_predictors(predictors, test_data)