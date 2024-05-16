	.file	"file_1.cpp"
	.text
	.p2align 4
	.globl	_Z3sumPii
	.def	_Z3sumPii;	.scl	2;	.type	32;	.endef
	.seh_proc	_Z3sumPii
_Z3sumPii:
.LFB1809:
	.seh_endprologue
	xorl	%eax, %eax
	testl	%edx, %edx
	je	.L1
	movl	%edx, %edx
	xorl	%eax, %eax
	leaq	(%rcx,%rdx,4), %r8
	.p2align 4,,10
	.p2align 3
.L4:
	movl	(%rcx), %edx
	addq	$4, %rcx
	addl	%edx, %eax
	cmpq	%r8, %rcx
	jne	.L4
.L1:
	ret
	.seh_endproc
	.def	__main;	.scl	2;	.type	32;	.endef
	.section	.text.startup,"x"
	.p2align 4
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
.LFB1810:
	subq	$40, %rsp
	.seh_stackalloc	40
	.seh_endprologue
	call	__main
	movq	.refptr._ZSt4cout(%rip), %rcx
	movl	$34, %edx
	call	_ZNSolsEi
	xorl	%eax, %eax
	addq	$40, %rsp
	ret
	.seh_endproc
	.ident	"GCC: (Rev6, Built by MSYS2 project) 13.2.0"
	.def	_ZNSolsEi;	.scl	2;	.type	32;	.endef
	.section	.rdata$.refptr._ZSt4cout, "dr"
	.globl	.refptr._ZSt4cout
	.linkonce	discard
.refptr._ZSt4cout:
	.quad	_ZSt4cout
