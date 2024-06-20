**pypsrp: Python PowerShell Remoting Protocol Client Library**

**Overview:**
pypsrp is a Python library designed to interface with the PowerShell Remoting Protocol (PSRP) and Windows Remote Management (WinRM). It allows users to execute commands on remote Windows hosts from any machine that can run Python.

**APIs Provided:**
1. **Simple Client API:** For copying files and executing processes or PowerShell scripts on a remote Windows host.
2. **WSMan Interface:** For making various WSMan calls (Send, Create, Connect, Disconnect).
3. **WinRS Layer:** For executing cmd commands and other executables using the WinRM protocol.
4. **PSRP Layer:** For creating remote Runspace Pools and executing PowerShell pipelines.

**Key Features:**
- Execute cmd commands and other executables.
- Run PowerShell scripts.
- Copy files to/from remote hosts.
- Create and manage Runspace Pools and PowerShell pipelines asynchronously.
- Supports various authentication methods: Basic, Certificate, NTLM, Negotiate/Kerberos, and CredSSP (additional libraries may be required).

**Installation:**
```bash
pip install pypsrp
```
For Kerberos or CredSSP support, additional system packages and Python libraries need to be installed.

**Usage Examples:**
- **Client API:**
    ```python
    from pypsrp.client import Client

    with Client("server", username="user", password="password") as client:
        stdout, stderr, rc = client.execute_cmd("dir")
        client.copy("~/file.txt", "C:\\temp\\file.txt")
        client.fetch("C:\\temp\\file.txt", "~/file.txt")
    ```
- **WinRS/Process:**
    ```python
    from pypsrp.shell import Process, WinRS
    from pypsrp.wsman import WSMan

    wsman = WSMan("server", ssl=False, auth="basic", encryption="never",
                  username="vagrant", password="vagrant")

    with wsman, WinRS(wsman) as shell:
        process = Process(shell, "dir")
        process.invoke()
    ```
- **RunspacePool/PowerShell:**
    ```python
    from pypsrp.powershell import PowerShell, RunspacePool
    from pypsrp.wsman import WSMan

    wsman = WSMan("server", auth="kerberos",  cert_validation=False)

    with wsman, RunspacePool(wsman) as pool:
        ps = PowerShell(pool)
        ps.add_cmdlet("Get-Process").add_cmdlet("Select-Object").add_argument("Name")
        output = ps.invoke()
    ```

**Configuration Options:**
- **WSMan:**
    Options include server address, max envelope size, operation timeout, port, authentication methods, SSL usage, proxy settings, and more.
  
- **Shells:**
    - **WinRS:** Options include resource URI, input/output streams, codepage, environment variables, working directory, etc.
    - **RunspacePool:** Options include connection object, apartment state, thread options, host info, configuration name, min/max runspaces, etc.

**Logging:**
The library uses Python's logging module. Configurations can be set using a JSON file and environment variable.

**Testing:**
Changes can be tested using `tox`. Integration tests can be run against a real Windows host with the appropriate environment variables set. Additional setup can be done using Vagrant for more complex testing environments.

This summary captures the primary functionalities, usage, installation instructions, and configuration details of the `pypsrp` library.
