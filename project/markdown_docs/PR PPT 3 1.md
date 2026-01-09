# DIMENSIONALITY REDUCTION 

**==> picture [720 x 70] intentionally omitted <==**

--- end of page.page_number=1 ---

## Dimensionality of input 

 Number of Observables (e.g. age and income) 

- If number of observables is increased 

   - More time to compute 

 More  memory to store inputs and intermediate results  More complicated explanations (knowledge from learning) 

   - Regression from 100 vs. 2 parameters 

- No simple visualization 

   - 2D vs. 10D graph 

 **Need much more data (curse of dimensionality)** 

- 1M of 1-d inputs is not equal to 1 input of dimension 1M 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=2 ---

## Dimensionality reduction 

- Some features (dimensions) bear little or nor useful information (e.g. color of hair for a car selection) 

   - Can drop some features 

   - Have to estimate which features can be dropped from data 

 Several features can be combined together without loss or even with gain of information (e.g. income of all family members for loan application) 

- Some features can be combined together 

- Have to estimate which features to combine from data 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=3 ---

Feature Selection vs Extraction 

- Feature selection: Choosing _k_ < _d_ important features, ignoring the remaining _d_ – _k_ 

   - Subset selection algorithms 

- Feature extraction: _x i d_ Project the original _i_ , =1,..., 

- dimensions to new _k_ < _d_ dimensions, _z_ , _j_ =1,..., _k j_ 

   - Principal Components Analysis (PCA) 

   - Linear Discriminant Analysis (LDA) 

   - Factor Analysis (FA) 

Lecture Notes for E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=4 ---

## Usage 

- Have data of dimension d 

- Reduce dimensionality to k<d 

   - Discard unimportant features 

   - Combine several features in one 

