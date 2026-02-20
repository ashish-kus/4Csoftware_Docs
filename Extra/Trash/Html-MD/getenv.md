<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.get_env()

### sys.get_env()

Purpose:

sys.get_env() returns the value of an environment variable.

Usage:

\<avar\> = sys.get_env(\<ENVVAR\>);

Arguments:

alpha \<ENVVAR\> - the name of the environment variable.

Returns:

alpha \<avar\> - The value of the env var.

NULL alpha - no value defined for this env var.

There are no error returns.

Where Used:

sys.get_env() can be called from anywhere. It can be used to determine
different programs to run based on site env vars.

Example:

The following example is from the system program "sh". sys.get_env() is
used to determine which shell to run.\
\


    /*
        start the shell
    */
    if ((prog = sys.get_env("SHELL")) == "")
        prog = "/bin/sh";
    sys.msg(""); /* Force Flush of Output */
    sys.make_task(prog); /* Can't use sh() because of PCL name conflict */
    sys.exit_prog(0);

Description:

Return the value of an environment variable. It can be used to decide
one of several programs to run that may be different at different sites.
If used too much in this way, the programs will become dificult to
maintain.

Bugs/Features/Comments:

See Also:

[sys.get_clenv()](./getclenv.html)

[sys.put_env()](./putenv.html)

\
\
[Back to Top](#TOPOFPAGE)
