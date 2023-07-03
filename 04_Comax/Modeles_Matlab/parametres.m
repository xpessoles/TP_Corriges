%% COMAX %%

% Paramètres du moteur
Rm = 0.299      ; % Ohm
Lm = 0.0824e-3  ; % Henry
Kc = 30.2e-3   ; % Nm/A

Ke = 317               ; %tr/min  /V
Ke = 317*2*pi/60       ; %rad/s/V
Kem = 1/317            ; %V/(tr/min) 
J = 142                ; % g.cm²
J = 142/1000/100/100   ; % kg.m²
f = 0                  ;

% Correcteur vitesse
KP_EPOS = 2420;
KI_EPOS = 8340;
KD_EPOS = 3230;

% Correcteur courant
Kii_EPOS = 200;
Kip_EPOS = 3150;



% Paramètres mécaniques
kr = 1/15.88        ; % Réducteur
r = (104e-3)/2/pi   ; % axe linéaire m/rad
rkr = kr*r          ; % transmission moteur >> translation m/rad
M_axe = 3.4         ; % Masse de l'axe
nm = 3              ; % Nombre de masse
M_m = 1             ; % Masses 


% PROFIL DE POSITION
amax = 20000       ; % tr/min /s
amax = amax*2*pi/60; % rad /s²
vmax = 5000        ; % tr/min
vmax = vmax*2*pi/60; % rad/s




% Trapeze
L = 300             ; % mm distance à parcourir
am = 300/1000 /rkr       ; % angle moteur an radian correspondant
% Temps d'accélération : 
t1 = vmax / amax        ;  
% angle a vitesse constante : 
avc = am - t1*vmax      ;
% temps à vitesse constante
tvc = avc/vmax          ;

t2 = t1+tvc             ;
t3 = tvc+2*t1           ;