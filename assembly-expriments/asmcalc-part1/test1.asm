extern printf  ; the C function, to be called
 
        SECTION .data  ; Data section, initialized variables
 
        a: dd 5  ; int a=5;
        fmt:    db "a=%d, eax=%d", 10, 0 ; The printf format, "\n",'0'
 
 
        SECTION .text                   ; Code section.
 
        global main  ; the standard gcc entry point
main:    ; the program label for the entry point
        push    rbp  ; set up stack frame
        mov     rbp,rsp
 
        mov rax, [a] ; put a from store into register
        add rax, 2  ; a+2
        push rax  ; value of a+2
        push    qword [a] ; value of variable a
        push    qword fmt ; address of ctrl string
        call    printf  ; Call C function
        add     rsp, 12  ; pop stack 3 push times 4 bytes
        mov     rax,0  ;  normal, no error, return value
        ret