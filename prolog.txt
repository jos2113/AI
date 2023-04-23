male(valerian).
male(charlie).
male(john).
male(franky).
male(joyal).
male(joston).
female(agnes).
female(faustine).
female(monica).
female(maximi).
female(jenisha).
female(jenevi).
parent(valerian,john).
parent(valerian,franky).
parent(agnes,john).
parent(agnes,franky).
parent(charlie,monica).
parent(charlie,maximi).
parent(faustine,monica).
parent(faustine,maximi).
parent(franky,joyal).
parent(maximi,jenevi).
parent(john,joston).
parent(john,jenisha).
parent(monica,joston).
parent(monica,jenisha).
mother(X,Y):- parent(X,Y), female(X), X\==Y.
father(X,Y):- parent(X,Y), male(X), X\==Y.
sibling(X,Y):- father(Z,X), father(Z,Y), X\==Y.
brother(X,Y):- father(Z, X), father(Z,Y), male(X), X\==Y.
sister(X,Y):- father(Z, X), father(Z,Y), female(X), X\==Y.
uncle(X,Y):- parent(Z,Y), sibling(X,Z), male(X), X\==Y.
aunt(X,Y):- parent(Z,Y), sibling(X,Z), female(X), X\==Y.
grandfather(X,Y):- parent(X,Z), parent(Z,Y), male(X), X\==Y.
grandmother(X,Y):- parent(X,Z), parent(Z,Y), female(X), X\==Y.
