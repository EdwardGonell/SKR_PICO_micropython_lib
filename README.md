# SKR_PICO_micropython_lib
This is a micropython library to control the SKR Pico, work in progress by a noob (me).

My end goal with this project is to control 2 stepper motor for a camera mount but in the process I'll be making
a library of presets to build my project on top of. This is as simple as it may possibly get and may have plenty
of fault since I barely have any knowledge in programing. 

I'll be using some libraries already available here on github to be able to comunicate with the four TMC2209's the board has.
As of now I have the X "axis" working, have not yet tried to use several motors at the same times and I'm building on top
of kjk25's library which is an adaptation of Chr157i4n's TMC2209 library.
