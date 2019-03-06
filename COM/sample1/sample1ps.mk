
sample1ps.dll: dlldata.obj sample1_p.obj sample1_i.obj
	link /dll /out:sample1ps.dll /def:sample1ps.def /entry:DllMain dlldata.obj sample1_p.obj sample1_i.obj \
		kernel32.lib rpcndr.lib rpcns4.lib rpcrt4.lib oleaut32.lib uuid.lib \

.c.obj:
	cl /c /Ox /DWIN32 /D_WIN32_WINNT=0x0400 /DREGISTER_PROXY_DLL \
		$<

clean:
	@del sample1ps.dll
	@del sample1ps.lib
	@del sample1ps.exp
	@del dlldata.obj
	@del sample1_p.obj
	@del sample1_i.obj
