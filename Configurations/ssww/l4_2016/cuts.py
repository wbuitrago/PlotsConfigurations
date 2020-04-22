# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections


supercut='nLepton>3'

## Signal regions

cuts['loosezz'] ='loosezz'

cuts['zz_jetpt30'] ='zz && jetpt30 && abs(detajj) > 2.5 && mjj>500 && zlep_zz'
cuts['zz_jetpt50'] ='zz && jetpt50 && abs(detajj) > 2.5 && mjj>500 && zlep_zz'

