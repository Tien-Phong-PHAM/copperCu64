

set y2tics
set multiplot layout 2,1
plot "../output/gamma-depth-Edep.txt" w l title "Edep", \
     "../output/gamma-depth-Edep-Uncertainty.txt" axis x1y2 w l title "uncertainty"

plot "../output/gamma-profile-Edep.txt"  w l title "Edep", \
     "../output/gamma-profile-Edep-Uncertainty.txt" axis x1y2 w l title "uncertainty"

unset multiplot