- Use resulting k-dimensional data set for 

   - Learning for classification problem (e.g. parameters of probabilities P(x|C) 

   - Learning for regression problem (e.g. parameters for model y=g(x|Thetha) 

--- end of page.page_number=5 ---

## Subset selection 

- Have initial set of features of size d 

- There are 2^d  possible subsets 

- Need a criteria to decide which subset is the best 

- A way to search over the possible subsets 

- Can’t go over all 2^d possibilities 

- Need some heuristics 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=6 ---

# “Goodness” of feature set 

- Supervised 

   - Train using selected subset 

 Estimate error on validation data set 

- Unsupervised 

 Look at input only(e.g. age, income and savings)  Select subset of 2 that bear most of the information about the person 

--- end of page.page_number=7 ---

## Mutual Information 

- Have a 3 random variables(features) X,Y,Z and have to select 2 which gives most information 

- If X and Y are “correlated” then much of the information about of Y is already in X 

- Make sense to select features which are “uncorrelated” 

- Mutual Information (Kullback–Leibler Divergence ) is more general measure of “mutual information” 

- Can be extended to n variables (information variables x1,.. xn have about variable xn+1) 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=8 ---

## Subset-selection 

- Forward search 

   - Start from empty set of features 

   - Try each of remaining features 

   - Estimate classification/regression error for adding specific feature 

   - Select feature that gives maximum improvement in validation error 

   - Stop when no significant improvement 

- Backward search 

   - Start with original set of size d 

   - Drop features with smallest impact on error 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=9 ---

**10** 

## Floating Search 

- Forward and backward search are “greedy” algorithms 

   - Select best options at single step 

   - Do not always achieve optimum value 

- Floating search 

   - _k l_ 

   - Two types of steps: Add , remove 

   - _More computations_ 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=10 ---

**11** 

## Feature Extraction 

- Face recognition problem 

   - Training data input: pairs of Image + Label(name) 

   - Classifier input: Image 

   - Classifier output: Label(Name) 

 Image: Matrix of 256X256=65536 values in range 

   - 0..256 

- Each pixels bear little information so can’t select 100 best ones 

- Average of pixels around specific positions may give an indication about an eye color. 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=11 ---

**12** 

## Projection 

#  Find a projection matrix w from d-dimensional to k- dimensional vectors that keeps error low 

**==> picture [171 x 74] intentionally omitted <==**

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=12 ---

**13** 

## PCA: Motivation 

- Assume that  d observables are linear combination 

- of k<d vectors 

- z =w x +…+w x i i1 i1 ik id 

- We would like to work with basis as it has lesser 

- dimension and have all(almost) required information 

- What we expect from such basis 

   - Uncorrelated or otherwise can be reduced further 

   - Have large variance (e.g. wi1 have large variation) or otherwise bear no information 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=13 ---

## PCA: Motivation 

**==> picture [483 x 337] intentionally omitted <==**

--- end of page.page_number=14 ---

**15** 

## PCA: Motivation 

#  Choose directions such that a total variance of data will be maximum 

 Maximize Total Variance 

 Choose directions that are orthogonal 

 Minimize correlation 

 Choose k<d orthogonal directions which maximize total variance 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=15 ---

## PCA 

- Choosing only directions: 

- 

**==> picture [204 x 49] intentionally omitted <==**

- Maximize variance subject to a constrain using Lagrange 

- Multipliers 

- Taking Derivatives 

**==> picture [201 x 49] intentionally omitted <==**

**==> picture [139 x 42] intentionally omitted <==**

 Eigenvector. Since want to maximize                             we should choose an eigenvector with largest eigenvalue 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=16 ---

**17** 

## PCA 

 d-dimensional feature space 

 d by d symmetric covariance matrix estimated from samples 

 Select k largest eigenvalue of  the covariance matrix and associated k eigenvectors  The first eigenvector will be a direction with largest variance 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=17 ---

**18** 

## What PCA does 

_**z**_ = **W** _[T]_ _**x**_ – _**m**_ ( ) 

# where the columns of **W** are the eigenvectors of **∑** , and _**m**_ is sample mean 

Centers the data at the origin and rotates the axes 

**==> picture [592 x 199] intentionally omitted <==**

--- end of page.page_number=18 ---

How to choose k ? 

- Proportion of Variance (PoV) explained 

**==> picture [139 x 79] intentionally omitted <==**

**==> picture [160 x 79] intentionally omitted <==**

when λ _i_ are sorted in descending order 

- Typically, stop at PoV>0.9 

 Scree graph plots of PoV vs _k_ , stop at “elbow” 

Lecture Notes for E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=19 ---

**==> picture [720 x 26] intentionally omitted <==**

**----- Start of picture text -----**<br>
20<br>**----- End of picture text -----**<br>


--- end of page.page_number=20 ---

**21** 

## PCA 

- PCA is unsupervised (does not take into account class information) 

- Can take into account classes : Karhuned-Loeve Expansion 

   - Estimate Covariance Per Class 

   - Take average weighted by prior 

- Common Principle Components 

   - Assume all classes have same eigenvectors (directions) but different variances (also called as Flury–Gautschi common principal component model.) 

Lecture Notes for E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=21 ---

**22** 

## PCA 

 Does not try to explain noise 

 Large noise can become new dimension/largest PC  Interested in resulting uncorrelated variables which explain large portion of **total** sample variance 

 Sometimes interested in explained shared variance (common factors) that affect data 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=22 ---

**23** 

## Factor Analysis 

- Assume set of unobservable (“latent”) variables 

- Goal: Characterize dependency among observables using latent variables 

- Suppose group of variables  having large correlation among themselves and small correlation with other variables 

- Single factor? 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=23 ---

**24** 

## Factor Analysis 

- Assume k input factors (latent unobservable) 

- variables generating d observables 

- Assume all variations in observable variables are due to latent or noise (with unknown variance) 

- Find transformation from unobservable to observables which explain the data 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=24 ---

## Factor Analysis 

 Find a small number of factors _**z**_ , which when _**x**_ : combined generate 

_x_ – = _v z_ + _v z_ + ... + _v z_ + ε _i µi i_ 1 1 _i2_ 2 _ik k i_ where _z k_ are the latent factors with , _j_ =1,..., _j z z z i ≠_ E[ ]=0, Var( )=1, Cov( _, z_ )=0, _j_ , _j j i , j_ ε are the noise sources _i_ ε ε ε _i ≠_ ε _z_ E[ _i_ ]= ψ _i_ , Cov( _i_ , _j_ ) =0, _j_ , Cov( _i_ , _j_ ) =0 , and _v_ are the factor loadings _ij_ 

Lecture Notes for E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=25 ---

## Factor Analysis 

 Find V such that                             where S is estimation of covariance matrix and V loading (explanation by latent variables) 

- V is d x k matrix (k<d) 

- Solution using eigenvalue and eigenvectors 

**==> picture [256 x 52] intentionally omitted <==**

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=26 ---

**27** 

## Factor Analysis 

#  _z_ In FA, factors are stretched, rotated and _j_ _**x**_ translated to generate 

**==> picture [605 x 262] intentionally omitted <==**

Lecture Notes for E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=27 ---

**28** 

FA Usage 

 Speech  is a function of position of small number of articulators (lungs, lips, tongue) 

 Factor analysis: go from signal space (4000 points for 500ms ) to articulation space (20 points) 

 Classify speech (assign text label) by 20 points 

 Speech Compression: send 20 values 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=28 ---

## Linear  Discriminant Analysis 

#  Find a low-dimensional space such that when _**x**_ is projected, classes are well-separated 

**==> picture [341 x 294] intentionally omitted <==**

--- end of page.page_number=29 ---

**30** 

# Means and Scatter after projection 

**==> picture [438 x 143] intentionally omitted <==**

**==> picture [415 x 140] intentionally omitted <==**

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=30 ---

## Good Projection 

- Means are far away as possible 

- Scatter is small as possible 

- Fisher Linear Discriminant 

− _m m_ 1 ( 

2 ) 

= _J_ **w** ( ) 

2 

2 2 _s_ + _s_ 1 2 

**==> picture [231 x 200] intentionally omitted <==**

--- end of page.page_number=31 ---

## Summary 

- Feature selection 

   - Supervised: drop features which don’t introduce large errors (validation set) 

   - Unsupervised: keep only uncorrelated features (drop features that don’t add much information) 

- Feature extraction 

   - Linearly combine feature into smaller set of features 

   - Supervised 

      - PCA: explain most of the total variability 

      - FA: explain most of the common variability 

   - Unsupervised 

      - LDA: best separate class instances 

Based on E Alpaydın 2004 Introduction to Machine Learning © The MIT Press (V1.1) 

--- end of page.page_number=32 ---

