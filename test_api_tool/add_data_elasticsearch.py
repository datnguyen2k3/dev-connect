$secpasswd = ConvertTo-SecureString "i+xMpJfDp_ZW4wHvsApE" -AsPlainText -Force
$mycreds = New-Object System.Management.Automation.PSCredential ("elastic", $secpasswd)

Invoke-WebRequest -Uri "http://localhost:9200/bank/_bulk?pretty&refresh" -Method Post -ContentType "application/json" -InFile "C:\Users\thanh\Desktop\dev-connect\test_api_tool\accounts.json" -Credential $mycreds


