<span id="TOPOFPAGE"></span> Goto: [4C Home](../../index.html) \| [4C
Docs](../index.html) \| [System PCLs List](./index.html)

sys.set_clenv()

### sys.set_clenv()

Purpose:

sys.set_clenv() allows the server to set an environment variable on the
client.

Usage:

sys.set_clenv(\<envvar\>,\<envval\>);

Arguments:

alpha \<envvar\> - The name of the environment variable.

alpha \<envval\> - The value to set the environment variable to.

Returns:

0 - Always returns 0

Where Used:

sys.set_clenv() is most useful when the you are going to have the
4cclient run another program and you need that program to have access to
special info that you don't want to pass as arguments to the program.

Example:

Description:

sys.set_clenv() sets an environment variable in the current client
process. Only the running client and any process that the client starts
have access to environment variables set this way.

Requirements

4CServer version 4.8.1 and later

4CClient version 4.8.1 and later

Bugs/Features/Comments:

See Also:

[sys.get_clenv()](./getclenv.html)

[sys.get_env()](./getenv.html)

[sys.put_env()](./putenv.html)

\
\
[Back to Top](#TOPOFPAGE)
