public vuln
vuln proc near

src= qword ptr -658h
dest= byte ptr -650h
var_8= qword ptr -8

push    rbp
mov     rbp, rsp
sub     rsp, 660h
mov     [rbp+src], rdi
mov     rax, fs:28h
mov     [rbp+var_8], rax
xor     eax, eax
mov     rdx, [rbp+src]
lea     rax, [rbp+dest]
mov     rsi, rdx        ; src
mov     rdi, rax        ; dest
call    _strcpy
nop
mov     rax, [rbp+var_8]
xor     rax, fs:28h
jz      short locret_40084E