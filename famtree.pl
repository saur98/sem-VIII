parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).
parent(bill,tom).
parent(smith,will).
parent(bill,smith).

male(tom).
male(bob).
male(pat).
male(jim).
male(bill).
male(smith).

female(liz).
female(ann).
female(pam).
female(will).


father(X,Y):- parent(X,Y),male(X).
mother(X,Y):- parent(X,Y),female(X).

grandparent(X,Y):- parent(X,Z),parent(Z,Y).
grandfather(X,Y):- grandparent(X,Y),male(X).
grandmother(X,Y):- grandparent(X,Y),female(X).

child(X,Y):- parent(Y,X).
son(X,Y):- child(Y,X),male(X).
daughter(X,Y):- child(Y,X),female(X).

sibling(X,Y):-parent(Z,X),parent(Z,Y),not(X=Y).
sister(X,Y):- female(X),sibling(X,Y).
brother(X,Y):- male(X),sibling(X,Y).

cousin(X,Y):- parent(A,X),parent(B,Y),sibling(A,B),not(X=Y).
uncle(X,Y):- parent(Z,Y),brother(X,Z).
aunt(X,Y):-   parent(Z,Y),sister(X,Z).

husband(X,Y):- parent(X,Z),parent(Y,Z),male(X),not(X=Y).
wife(X,Y):- parent(X,Z),parent(Y,Z),female(X),not(X=Y).

stepfather(X,Y):- wife(Z,X),parent(Z,Y),not(parent(X,Y)).
stepmother(X,Y):- husband(Z,X),parent(Z,Y),not(parent(X,Y)).

happy(X):- parent(X,Y).

predecessor(X,Z):- parent(X,Z).
predecessor(X,Z):- parent(X,Y),predecessor(Y,Z).

