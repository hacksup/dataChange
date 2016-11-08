#2014400019 Lee In Sup

This program is for Data Change. We learned about WinDivert and netfilters.
Since prior homework, I changed language from c to python so I found 'pydivert', 
which is replacement for 'Windivert' by python. 

I studied how to use pydivert, tested it, captured packet, and so on.

Remind that we always have to start cmd by Administrator permission. Therefore,
I executed Pycharm with administrator permission.

Our goal is to make situation that when we search "∏∂¿Ã≈¨ ¿ËΩº", change the
result with "GILBERT". In this program, we need to capture out-bound packets and
see the payload, and remove 'gzip'. because we want deflate for changing data in
in-bound packets. and then we need to capture in-bound packets and change data
'Michael' with 'GILBERT'.

Before this homework, I used Linux ubuntu 16-04 as OS(in VMware), but on this 
homework, I used Windows10 as OS.

Before starting program, we first have to
[pip install pydivert].
Windivert is bundled in pydivert, so we do not have to install WinDivert seperately.

I bundled with pictures which is capture for searching '∏∂¿Ã≈¨ ¿ËΩº' in daum.net,
which one is before executing program, which one is after executing program.