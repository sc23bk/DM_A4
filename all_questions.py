# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "Rules do not conflict with one another; a single person can fit more than one rule."
    answers["(b) explain"] = "Not every case for a possible input is covered by the entire set of rules."
    answers["(c) explain"] = "When numerous rules match, ordering is required to identify which rule to apply."
    answers["(d) explain"] = "For those circumstances that don't fit under any of the listed conditions, a default class is required."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) example"] = "A warm-blooded aerial species might fulfill both R1 and R3, therefore they are not mutually exclusive."
    answers["(b) example"] = "Vertebrates with mixed features or amphibians are not covered by the rules, which are not exhaustive."
    answers["(c) example"] = "A vertebrate could be incorrectly classified if a less suitable rule was applied before the ordering, which is why it is important."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "To update weights effectively and minimize loss, back-propagation computes the gradient of the error at one layer using the gradient from the next layer, as described by the chain rule." # Topic in book page 254
    answers["(b) explain"] = "Activation values at one layer are calculated using those from the previous layer, demonstrating the feedforward nature of ANN computations from input to output."
    answers["(c) explain"] = "The vanishing gradient problem occurs when gradients become too small, inhibiting learning in early layers. It is unrelated to the difference between training and test errors, which signals overfitting." # Topic in book page 253-254
    answers["(d) explain"] = "Even if an ANN model correctly classifies all training cases, gradients are not always zero since gradients reflect the direction of prospective modifications to reduce error rather than the lack of error itself." # Topic in book page 253-254

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.5

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 50

    # explain_string
    answers["(a) explain"] = "A smaller K = 5, is chosen for well-separated data to limit the chance of noise interfering with classification while capturing the data's local structure."
    answers["(b) explain"] = "A greater K value = 50, is chosen for intermixed data to reduce the influence of overlap and noise by evaluating a bigger neighborhood for classification."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "Feature A equals 1 in 3 of 5 positive examples, resulting in a probability of 60% (P(A=1∣+)."
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 0.857
    answers["(b) P(R|+)"] = 0.192
    answers["(b) P(R|-)"] = 0.032

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = "The test sample (R) has a higher likelihood of belonging to the positive class ('+') with a posterior probability of 0.857 (P(R∣+)=0.192 vs. P(R∣−)=0.032)."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = "yes"
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6  
    answers["(d) P(A=1,B=0)"] = 0.55

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "yes"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.4
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.5

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "yes"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "Given the class, Naive Bayes assumes features are conditionally independent."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
