gen:
	bash traverse.sh

train:
	svm-train train

class:
	svm-predict test train.model
