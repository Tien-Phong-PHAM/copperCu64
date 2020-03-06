

set y2tics
set multiplot layout 2,2
plot "../output/depth-pat-proton-Edep.txt" w l title "edep", \
     "../output/depth-pat-proton-Edep-Uncertainty.txt" axis x1y2 w l title "unc"

plot "../output/profile-pat-proton-Edep.txt" w l title "edep", \
     "../output/profile-pat-proton-Edep-Uncertainty.txt" axis x1y2 w l title "unc"

plot "../output/depth-pat-proton-Dose.txt" w l title "dose"

plot "../output/profile-pat-proton-Dose.txt" w l title "dose"


unset multiplot
