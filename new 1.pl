male(tom).
male(bob).
male(jim).
female(pam).
female(liz).
female(ann).
female(pat).
parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).
father(X,Y):- parent(X,Y), male(X), X\==Y.
mother(X,Y):- parent(X,Y), female(X), X\==Y.
grandfather(X,Y):- parent(X,Z), parent(Z,Y), male(X), X\==Y.
grandmother(X,Y):- parent(X,Z), parent(Z,Y), female(X), X\==Y.