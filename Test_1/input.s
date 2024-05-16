	.file	"file_1.cpp"
	.text
	.globl	_Z3sumPii
	.def	_Z3sumPii;	.scl	2;	.type	32;	.endef
	.seh_proc	_Z3sumPii
_Z3sumPii:
.LFB2220:
	pushq	%rbp
	.seh_pushreg	%rbp
	pushq	%rbx
	.seh_pushreg	%rbx
	subq	$40, %rsp
	.seh_stackalloc	40
	leaq	32(%rsp), %rbp
	.seh_setframe	%rbp, 32
	.seh_endprologue
	movq	%rcx, 32(%rbp)
	movl	%edx, 40(%rbp)
	cmpl	$0, 40(%rbp)
	jne	.L2
	movl	$0, %eax
	jmp	.L3
.L2:
	movq	32(%rbp), %rax
	movl	(%rax), %ebx
	movl	40(%rbp), %eax
	leal	-1(%rax), %edx
	movq	32(%rbp), %rax
	addq	$4, %rax
	movq	%rax, %rcx
	call	_Z3sumPii
	addl	%ebx, %eax
.L3:
	addq	$40, %rsp
	popq	%rbx
	popq	%rbp
	ret
	.seh_endproc
	.def	__main;	.scl	2;	.type	32;	.endef
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
.LFB2221:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$64, %rsp
	.seh_stackalloc	64
	.seh_endprologue
	call	__main
	movl	$12, -32(%rbp)
	movl	$3, -28(%rbp)
	movl	$4, -24(%rbp)
	movl	$15, -20(%rbp)
	movl	$4, -4(%rbp)
	movl	-4(%rbp), %edx
	leaq	-32(%rbp), %rax
	movq	%rax, %rcx
	call	_Z3sumPii
	movl	%eax, %edx
	movq	.refptr._ZSt4cout(%rip), %rax
	movq	%rax, %rcx
	call	_ZNSolsEi
	movl	$0, %eax
	addq	$64, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
_ZNSt8__detail30__integer_to_chars_is_unsignedIjEE:
	.byte	1
_ZNSt8__detail30__integer_to_chars_is_unsignedImEE:
	.byte	1
_ZNSt8__detail30__integer_to_chars_is_unsignedIyEE:
	.byte	1
	.ident	"GCC: (Rev6, Built by MSYS2 project) 13.2.0"
	.def	_ZNSolsEi;	.scl	2;	.type	32;	.endef
	.section	.rdata$.refptr._ZSt4cout, "dr"
	.globl	.refptr._ZSt4cout
	.linkonce	discard
.refptr._ZSt4cout:
	.quad	_ZSt4cout
