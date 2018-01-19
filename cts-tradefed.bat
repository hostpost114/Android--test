@echo off

setlocal enabledelayedexpansion
setlocal ENABLEEXTENSIONS

set CTS_ROOT=%~dp0\..\..


set JAR_DIR=%CTS_ROOT%\android-cts\tools


set JARS=compatibility-common-util-tests.jar compatibility-host-util.jar compatibility-host-util-tests.jar compatibility-tradefed-tests.jar cts-tradefed.jar cts-tradefed-tests.jar host-libprotobuf-java-full.jar hosttestlib.jar tradefed.jar


set DestJar=*.jar



set JAR_PATH=.

for %%i in (%JARS%) do (

	set JAR_PATH=!JAR_PATH!;%%i

)

for  %%a in ("%CTS_ROOT%\android-cts\testcases\*.jar") do (

    set JAR_PATH=!JAR_PATH!;%%a

)


java -Xmx1024m %RDBG_FLAG% -cp %JAR_PATH% -DCTS_ROOT=%CTS_ROOT% com.android.compatibility.common.tradefed.command.CompatibilityConsole %*

pause

