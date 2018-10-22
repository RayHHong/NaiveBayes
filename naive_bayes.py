# naive_bayes.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Justin Lizama (jlizama2@illinois.edu) on 09/28/2018

"""
This is the main entry point for MP4. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
import math

def naiveBayes(train_set, train_labels, dev_set, smoothing_parameter):
    """
    train_set - List of list of words corresponding with each email
    example: suppose I had two emails 'i like pie' and 'i like cake' in my training set
    Then train_set := [['i','like','pie'], ['i','like','cake']]

    train_labels - List of labels corresponding with train_set
    example: Suppose I had two emails, first one was spam and second one was ham.
    Then train_labels := [0,1]

    dev_set - List of list of words corresponding with each email that we are testing on
              It follows the same format as train_set

    smoothing_parameter - The smoothing parameter you provided with --laplace (1.0 by default)
    """
    # TODO: Write your code here
    # return predicted labels of development set


    len_ham = (train_labels == 0).sum()
    p_ham = len_ham/len(train_labels)

    len_spam = (train_labels == 1).sum()
    p_spam = len_spam/len(train_labels)


    # init_probs = {}
    # for w in train_set:
    #     init_probs[w] = train_set.count(w)/len(train_set)

    total_spam = 0
    total_ham = 0
    spam_sum = {}
    ham_sum = {}
    total = {}

    for e, i in zip(train_set, train_labels):
        if(i == 1):
            total_spam += len(e)
            for w in e:
                if w not in spam_sum:
                    spam_sum[w] = 1
                elif w in spam_sum:
                    spam_sum[w] += 1
                if w not in total:
                    total[w] = 1
        elif(i == 0):
            total_ham += len(e)
            for w in e:
                if w not in ham_sum:
                    ham_sum[w] = 1
                elif w in ham_sum:
                    ham_sum[w] += 1
                if w not in total:
                    total[w] = 1
    # print(spam_probs)



    ##laplace smoothing
    #SPAM
    n = sum(spam_sum.values())
    V = len(total)
    spam_probs = {k: math.log((spam_sum[k]+smoothing_parameter)/(n+smoothing_parameter*(V+1))) for k in spam_sum}

    # print(spam_probs)
    # print(sum(spam_probs.values()))




    dev_probs = {}

    for i,l in enumerate(dev_set):
        dev_probs[i] = 0
        for w in l:
            if(w in spam_probs):
                dev_probs[i] += spam_probs[w]
            else:
                dev_probs[i] += math.log((smoothing_parameter)/(n+smoothing_parameter*(V+1)))

        # print(dev_probs[i])




    #HAM
    n = sum(ham_sum.values())
    V = len(total)

    ham_probs = {k: math.log((ham_sum[k]+smoothing_parameter)/(n+smoothing_parameter*(V+1))) for k in ham_sum}

    #print(sum(ham_probs.values()))



    dev_probs_ham = {}

    for i,l in enumerate(dev_set):
        dev_probs_ham[i] = 0
        for w in l:
            if(w in ham_probs):
                dev_probs_ham[i] += ham_probs[w]
            else:
                dev_probs_ham[i] += math.log((smoothing_parameter)/(n+smoothing_parameter*(V+1)))

        #print(dev_probs_ham[i], dev_probs[i])


    dev_labels = []
    for i in range(len(dev_set)):
        if(dev_probs_ham[i] > dev_probs[i]):
            dev_labels.append(0)
        else:
            dev_labels.append(1)







    return dev_labels
