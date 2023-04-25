male(tom).
male(bob).
male(pat).
male(jim).
female(pam).
female(liz).
female(ann).
parent(tom,bob).
parent(pam,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).
mother(X,Y):-parent(X,Y),female(X),X\==Y.
father(X,Y):-parent(X,Y),male(X),X\==Y.
haschild(X):-parent(X,_).

/* any additional queries asked then.....
male(X).
female(X).
parent(child,parent_name).
mother(X,Y):- parent(X,Y),female(X).
father(X,Y):-parent(X,Y),male(X).
haschild(X):-parent(X,_).
sister(X,Y):-parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.
grandparent(X,Y):-parent(X,Z),parent(Z,Y).
grandmother(X,Z):-mother(X,Y),parent(Y,Z).
grandfather(X,Z):-father(X,Y),parent(Y,Z).
wife(X,Y):-parent(X,Z),parent(Y,Z),female(X),male(Y).
uncle(X,Z):-brother(X,Y),parent(Y,Z).*/

/*
OUTPUT COMMANDS
male(X).
female(Y).
mother(X,Y).
father(X,Y).
haschild(X).
brother(X,Y).
sister(X,Y).
wife(X,Y).
grandfather(X,Y).
grandmother(X,Y).
uncle(X,Y).
*/