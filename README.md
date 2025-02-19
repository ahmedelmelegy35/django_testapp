# django_testapp

## Setup github self-managed agent
Ensure your system is up to date
```bash
sudo apt update
sudo apt upgrade -y
```
Install Required Software
Some workflows might require additional software like Git, Docker, or specific language runtimes.
```bash
sudo apt install -y git
```
Create a Directory for the Runner
Choose a directory where the runner will reside.
```bash
mkdir actions-runner && cd actions-runner
```
Go to the [GitHub Actions runner releases](https://github.com/actions/runner/releases) page and download the latest runner package suitable for your operating system.
```bash
curl -O -L https://github.com/actions/runner/releases/download/v2.322.0/actions-runner-linux-arm64-2.322.0.tar.gz
# Extract the installer
tar xzf ./actions-runner-linux-arm64-2.322.0.tar.gz
```

### Obtain a Runner Token
You need a token to authenticate the runner with GitHub.
Navigate to your GitHub repository.
Click on Settings.
In the left sidebar, click Actions.
Click Runners.
Click Add Runner.
Select your operating system.
Copy the config command provided; it contains the token.
#### Run the Configuration Command
In your terminal, paste the config command you copied.

Example:
```bash
./config.sh --url https://github.com/yourusername/yourrepository --token YOUR_TOKEN  --labels  self-hosted,oracle-vm-runner
```
During configuration, you'll be prompted to:

Enter the runner name (press Enter to accept the default).
Enter the runner group (press Enter to accept the default).
Enter additional labels (you can add custom labels or press Enter to skip).
Configure the runner as a service (optional).

#### Run as a Service
To run the runner in the background and start automatically on boot:

Install the service:

```bash
sudo ./svc.sh install
```
Start the service:
```bash
sudo ./svc.sh start
```
