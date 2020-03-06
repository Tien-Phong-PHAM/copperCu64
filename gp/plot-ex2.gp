

set y2tics
set multiplot layout 2,2
plot "../output/depth-pat-Edep.txt" w l title "edep", "../output/depth-pat-Edep-Uncertainty.txt" axis x1y2 w l title "uncertainty"

plot "../output/profile-pat-Edep.txt" w l title "edep", "../output/profile-pat-Edep-Uncertainty.txt" axis x1y2 w l title "uncertainty"

plot "../output/depth-pat-Dose.txt" w l title "dose"

plot "../output/profile-pat-Dose.txt" w l title "dose"

unset multiplot
