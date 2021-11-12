write-host "Installing ADDS"
Install-WindowsFeature AD-Domain-Services
write-host "ADDS Installed"
# Install-WindowsFeature -Name AD-Domain-Services,DNS