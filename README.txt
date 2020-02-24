Run location_predictor.py to generate predictions. 

The program parses the training data from lab2_rss and runs the regression. To find the distance between the car and the Wi-Fi device, we calculate distance from the equation rss = B + A * log_10(d), where d is the distance. Given the coefficient and the intercept from the regression, we can solve for d and generate a prediction. 


