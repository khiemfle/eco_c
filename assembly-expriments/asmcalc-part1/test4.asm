; hello_64.asm    print a string using printf
; Assemble:	  nasm -f elf64 -l hello_64.lst  hello_64.asm
; Link:		  gcc -m64 -o hello_64  hello_64.o
; Run:		  ./hello_64 > hello_64.out
; Output:	  cat hello_64.out

; Equivalent C code
; // hello.c
; #include <stdio.h>
; int main()
; {
;   char msg[] = "Hello world\n";
;   printf("%s\n",msg);
;   return 0;
; }
	
; Declare needed C  functions
        extern	printf		; the C function, to be called

	%macro	pabc 1			; a "simple" print macro
	section .data
				.str	db	%1,0		; %1 is first actual in macro call
	section .text
							; push onto stack backwards 
				push    qword [c]	; int c
				push    qword .str 	; users string
        push    qword fmt       ; address of format string
        call    printf          ; Call C function
        add     esp,20          ; pop stack 5*4 bytes
	%endmacro

        section .data		; Data section, initialized variables
msg:	db "Hello world", 0	; C string needs 0
fmt:    db "%s, c=%q", 20, 0          ; The printf format, "\n",'0'

a:	dq	3		; 64-bit variable a initialized to 3
	b:	dq	4		; 64-bit variable b initializes to 4

	section .bss 		; uninitialized space
	c:	resq	1		; reserve a 64-bit word

        section .text           ; Code section.

        global main		; the standard gcc entry point
main:				; the program label for the entry point
  push    rbp		; set up stack frame, must be aligned

	mov     rdx, 06171e475af61h
	mov     rax, 5DEECE66Dh
	imul    rax, rdx
	lea     rcx, [rax+0Bh]
	mov     edx, 10001h
	mov     rax, rcx
	mul     rdx
	mov     rax, rcx
	sub     rax, rdx
	shr     rax, 1
	add     rax, rdx
	shr     rax, 2Fh
	mov     rdx, rax
	shl     rdx, 30h
	sub     rdx, rax
	mov     rax, rcx
	sub     rax, rdx
	; mov     cs:seed, rax
	; mov     rax, cs:seed

	; mov	rdi, rax
	; mov     rsi, rax
	; lea     rdi, fmt     ; "%zu: %s - "
	; mov     eax, 0

	; mov     [c], rax
	; push    qword [c]
	; call    printf

	mov	[c],rax		; store into c
	pabc	"c"

	; add     esp, 8
	; mov	rsi, msg
	 ; mov	rax,0		; or can be  xor  rax,rax
 ;  call    printf		; Call C function

 ;  mov	rax,[a]	 	; load a
	; add	rax,[b]		; add b
	; mov	[c],rax		; store into c
	; pabc	"c=a+b"		; invoke the print macro

	pop	rbp		; restore stack

	mov	rax,0		; normal, no error, return value
	ret			; return