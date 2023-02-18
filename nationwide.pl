:- module(interestcompartible,
    [ major/1
    , interestrelation/3
    , interestcompatible/3
    , interest/1
    , student/2
    , interested/2
    ]).




    student('aaron', 'cs').
student('melinda', 'it').
student('tionna', 'cs').
student('clavine', 'cs').
student('lloyd', 'it').
student('virgil', 'it').
student('jordan', 'unknown').
student('tahron', 'cs').
student('camden', 'cs').
student('quentin', 'it').
student('kai', 'it').

interestrelation('cs', 'gis', 'aaron').
interestrelation('it', 'security', 'melinda').
interestrelation('cs', 'ug', 'tionna').
interestrelation('cs', 'swENG', 'clavine').
interestrelation('it', 'ug', 'lloyd').
interestrelation('it', 'swENG', 'virgil').
interestrelation('unknown', 'unknown', 'jordan').
interestrelation('cs', 'ug', 'tahron').
interestrelation('cs', 'swENG', 'camden').
interestrelation('it', 'swENG', 'quentin').
interestrelation('it', 'ds', 'kai').

interested('aaron', 'gis').
interested('melinda', 'ds').
interested('tionna', 'swENG').
interested('clavine', 'security').
interested('lloyd', 'ds').
interested('virgil', 'swENG').
interested('jordan', 'ds').
interested('tahron', 'swENG').
interested('camden', 'ds').
interested('quentin', 'swENG').
interested('kai', 'ds').

interest('cs').
interest('it').
interest('gis').
interest('swENG').
interest('security').
interest('ds').

major('cs').
major('it').
major('ds').

interestcompatible(X, Y, Z) :-
    student(Z, _),
    interestrelation(M, Y, Z),
    interestrelation(M, X, Z).
