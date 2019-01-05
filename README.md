# Prediction-Model
an algorithm to predict y (boolean) with regard to some variables.
this algorithm develops a prediction modem for playing tennis (yes, no).
raw data is shown below. there are some variables; outlook, temperature, humidity and windy, effecting decison for play.
In our algorithm, firstly we convert categoric variables(outlook, humidity, windy) into numeric values with help of LabelEncoder, OneHotEncoder.
And then we build our model and improve it based on P-values of each variable. Enjoy!

outlook	temperature	humidity	windy	play
rainy	65	70	True	no
rainy	71	91	True	no
sunny	72	95	False	no
sunny	80	90	True	no
sunny	85	85	False	no
overcast	64	65	True	yes
rainy	68	80	False	yes
sunny	69	70	False	yes
rainy	70	96	False	yes
overcast	72	90	True	yes
rainy	75	80	False	yes
sunny	75	70	True	yes
overcast	81	75	False	yes
overcast	83	86	False	yes
