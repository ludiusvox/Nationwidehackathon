:- module(interestcompartible,
    [ major/1
    , interestrelation/2
    , interestcompatible/2


    ]).

interestcompatible(X,Y) :- major(X,Z), interestrelation(Z,Y).
outputcompatibility(X,Y) :- major(X,Z), interestrelation(Z,W), interestrelation(W,Y).
interestrelation('cs', 'swENG').
interestrelation('it', 'security').
interestrelation('gis','ds').
interestrelation('swENG','security').
interestrelation('security','ds').
interestrelation('ds','swENG').
interestrelation('ug','ds').
interestrelation(_, _) :- fail, !.

major('cs').
major('it').
major('ds').
%year('ug').
%year('grad').


list([]).
list([_|T]) :- list(T).

comparison(D, D, [D]).
comparison(O, D, [O|T]) :- list(T), interestrelation(O, N), comparison(N, D, T).













